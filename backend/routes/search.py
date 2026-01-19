"""Search endpoint for hybrid search."""
from fastapi import APIRouter
from models.schemas import SearchRequest, SearchResponse
from services.mock_retriever import mock_retriever

router = APIRouter(prefix="/api/v1")


@router.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    Perform hybrid search on legal documents.
    
    Args:
        request: Search request with query and optional filters
        
    Returns:
        Search results with relevance scores
    """
    results, query_time = mock_retriever.search(
        query=request.query,
        filters=request.filters,
        top_k=request.top_k
    )
    
    return SearchResponse(
        results=results,
        total=len(results),
        query_time_ms=query_time
    )
