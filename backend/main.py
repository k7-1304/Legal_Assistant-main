"""Legal Assistant API - FastAPI Application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

from config import settings
from routes import (
    health_router,
    search_router,
    autocomplete_router,
    chat_router,
    viability_router,
    arguments_router,
    clauses_router,
)
from middleware import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Legal Assistant API",
    description="AI-powered legal research and petition drafting platform for Indian laws",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Register routers
app.include_router(health_router, tags=["Health"])
app.include_router(search_router, tags=["Search"])
app.include_router(autocomplete_router, tags=["Autocomplete"])
app.include_router(chat_router, tags=["Chat"])
app.include_router(viability_router, tags=["Viability Predictor"])
app.include_router(arguments_router, tags=["Argument Miner"])
app.include_router(clauses_router, tags=["Clause Search"])


@app.on_event("startup")
async def startup_event():
    """Startup event handler."""
    logger.info("Starting Legal Assistant API...")
    logger.info(f"Debug mode: {settings.debug}")
    logger.info(f"Using mock data: {settings.use_mock_data}")
    logger.info("API is ready to accept requests")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    logger.info("Shutting down Legal Assistant API...")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
