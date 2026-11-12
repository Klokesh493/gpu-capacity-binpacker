# Gpu Capacity Binpacker architecture

Suggests GPU placement decisions for ML workloads while preserving headroom for online inference.

```mermaid
flowchart LR
    N0["sample_capacity.csv"]
    N1["gpu_binpacker.py"]
    N2["available for batch / placement decision / decisions"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
