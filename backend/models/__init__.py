"""Package initialization for models."""
from .schemas import (
    # Metadata
    Metadata,
    # Documents
    LegalChunk,
    JudgmentChunk,
    # Search
    SearchFilters,
    SearchRequest,
    SearchResult,
    SearchResponse,
    # Autocomplete
    AutocompleteResponse,
    # Chat
    ChatRequest,
    SourceReference,
    ChatResponse,
    # Viability
    ViabilityFilters,
    ViabilityRequest,
    SupportingCase,
    ViabilityResponse,
    # Arguments
    ArgumentsRequest,
    SourceCase,
    ArgumentsResponse,
    # Clauses
    ClausesRequest,
    ClauseResult,
    ClausesResponse,
    # Health
    HealthResponse,
)

__all__ = [
    "Metadata",
    "LegalChunk",
    "JudgmentChunk",
    "SearchFilters",
    "SearchRequest",
    "SearchResult",
    "SearchResponse",
    "AutocompleteResponse",
    "ChatRequest",
    "SourceReference",
    "ChatResponse",
    "ViabilityFilters",
    "ViabilityRequest",
    "SupportingCase",
    "ViabilityResponse",
    "ArgumentsRequest",
    "SourceCase",
    "ArgumentsResponse",
    "ClausesRequest",
    "ClauseResult",
    "ClausesResponse",
    "HealthResponse",
]
