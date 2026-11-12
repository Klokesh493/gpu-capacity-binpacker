# Gpu Capacity Binpacker architecture

Suggests GPU placement decisions for ML workloads while preserving headroom for online inference.

```mermaid
flowchart LR
    A["Cluster GPU inventory"]
    B["Subtract used GPUs and reserved inference GPUs"]
    C{"Batch request fits available GPUs?"}
    D["Recommend place"]
    E["Recommend partial queue or queue based on remaining capacity"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
