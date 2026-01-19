"""Configuration management for Legal Assistant API."""
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field
import json


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    debug: bool = Field(default=True, alias="DEBUG")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    
    # CORS Configuration
    allowed_origins: str = Field(
        default='["http://localhost:5173","http://localhost:3000"]',
        alias="ALLOWED_ORIGINS"
    )
    
    # Mock Data Settings
    use_mock_data: bool = Field(default=True, alias="USE_MOCK_DATA")
    
    # Search Parameters
    vector_search_top_k: int = Field(default=20, alias="VECTOR_SEARCH_TOP_K")
    bm25_top_k: int = Field(default=20, alias="BM25_TOP_K")
    hybrid_vector_weight: float = Field(default=0.6, alias="HYBRID_VECTOR_WEIGHT")
    hybrid_bm25_weight: float = Field(default=0.4, alias="HYBRID_BM25_WEIGHT")
    rerank_top_k: int = Field(default=5, alias="RERANK_TOP_K")
    
    # LLM Parameters
    llm_temperature: float = Field(default=0.0, alias="LLM_TEMPERATURE")
    llm_max_tokens: int = Field(default=2000, alias="LLM_MAX_TOKENS")
    
    # Chatbot Memory
    chatbot_max_history: int = Field(default=10, alias="CHATBOT_MAX_HISTORY")
    
    @property
    def allowed_origins_list(self) -> List[str]:
        """Parse allowed origins from JSON string."""
        try:
            return json.loads(self.allowed_origins)
        except json.JSONDecodeError:
            return ["http://localhost:5173"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
