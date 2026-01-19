"""Package initialization for routes."""
from .health import router as health_router
from .search import router as search_router
from .autocomplete import router as autocomplete_router
from .chat import router as chat_router
from .viability import router as viability_router
from .arguments import router as arguments_router
from .clauses import router as clauses_router

__all__ = [
    "health_router",
    "search_router",
    "autocomplete_router",
    "chat_router",
    "viability_router",
    "arguments_router",
    "clauses_router",
]
