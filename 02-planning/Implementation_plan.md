# Technical Design: Unified Legal Search & Indexing System
**Project:** AI Petition System Implementation
**Components:** MongoDB Atlas, Vector Search, BM25 (Full-Text Search)

## 1. Executive Summary
To provide the AI Petition system with the ability to reason across both statutory law and judicial precedents, we are implementing a **Unified Hybrid Index**. By merging Law/Act JSONs and Judgment JSONs into a single collection with a normalized schema, we enable the AI to retrieve legal context and case citations in a single low-latency query.

---

## 2. Data Normalization Schema
To index two different JSON structures in the same index, they must be mapped to a "Common Document Format."

### Schema Mapping Table
| Target Field | Law JSON Mapping | Judgment JSON Mapping |
| :--- | :--- | :--- |
| `doc_type` | `"statute"` | `"judgment"` |
| `content_body` | `raw_content` | `Text` |
| `title` | `metadata.act_name` | `Titles` |
| `embedding` | `embedding` | (Vector generated from Text) |
| `law_id` | `metadata.section_id` | Extracted from `Text` (e.g., "138") |
| `source_url` | N/A | `Doc_url` |

### Normalized JSON Structure
```json
{
  "_id": "unique_id",
  "doc_type": "statute | judgment",
  "content_body": "The raw text of the law or the judgment",
  "embedding": [0.012, -0.234, "..."],
  "metadata": {
    "title": "Short Title of the Document",
    "court": "Name of Court (if judgment)",
    "act_name": "Act Name (if statute)",
    "sections_referenced": ["138", "141"],
    "date_of_origin": "YYYY-MM-DD"
  }
}

3. Indexing Strategy in MongoDB
3.1 Vector Index (Semantic Search)
This allows the AI to find documents based on "Legal Intent" (e.g., searching for "vicarious liability" will find judgments even if that specific phrase isn't in the law).

Configuration:

Field: embedding

Dimensions: (Match your model, e.g., 1536 for OpenAI)

Similarity: cosine

3.2 BM25 Index (Full-Text Search)
This allows for precise keyword matching, such as searching for specific Section numbers or Case names like "Priti Bhojnagarwala".

Configuration:

Field: content_body

Analyzer: lucene.standard

4. Implementation Workflow
Step 1: Pre-processing & Chunking
Since Judgments can be extremely long (the provided sample is ~75KB), they must be split into smaller chunks (approx. 1000 tokens) before indexing. Laws are typically indexed section-by-section.

Step 2: Ingestion Pipeline
Load the raw JSON files.

Transform them into the Normalized Schema.

Generate Embeddings for the Judgment text (if not already present).

Upsert into the MongoDB collection legal_knowledge_base.

Step 3: Hybrid Retrieval Logic
When a user interacts with the petition system, the backend performs a hybrid search:

Vector Search: Finds documents with similar meanings.

Keyword Filter: Limits results to specific Acts if mentioned by the user.

Synthesis: Passes the top-ranked Law and top-ranked Judgment to the LLM as context.

5. Benefits of the Proposed Solution
Contextual Accuracy: The AI retrieves the Law and the Judgment explaining that Law simultaneously.

Improved Retrieval Performance: One database call instead of two separate lookups.

Easier Maintenance: One single pipeline to update when new laws or judgments are added.

Next Step Recommendation: Would you like me to provide a Python script that automates the transformation of your two specific JSON samples into this unified format?
