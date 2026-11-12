# GPU Capacity Binpacker

Batch workloads compete with inference for GPUs. A placement recommendation must account for reserved serving headroom.

## What I built

I built a capacity advisor that subtracts used GPUs and an inference reserve before recommending whether a batch workload should be placed or queued. The output includes the computed headroom for each candidate cluster.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [gpu_binpacker.py](gpu_binpacker.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 gpu_binpacker.py sample_capacity.csv
```

US East can place the request with 24 GPUs available. US West queues because the reported usage and reserve exceed capacity. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 gpu_binpacker.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

This estimate uses GPU counts. Review accelerator type, fragmentation, topology, and scheduling quotas separately.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
