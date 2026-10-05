"""Core functionality for Agent Jorge."""

from dataclasses import dataclass


@dataclass
class AgentJorge:
    """Main Agent Jorge instance."""

    name: str = "Agent Jorge"

    def greet(self, target: str = "World") -> str:
        """Return a greeting message.

        Args:
            target: The entity to greet.

        Returns:
            Formatted greeting string.
        """
        return f"Hello, {target}! Welcome to {self.name}."
