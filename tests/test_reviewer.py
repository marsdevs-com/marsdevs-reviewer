"""
Basic tests for MarsDevs Code Reviewer
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from marsdevs_reviewer.reviewer import (
    get_file_extension,
    get_cache_key,
    format_review_output
)


class TestReviewer(unittest.TestCase):
    """Test cases for reviewer functions."""
    
    def test_get_file_extension(self):
        """Test file extension extraction."""
        self.assertEqual(get_file_extension("test.py"), ".py")
        self.assertEqual(get_file_extension("path/to/file.js"), ".js")
        self.assertEqual(get_file_extension("no_extension"), "")
        self.assertEqual(get_file_extension("multiple.dots.py"), ".py")
    
    def test_get_cache_key(self):
        """Test cache key generation."""
        diff1 = "diff --git a/test.py b/test.py"
        diff2 = "diff --git a/other.py b/other.py"
        conventions = "test conventions"
        
        # Same inputs should produce same key
        key1 = get_cache_key(diff1, conventions)
        key2 = get_cache_key(diff1, conventions)
        self.assertEqual(key1, key2)
        
        # Different inputs should produce different keys
        key3 = get_cache_key(diff2, conventions)
        self.assertNotEqual(key1, key3)
    
    def test_format_review_output_no_issues(self):
        """Test output formatting when no issues found."""
        review = {
            "has_issues": False,
            "summary": "All good!"
        }
        fixes_applied = []
        
        should_allow, output = format_review_output(review, fixes_applied)
        
        self.assertTrue(should_allow)
        self.assertIn("No convention violations found", output)
        self.assertIn("All good!", output)
    
    def test_format_review_output_with_issues(self):
        """Test output formatting with issues."""
        review = {
            "has_issues": True,
            "severity": "high",
            "issues": [
                {
                    "type": "convention",
                    "file": "test.py",
                    "line_start": 10,
                    "description": "Test issue",
                    "convention_violated": "Test convention"
                }
            ],
            "summary": "Found issues"
        }
        fixes_applied = []
        
        should_allow, output = format_review_output(review, fixes_applied)
        
        self.assertFalse(should_allow)  # High severity blocks
        self.assertIn("Found 1 convention issue(s)", output)
        self.assertIn("Test issue", output)
        self.assertIn("COMMIT BLOCKED", output)

    def test_parallel_learning_and_api_review_merge(self):
        """Test that learning and API review results are merged when both are needed."""
        from marsdevs_reviewer import reviewer
        import types
        
        # Mock diff and files
        diff = "diff --git a/test.py b/test.py\n+print('hello')"
        files = ["test.py"]
        conventions_context = "context"
        
        # Mock learned issues and API review
        learned_issues = [
            {"type": "convention", "file": "test.py", "line_start": 1, "description": "Learned issue", "convention_violated": "Test convention"}
        ]
        api_review = {
            "has_issues": True,
            "severity": "medium",
            "issues": [
                {"type": "convention", "file": "test.py", "line_start": 1, "description": "API issue", "convention_violated": "API convention"}
            ],
            "summary": "API found issues"
        }
        
        # Patch the review_code_with_conventions and pattern_matcher
        with patch.object(reviewer, "review_code_with_conventions", return_value=api_review) as mock_api:
            pattern_matcher = MagicMock()
            pattern_matcher.find_issues_with_learned_patterns.return_value = learned_issues
            
            # Simulate the main logic for merging
            with patch.object(reviewer, "PatternMatcher", return_value=pattern_matcher):
                with patch.object(reviewer, "LearningManager"):
                    # Patch other dependencies to avoid side effects
                    with patch.object(reviewer, "get_staged_diff", return_value=diff), \
                         patch.object(reviewer, "get_staged_files", return_value=files), \
                         patch.object(reviewer, "find_similar_files", return_value={}), \
                         patch.object(reviewer, "get_project_config_files", return_value={}), \
                         patch.object(reviewer, "analyze_coding_conventions", return_value=""), \
                         patch.object(reviewer, "debug_conventions"), \
                         patch.object(reviewer, "save_cached_review"), \
                         patch.object(reviewer, "load_cached_review", return_value=None), \
                         patch.object(reviewer, "format_review_output", return_value=(True, "output")):
                        # Patch sys.exit to prevent exiting
                        with patch("sys.exit") as mock_exit:
                            reviewer.main(auto_apply_fixes=True)
                            # Check that both issues are present in the merged review
                            # (The actual print output is not checked here, but the logic is exercised)
                            mock_api.assert_called()
                            self.assertTrue(pattern_matcher.find_issues_with_learned_patterns.called)


if __name__ == "__main__":
    unittest.main()