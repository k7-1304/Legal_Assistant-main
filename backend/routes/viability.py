"""Viability predictor endpoint for case outcome prediction."""
from fastapi import APIRouter
from models.schemas import (
    ViabilityRequest,
    ViabilityResponse,
    SupportingCase,
    SearchFilters
)
from services.mock_retriever import mock_retriever

router = APIRouter(prefix="/api/v1")


@router.post("/viability", response_model=ViabilityResponse)
async def predict_viability(request: ViabilityRequest):
    """
    Predict case outcome based on similar judgments.
    
    Args:
        request: Viability request with case facts
        
    Returns:
        Prediction with confidence and supporting cases
    """
    # Search for similar judgments
    search_filters = SearchFilters(doc_type="judgment")
    
    if request.filters:
        if request.filters.court:
            search_filters.court = request.filters.court
        if request.filters.case_type:
            search_filters.case_type = request.filters.case_type
    
    results, _ = mock_retriever.search(
        query=request.facts,
        filters=search_filters,
        top_k=10
    )
    
    # Analyze outcomes
    outcomes = []
    supporting_cases = []
    
    for result in results:
        if result.metadata.outcome:
            outcomes.append(result.metadata.outcome)
            
            supporting_cases.append(
                SupportingCase(
                    title=result.metadata.title or "Unknown Case",
                    court=result.metadata.court or "Unknown Court",
                    outcome=result.metadata.outcome,
                    relevance=result.score,
                    url=result.metadata.doc_url or "https://indiankanoon.org"
                )
            )
    
    # Determine prediction
    if not outcomes:
        prediction = "MEDIUM"
        confidence = 0.5
        reasoning = "Insufficient similar cases found for accurate prediction."
    else:
        allowed_count = sum(1 for o in outcomes if "allow" in o.lower())
        dismissed_count = sum(1 for o in outcomes if "dismiss" in o.lower())
        total = len(outcomes)
        
        if allowed_count >= total * 0.7:
            prediction = "HIGH"
            confidence = 0.85
            reasoning = f"Based on {allowed_count} out of {total} similar cases being allowed, your case has high viability."
        elif dismissed_count >= total * 0.7:
            prediction = "LOW"
            confidence = 0.85
            reasoning = f"Based on {dismissed_count} out of {total} similar cases being dismissed, your case has low viability."
        else:
            prediction = "MEDIUM"
            confidence = 0.65
            reasoning = f"Mixed outcomes in similar cases ({allowed_count} allowed, {dismissed_count} dismissed). Outcome is uncertain."
    
    return ViabilityResponse(
        prediction=prediction,
        confidence=confidence,
        reasoning=reasoning,
        supporting_cases=supporting_cases[:5]  # Top 5 cases
    )
