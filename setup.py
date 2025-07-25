"""
Setup script for MarsDevs Code Reviewer
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="marsdevs-reviewer",
    version="1.1.3",
    author="MarsDevs Team",
    author_email="team@marsdevs.com",
    description="AI-powered code review tool that learns from your repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/marsdevs-com/marsdevs-reviewer/",
    project_urls={
        "Bug Tracker": "http://github.com/marsdevs-com/marsdevs-reviewer/issues",
        "Documentation": "http://github.com/marsdevs-com/marsdevs-reviewer/#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Version Control :: Git",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "marsdevs-reviewer=marsdevs_reviewer.cli:main",
        ],
    },
    keywords="git pre-commit code-review ai conventions linting",
)