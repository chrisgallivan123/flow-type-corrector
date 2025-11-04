# Architecture

```mermaid
flowchart TD
    A[HTTP Client] -->|payload {title, description}| B[n8n Webhook]
    B --> C[Normalize / Clean]
    C --> D{Use Retrieval?}
    D -- yes --> E[Vector DB / Knowledge Base]
    E --> F[LLM Classification + Guardrails]
    D -- no --> F[LLM Classification + Guardrails]
    F --> G[Schema Enforcer]
    G --> H[Apply Corrections (Expand)]
    H --> I[Return {type, confidence, rationale}]
    H --> J[(Audit Store) ]
```
## Notes
- **Prod** JSON minimizes logs and disables debug‑only nodes.
- **Guardrails** ensure type ∈ {{Feature, Defect, Risk, Debt}}; unknowns routed to fallback.
- **Extensible**: swap models, adjust prompts, or enrich with retrieval snippets.
