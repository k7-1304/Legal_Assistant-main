"""Chat endpoint for RAG-based conversational Q&A."""
from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.mock_retriever import mock_retriever
from services.mock_llm import mock_llm

router = APIRouter(prefix="/api/v1")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    RAG-based conversational legal Q&A.
    
    Args:
        request: Chat request with session_id and query
        
    Returns:
        Answer with source citations
    """
    # Retrieve relevant chunks
    results, _ = mock_retriever.search(
        query=request.query,
        filters=None,
        top_k=5
    )
    
    # Convert to dict format for LLM
    chunks = [
        {
            "content": result.content,
            "metadata": result.metadata.model_dump(),
            "score": result.score
        }
        for result in results
    ]
    
    # Generate response using mock LLM
    answer, sources = mock_llm.generate_chat_response(
        query=request.query,
        session_id=request.session_id,
        retrieved_chunks=chunks
    )
    
    return ChatResponse(
        answer=answer,
        sources=sources,
        session_id=request.session_id
    )
