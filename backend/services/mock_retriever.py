"""Mock retrieval service simulating hybrid search."""
from typing import List, Optional, Dict, Any
import time
from models.schemas import SearchResult, SearchFilters, Metadata
from services.mock_data import get_all_chunks


class MockRetriever:
    """Mock retrieval service for testing."""
    
    def __init__(self):
        """Initialize mock retriever."""
        self.all_chunks = get_all_chunks()
    
    def search(
        self,
        query: str,
        filters: Optional[SearchFilters] = None,
        top_k: int = 5
    ) -> tuple[List[SearchResult], int]:
        """
        Perform mock hybrid search.
        
        Args:
            query: Search query
            filters: Optional filters
            top_k: Number of results to return
            
        Returns:
            Tuple of (results, query_time_ms)
        """
        start_time = time.time()
        
        # Filter chunks based on filters
        filtered_chunks = self._apply_filters(self.all_chunks, filters)
        
        # Simple keyword matching for mock search
        scored_chunks = []
        query_lower = query.lower()
        
        for chunk in filtered_chunks:
            score = self._calculate_mock_score(chunk, query_lower)
            if score > 0:
                scored_chunks.append((chunk, score))
        
        # Sort by score descending
        scored_chunks.sort(key=lambda x: x[1], reverse=True)
        
        # Take top_k
        top_chunks = scored_chunks[:top_k]
        
        # Convert to SearchResult
        results = [
            SearchResult(
                id=chunk.id,
                content=chunk.raw_content,
                metadata=chunk.metadata,
                score=round(score, 2)
            )
            for chunk, score in top_chunks
        ]
        
        query_time = int((time.time() - start_time) * 1000)
        
        return results, query_time
    
    def _apply_filters(
        self,
        chunks: List[Any],
        filters: Optional[SearchFilters]
    ) -> List[Any]:
        """Apply filters to chunks."""
        if not filters:
            return chunks
        
        filtered = chunks
        
        if filters.doc_type:
            filtered = [
                c for c in filtered
                if c.metadata.doc_type == filters.doc_type
            ]
        
        if filters.act_name:
            filtered = [
                c for c in filtered
                if c.metadata.act_name and filters.act_name.lower() in c.metadata.act_name.lower()
            ]
        
        if filters.category:
            filtered = [
                c for c in filtered
                if c.metadata.category and filters.category.lower() in c.metadata.category.lower()
            ]
        
        if filters.court:
            filtered = [
                c for c in filtered
                if c.metadata.court and filters.court.lower() in c.metadata.court.lower()
            ]
        
        if filters.case_type:
            filtered = [
                c for c in filtered
                if c.metadata.case_type and filters.case_type.lower() in c.metadata.case_type.lower()
            ]
        
        return filtered
    
    def _calculate_mock_score(self, chunk: Any, query_lower: str) -> float:
        """Calculate mock relevance score based on keyword matching."""
        score = 0.0
        
        # Check in raw content
        content_lower = chunk.raw_content.lower()
        text_for_embedding_lower = chunk.text_for_embedding.lower()
        
        # Exact phrase match gets highest score
        if query_lower in content_lower:
            score += 0.9
        elif query_lower in text_for_embedding_lower:
            score += 0.8
        else:
            # Check individual words
            query_words = query_lower.split()
            matches = sum(1 for word in query_words if word in content_lower)
            if matches > 0:
                score += 0.3 + (matches / len(query_words)) * 0.5
        
        # Boost for section ID match
        if chunk.metadata.section_id:
            section_id_lower = chunk.metadata.section_id.lower()
            if section_id_lower in query_lower:
                score += 0.2
        
        # Boost for act name match
        if chunk.metadata.act_name:
            act_name_lower = chunk.metadata.act_name.lower()
            query_words = query_lower.split()
            for word in query_words:
                if word in act_name_lower:
                    score += 0.1
                    break
        
        # Cap at 1.0
        return min(score, 1.0)


# Global retriever instance
mock_retriever = MockRetriever()
