# Agentic Commerce

A hands-on project for building an **Agentic AI Commerce System** using real-world product, review, and multimodal data.

The project starts from raw Amazon product data collected through Apify and progressively builds:

- Product data ingestion
- Review ingestion
- Relational commerce database
- Product/review/media relationships
- Multimodal data pipeline
- Semantic representations
- Embeddings
- Vector search
- Agentic commerce

The project is intentionally **code-heavy with minimal non-repeating theory**.

---

# Project Architecture

The overall system will eventually look like:

```text
                    AMAZON / APIFY DATA
                           |
                           v
                    RAW DATA STORAGE
                           |
                           v
                  EXTRACTION / ETL
                           |
                           v
                 NORMALIZED DATA
                           |
                           v
                    POSTGRESQL
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       Products         Reviews           Media
          |                |                |
          |                |          +-----+-----+
          |                |          |           |
          |                |        Images      Video
          |                |          |           |
          |                |          v           v
          |                |       Vision      Video Model
          |                |       Model
          |                |          |
          +----------------+----------+
                           |
                           v
              STRUCTURED + TEXTUAL
                 REPRESENTATION
                           |
                           v
                   QUALITY FILTERING
                           |
                           v
                      EMBEDDINGS
                           |
                           v
                     VECTOR DB(pg vector)
                           |
                           v
                 HYBRID RETRIEVAL
                           |
                           v
                    OLLAMA + (TOOL/OUTPUT SELECTOR(ReAct based) -> DIFFERENT DB'S WITH DIFFERENT SURFACE (LIKE AMAZON, FLIPKART , MYNTRA))
                           |
                           v
                  AGENTIC COMMERCE
