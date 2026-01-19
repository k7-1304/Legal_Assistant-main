"""Argument miner endpoint for extracting legal arguments."""
from fastapi import APIRouter
from models.schemas import (
    ArgumentsRequest,
    ArgumentsResponse,
    SourceCase,
    SearchFilters
)
from services.mock_retriever import mock_retriever

router = APIRouter(prefix="/api/v1")


@router.post("/arguments", response_model=ArgumentsResponse)
async def extract_arguments(request: ArgumentsRequest):
    """
    Extract legal arguments from judgments.
    
    Args:
        request: Arguments request with legal scenario
        
    Returns:
        Prosecution/defense arguments and winning strategy
    """
    # Search for relevant judgments
    search_filters = SearchFilters(doc_type="judgment")
    
    results, _ = mock_retriever.search(
        query=request.scenario,
        filters=search_filters,
        top_k=5
    )
    
    # Pattern-based argument extraction
    scenario_lower = request.scenario.lower()
    
    # Default arguments
    prosecution_args = [
        "Evidence presented by prosecution",
        "Statutory provisions violated",
        "Intent and mens rea established"
    ]
    defense_args = [
        "Lack of sufficient evidence",
        "Procedural irregularities",
        "Mitigating circumstances"
    ]
    winning_arg = "Defense argument was successful"
    court_ruling = "Court ruled in favor of defense"
    
    # Specific patterns
    if "murder" in scenario_lower or "302" in scenario_lower or "103" in scenario_lower:
        prosecution_args = [
            "Injury on vital part (head)",
            "Brain matter visible indicating severe injury",
            "Death resulted from the blow"
        ]
        defense_args = [
            "Solitary blow - no repeated attack",
            "Victim was sleeping - no premeditation",
            "No clear intent to kill"
        ]
        winning_arg = "Defense argument of 'single blow without intent to kill' was successful"
        court_ruling = "Converted Section 302 (Murder) to Section 304 (Culpable Homicide not amounting to Murder)"
    
    elif "cheque" in scenario_lower or "138" in scenario_lower:
        prosecution_args = [
            "Cheque dishonoured due to insufficient funds",
            "Legal notice sent and not complied with",
            "Accused was director/in charge of company"
        ]
        defense_args = [
            "Accused not involved in day-to-day operations",
            "No knowledge of the offence",
            "Exercised due diligence to prevent offence"
        ]
        winning_arg = "Prosecution argument prevailed in most cases"
        court_ruling = "Accused held liable under Section 141 NI Act"
    
    # Get source case
    source_case = SourceCase(
        title="State vs Sonu",
        court="Gujarat High Court",
        url="https://indiankanoon.org/doc/example002"
    )
    
    if results:
        first_result = results[0]
        source_case = SourceCase(
            title=first_result.metadata.title or "Unknown Case",
            court=first_result.metadata.court or "Unknown Court",
            url=first_result.metadata.doc_url or "https://indiankanoon.org"
        )
    
    return ArgumentsResponse(
        prosecution_arguments=prosecution_args,
        defense_arguments=defense_args,
        winning_argument=winning_arg,
        court_ruling=court_ruling,
        source_case=source_case
    )
