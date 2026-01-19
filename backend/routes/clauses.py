"""Clause search endpoint for petition drafting."""
from fastapi import APIRouter
from models.schemas import (
    ClausesRequest,
    ClausesResponse,
    ClauseResult,
    SearchFilters
)
from services.mock_retriever import mock_retriever

router = APIRouter(prefix="/api/v1")


@router.post("/clauses", response_model=ClausesResponse)
async def search_clauses(request: ClausesRequest):
    """
    Find exact legal phrasing for petition drafting.
    
    Args:
        request: Clauses request with drafting need
        
    Returns:
        Relevant clauses with citations
    """
    # Search for relevant judgments
    search_filters = SearchFilters(doc_type="judgment")
    
    results, _ = mock_retriever.search(
        query=request.need,
        filters=search_filters,
        top_k=5
    )
    
    # Extract clauses
    clauses = []
    
    # Pattern-based clause extraction
    need_lower = request.need.lower()
    
    if "quash" in need_lower and "settlement" in need_lower:
        clauses.append(
            ClauseResult(
                text="The continuation of criminal proceedings would amount to abuse of process of law and court, and the trial would be futile, as the dispute is overwhelmingly civil in nature and has been resolved.",
                source="Rabari Sagarbhai vs State",
                court="Gujarat High Court",
                citation="Citing Gian Singh vs State of Punjab"
            )
        )
        clauses.append(
            ClauseResult(
                text="The parties having settled the matter amicably and there being no useful purpose in continuing the criminal proceedings, the same are hereby quashed in exercise of powers under Section 482 BNSS.",
                source="Gian Singh vs State of Punjab",
                court="Supreme Court of India",
                citation="Landmark judgment on quashing powers"
            )
        )
    
    elif "bail" in need_lower:
        clauses.append(
            ClauseResult(
                text="The applicant has deep roots in society, is not a flight risk, and the investigation is complete. There is no likelihood of the applicant tampering with evidence or influencing witnesses.",
                source="Generic Bail Application",
                court="Various High Courts",
                citation="Standard bail application clause"
            )
        )
    
    elif "anticipatory bail" in need_lower:
        clauses.append(
            ClauseResult(
                text="The applicant apprehends arrest in connection with the alleged offence. The allegations are false and motivated. The applicant is ready to cooperate with the investigation and will not abscond.",
                source="Generic Anticipatory Bail Application",
                court="Various High Courts",
                citation="Standard anticipatory bail clause"
            )
        )
    
    else:
        # Generic clauses from search results
        for result in results[:3]:
            # Extract a relevant portion
            content = result.content
            if len(content) > 200:
                content = content[:200] + "..."
            
            clauses.append(
                ClauseResult(
                    text=content,
                    source=result.metadata.title or "Unknown Case",
                    court=result.metadata.court or "Unknown Court",
                    citation="Relevant judgment excerpt"
                )
            )
    
    return ClausesResponse(clauses=clauses)
