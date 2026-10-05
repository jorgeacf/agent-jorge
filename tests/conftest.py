"""Pytest fixtures and test configurations."""

import pytest

from agent_jorge.core import AgentJorge


@pytest.fixture
def agent() -> AgentJorge:
    """Fixture providing a default AgentJorge instance."""
    return AgentJorge()
