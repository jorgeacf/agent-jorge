"""Tests for the core module."""

from agent_jorge.core import AgentJorge


def test_agent_default_initialization(agent: AgentJorge) -> None:
    """Test default agent attributes."""
    assert agent.name == "Agent Jorge"


def test_agent_custom_name() -> None:
    """Test agent initialization with a custom name."""
    custom_agent = AgentJorge(name="Custom Agent")
    assert custom_agent.name == "Custom Agent"


def test_agent_greet_default(agent: AgentJorge) -> None:
    """Test default greeting message."""
    greeting = agent.greet()
    assert greeting == "Hello, World! Welcome to Agent Jorge."


def test_agent_greet_custom_target(agent: AgentJorge) -> None:
    """Test greeting with a specific target."""
    greeting = agent.greet("Alice")
    assert greeting == "Hello, Alice! Welcome to Agent Jorge."
