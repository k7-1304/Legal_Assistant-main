"""Pydantic models for API request/response validation."""
from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# ============================================================================
# Metadata Models
# ============================================================================

class Metadata(BaseModel):
    """Metadata for legal documents."""
    doc_type: Literal["statute", "judgment"]
    act_name: Optional[str] = None
    section_id: Optional[str] = None
    chapter: Optional[str] = None
    category: Optional[str] = None
    chunk_type: Optional[str] = None
    has_illustration: Optional[bool] = None
    has_proviso: Optional[bool] = None
    # Judgment specific
    title: Optional[str] = None
    court: Optional[str] = None
    case_type: Optional[str] = None
    outcome: Optional[str] = None
    acts_cited: Optional[List[str]] = None
    doc_url: Optional[str] = None


# ============================================================================
# Document Models
# ============================================================================

class LegalChunk(BaseModel):
    """Legal document chunk (Acts/Sections)."""
    id: str
    text_for_embedding: str
    raw_content: str
    metadata: Metadata


class JudgmentChunk(BaseModel):
    """Judgment document chunk."""
    id: str
    text_for_embedding: str
    raw_content: str
    metadata: Metadata


# ============================================================================
# Search Models
# ============================================================================

class SearchFilters(BaseModel):
    """Filters for search queries."""
    doc_type: Optional[Literal["statute", "judgment"]] = None
    act_name: Optional[str] = None
    category: Optional[str] = None
    court: Optional[str] = None
    case_type: Optional[str] = None


class SearchRequest(BaseModel):
    """Search request payload."""
    query: str = Field(..., min_length=1, description="Search query")
    filters: Optional[SearchFilters] = None
    top_k: int = Field(default=5, ge=1, le=50, description="Number of results")


class SearchResult(BaseModel):
    """Individual search result."""
    id: str
    content: str
    metadata: Metadata
    score: float = Field(..., ge=0.0, le=1.0)


class SearchResponse(BaseModel):
    """Search response payload."""
    results: List[SearchResult]
    total: int
    query_time_ms: int


# ============================================================================
# Autocomplete Models
# ============================================================================

class AutocompleteResponse(BaseModel):
    """Autocomplete suggestions response."""
    suggestions: List[str]


# ============================================================================
# Chat Models
# ============================================================================

class ChatRequest(BaseModel):
    """Chat request payload."""
    session_id: str = Field(..., description="Unique session identifier")
    query: str = Field(..., min_length=1, description="User query")


class SourceReference(BaseModel):
    """Source reference in chat response."""
    section_id: Optional[str] = None
    act_name: Optional[str] = None
    chapter: Optional[str] = None
    title: Optional[str] = None
    court: Optional[str] = None
    relevance_score: float = Field(..., ge=0.0, le=1.0)


class ChatResponse(BaseModel):
    """Chat response payload."""
    answer: str
    sources: List[SourceReference]
    session_id: str


# ============================================================================
# Viability Predictor Models
# ============================================================================

class ViabilityFilters(BaseModel):
    """Filters for viability prediction."""
    court: Optional[str] = None
    case_type: Optional[str] = None


class ViabilityRequest(BaseModel):
    """Viability prediction request."""
    facts: str = Field(..., min_length=10, description="Case facts description")
    filters: Optional[ViabilityFilters] = None


class SupportingCase(BaseModel):
    """Supporting case for viability prediction."""
    title: str
    court: str
    outcome: str
    relevance: float = Field(..., ge=0.0, le=1.0)
    url: str


class ViabilityResponse(BaseModel):
    """Viability prediction response."""
    prediction: Literal["HIGH", "MEDIUM", "LOW"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str
    supporting_cases: List[SupportingCase]


# ============================================================================
# Argument Miner Models
# ============================================================================

class ArgumentsRequest(BaseModel):
    """Arguments extraction request."""
    scenario: str = Field(..., min_length=10, description="Legal scenario description")


class SourceCase(BaseModel):
    """Source case reference."""
    title: str
    court: str
    url: str


class ArgumentsResponse(BaseModel):
    """Arguments extraction response."""
    prosecution_arguments: List[str]
    defense_arguments: List[str]
    winning_argument: str
    court_ruling: str
    source_case: SourceCase


# ============================================================================
# Clause Search Models
# ============================================================================

class ClausesRequest(BaseModel):
    """Clause search request."""
    need: str = Field(..., min_length=5, description="Drafting need description")


class ClauseResult(BaseModel):
    """Individual clause result."""
    text: str
    source: str
    court: str
    citation: str


class ClausesResponse(BaseModel):
    """Clause search response."""
    clauses: List[ClauseResult]


# ============================================================================
# Health Check Models
# ============================================================================

class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    service: str
    version: str
    timestamp: datetime
