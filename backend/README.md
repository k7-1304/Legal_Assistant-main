# Legal Assistant Backend - Quick Start Guide

## Installation

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file** (optional - defaults will work):
   ```bash
   cp .env.example .env
   ```

## Running the Server

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing with Postman

1. **Import the collection**:
   - Open Postman
   - Click "Import"
   - Select `Legal_Assistant_API.postman_collection.json`

2. **Test the endpoints**:
   - Start with "Health Check"
   - Try "Search - Murder BNS"
   - Test "Chat - Murder Punishment"
   - Explore other endpoints

## API Endpoints

### 1. Health Check
```bash
GET /health
```

### 2. Search
```bash
POST /api/v1/search
{
  "query": "Section 103 BNS murder",
  "filters": {"doc_type": "statute"},
  "top_k": 5
}
```

### 3. Autocomplete
```bash
GET /api/v1/autocomplete?q=sec
```

### 4. Chat
```bash
POST /api/v1/chat
{
  "session_id": "test-session-001",
  "query": "What is the punishment for murder under BNS?"
}
```

### 5. Viability Predictor
```bash
POST /api/v1/viability
{
  "facts": "I am the wife of the business owner. I didn't sign the cheque...",
  "filters": {"court": "High Court"}
}
```

### 6. Argument Miner
```bash
POST /api/v1/arguments
{
  "scenario": "My client hit the victim once on the head..."
}
```

### 7. Clause Search
```bash
POST /api/v1/clauses
{
  "need": "Draft prayer clause for quashing FIR based on settlement"
}
```

## Mock Data

The API uses in-memory mock data including:
- 8 legal sections (BNS, IPC, NI Act, BNSS)
- 4 judgment cases
- Autocomplete suggestions

## Next Steps

After testing with mock data, you can:
1. Connect to MongoDB Atlas
2. Integrate real LLM (Groq)
3. Add embeddings (Mistral)
4. Implement reranking (Cohere)
5. Add authentication
6. Deploy to production
