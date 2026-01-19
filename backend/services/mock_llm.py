"""Mock LLM service returning predefined responses."""
from typing import List, Dict, Optional
import time
from models.schemas import SourceReference


class MockLLM:
    """Mock LLM service for testing."""
    
    def __init__(self):
        """Initialize mock LLM with chat memory."""
        self.chat_memory: Dict[str, List[Dict[str, str]]] = {}
    
    def generate_chat_response(
        self,
        query: str,
        session_id: str,
        retrieved_chunks: List[Dict]
    ) -> tuple[str, List[SourceReference]]:
        """
        Generate mock chat response.
        
        Args:
            query: User query
            session_id: Session identifier
            retrieved_chunks: Retrieved context chunks
            
        Returns:
            Tuple of (answer, sources)
        """
        # Simulate LLM latency
        time.sleep(0.15)
        
        # Store in memory
        if session_id not in self.chat_memory:
            self.chat_memory[session_id] = []
        
        self.chat_memory[session_id].append({
            "role": "user",
            "content": query
        })
        
        # Generate response based on query patterns
        answer = self._generate_answer(query, retrieved_chunks)
        
        self.chat_memory[session_id].append({
            "role": "assistant",
            "content": answer
        })
        
        # Keep only last 10 messages
        if len(self.chat_memory[session_id]) > 10:
            self.chat_memory[session_id] = self.chat_memory[session_id][-10:]
        
        # Create source references
        sources = self._create_sources(retrieved_chunks)
        
        return answer, sources
    
    def _generate_answer(self, query: str, chunks: List[Dict]) -> str:
        """Generate answer based on query patterns."""
        query_lower = query.lower()
        
        # Pattern matching for common queries
        if "murder" in query_lower and "punishment" in query_lower:
            if "bns" in query_lower:
                return "Under Section 103 of the Bharatiya Nyaya Sanhita (BNS), 2023, whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine."
            else:
                return "Under Section 302 of the Indian Penal Code (IPC), 1860, whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine."
        
        elif "cheque" in query_lower and ("dishonour" in query_lower or "bounce" in query_lower):
            return "Under Section 138 of the Negotiable Instruments Act, 1881, dishonour of a cheque for insufficiency of funds is a criminal offence. The person shall be punished with imprisonment for a term which may extend to two years, or with fine which may extend to twice the amount of the cheque, or with both."
        
        elif "wife" in query_lower and "liable" in query_lower:
            return "Based on the judgment in Priti Bhojnagarwala vs State Of Gujarat, the court held that in an association of individuals, the wife is deemed to be a director and is responsible for the conduct of business. Therefore, she can be held liable under Section 141 of the NI Act even without signing the cheque."
        
        elif "settlement" in query_lower and ("quash" in query_lower or "fir" in query_lower):
            return "Based on the judgment in Rabari Sagarbhai vs State, when parties have settled the dispute amicably, the High Court can exercise its inherent powers under Section 482 BNSS to quash the FIR. The court held that continuation of criminal proceedings would amount to abuse of process of law when the dispute is overwhelmingly civil in nature and has been resolved."
        
        elif "culpable homicide" in query_lower or ("murder" in query_lower and "304" in query_lower):
            return "Based on the judgment in State vs Sonu, if the accused inflicted only a solitary blow without clear intention to kill, the offence may be classified as culpable homicide not amounting to murder under Section 304 IPC instead of murder under Section 302 IPC. The court considers factors like whether it was a single blow, lack of premeditation, and absence of repeated attacks."
        
        # Generic response using first chunk
        elif chunks:
            first_chunk = chunks[0]
            content = first_chunk.get("content", "")
            metadata = first_chunk.get("metadata", {})
            
            if metadata.get("doc_type") == "statute":
                act_name = metadata.get("act_name", "the Act")
                section_id = metadata.get("section_id", "")
                return f"According to Section {section_id} of {act_name}, {content[:200]}..."
            else:
                title = metadata.get("title", "the judgment")
                return f"Based on {title}, {content[:200]}..."
        
        return "I don't have sufficient information in my knowledge base to answer this question accurately. Please try rephrasing your query or provide more specific details."
    
    def _create_sources(self, chunks: List[Dict]) -> List[SourceReference]:
        """Create source references from chunks."""
        sources = []
        
        for chunk in chunks[:3]:  # Top 3 sources
            metadata = chunk.get("metadata", {})
            score = chunk.get("score", 0.8)
            
            source = SourceReference(
                section_id=metadata.get("section_id"),
                act_name=metadata.get("act_name"),
                chapter=metadata.get("chapter"),
                title=metadata.get("title"),
                court=metadata.get("court"),
                relevance_score=score
            )
            sources.append(source)
        
        return sources


# Global LLM instance
mock_llm = MockLLM()
