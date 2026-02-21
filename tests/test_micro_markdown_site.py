"""Tests for micro-markdown-site."""

import pytest
from micro_markdown_site import site


class TestSite:
    """Test suite for site."""

    def test_basic(self):
        """Test basic usage."""
        result = site("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            site("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = site(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
