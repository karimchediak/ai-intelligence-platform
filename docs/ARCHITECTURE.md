# AegisAI Architecture

AegisAI is organized as a layered autonomous-intelligence system.

1. **API** receives structured tasks.
2. **Orchestrator** coordinates planning and execution.
3. **Planner** converts natural-language objectives into tool-aware steps.
4. **Executor** runs steps and records memory events.
5. **Retrieval/agents** provide evidence.
6. **ML** provides forecasts and anomaly detection.
7. **Evaluation** measures quality.
8. **Frontend** exposes the system to a user.

The design deliberately separates orchestration from individual capabilities so new agents and tools can be added without rewriting the application.