"""Package initialization for services."""
from .mock_data import (
    MOCK_LEGAL_CHUNKS,
    MOCK_JUDGMENT_CHUNKS,
    AUTOCOMPLETE_DATA,
    get_all_legal_chunks,
    get_all_judgment_chunks,
    get_all_chunks,
)
from .mock_retriever import mock_retriever
from .mock_llm import mock_llm

__all__ = [
    "MOCK_LEGAL_CHUNKS",
    "MOCK_JUDGMENT_CHUNKS",
    "AUTOCOMPLETE_DATA",
    "get_all_legal_chunks",
    "get_all_judgment_chunks",
    "get_all_chunks",
    "mock_retriever",
    "mock_llm",
]
