"""Tests for the CLI module."""

import pytest

from agent_jorge.cli import main, parse_args


def test_cli_parse_args_default() -> None:
    """Test argument parser with default values."""
    args = parse_args([])
    assert args.name == "World"


def test_cli_parse_args_custom() -> None:
    """Test argument parser with custom name flag."""
    args = parse_args(["--name", "Alice"])
    assert args.name == "Alice"


def test_cli_main(capsys: pytest.CaptureFixture[str]) -> None:
    """Test main function execution and standard output."""
    exit_code = main(["--name", "Bob"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Hello, Bob! Welcome to Agent Jorge.\n" in captured.out
