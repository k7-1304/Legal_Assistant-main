"""Autocomplete endpoint for suggestions."""
from fastapi import APIRouter, Query
from models.schemas import AutocompleteResponse
from services.mock_data import AUTOCOMPLETE_DATA

router = APIRouter(prefix="/api/v1")


@router.get("/autocomplete", response_model=AutocompleteResponse)
async def autocomplete(q: str = Query(..., min_length=1, description="Query string")):
    """
    Get autocomplete suggestions for sections and acts.
    
    Args:
        q: Query string for autocomplete
        
    Returns:
        List of matching suggestions
    """
    q_lower = q.lower()
    
    # Filter suggestions that match the query
    suggestions = [
        suggestion for suggestion in AUTOCOMPLETE_DATA
        if q_lower in suggestion.lower()
    ]
    
    # Limit to top 10
    suggestions = suggestions[:10]
    
    return AutocompleteResponse(suggestions=suggestions)
