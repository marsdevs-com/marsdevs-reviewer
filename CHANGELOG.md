# Changelog

All notable changes to MarsDevs Code Reviewer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.3] - 2024-01-18

### Added
- Comprehensive CHANGELOG.md for version tracking
- Changelog reference in README.md
- CHANGELOG.md included in package distribution via MANIFEST.in

### Changed
- Improved package documentation for PyPI users

## [1.1.2] - 2024-01-18

### Fixed
- Fixed TTY detection issue preventing commits in non-interactive environments (PR #1)
- Pre-commit hook now gracefully handles non-TTY scenarios (automated commits, CI/CD)

### Changed
- Non-interactive environments now skip interactive prompts with informative message

## [1.1.1] - 2024-01-17

### Fixed
- Fixed critical issue where AI-suggested fixes were not being applied to files
- Enhanced error handling in `apply_fix()` function with better debugging
- Improved file path resolution for fix application
- Added comprehensive error messages for troubleshooting

### Added
- Debug logging for fix application process
- File existence validation before applying fixes
- Better error reporting when fixes fail

## [1.1.0] - 2024-01-17

### Added
- **Persistent Learning System** - Reduces API calls by learning from user decisions
  - Stores accepted/rejected patterns with confidence scores
  - Skips API calls for high-confidence patterns (>70%)
  - Local storage in `.marsdevs/` directory
- New CLI commands:
  - `marsdevs-reviewer stats` - View learning statistics
  - `marsdevs-reviewer export-learning` - Export learned patterns
  - `marsdevs-reviewer reset-learning` - Clear learning data
- Learning system components:
  - `LearningManager` - Manages persistent pattern storage
  - `ConventionExtractor` - Analyzes codebase conventions
  - `PatternMatcher` - Matches code against learned patterns

### Changed
- Review process now checks learned patterns before making API calls
- Improved performance for frequently reviewed patterns

## [1.0.0] - 2024-01-16

### Added
- Initial release of MarsDevs Code Reviewer
- AI-powered pre-commit hook using Anthropic's Claude API
- Repository-specific convention learning
- Interactive fix suggestions (accept/reject/skip)
- Smart caching for faster re-reviews
- CLI commands:
  - `marsdevs-reviewer install` - Install pre-commit hook
  - `marsdevs-reviewer uninstall` - Remove pre-commit hook
  - `marsdevs-reviewer review` - Manual review of staged changes
  - `marsdevs-reviewer clear-cache` - Clear review cache
- Support for multiple file types and languages
- Debug mode with `MARSDEVS_DEBUG` environment variable
- Comprehensive error handling and logging

### Features
- Learns from existing codebase conventions
- Reviews only staged changes, not existing code
- Provides context-aware suggestions based on repository patterns
- Skips documentation and configuration files by default
- Supports bypass with `git commit --no-verify`

[1.1.3]: https://github.com/marsdevs-com/marsdevs-reviewer/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/marsdevs-com/marsdevs-reviewer/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/marsdevs-com/marsdevs-reviewer/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/marsdevs-com/marsdevs-reviewer/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/marsdevs-com/marsdevs-reviewer/releases/tag/v1.0.0