"""Command-line interface for Agent Jorge."""

import argparse
import sys
from collections.abc import Sequence

from agent_jorge.core import AgentJorge


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        argv: List of arguments (defaults to sys.argv[1:]).

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        prog="agent-jorge",
        description="Agent Jorge CLI tool.",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        default="World",
        help="Name of the person or entity to greet.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point.

    Args:
        argv: Command-line arguments.

    Returns:
        Exit code (0 for success).
    """
    args = parse_args(argv)
    agent = AgentJorge()
    print(agent.greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
