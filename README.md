# GPU Capacity Binpacker

Suggests GPU placement decisions for ML workloads while preserving headroom for online inference.

Focus: GPU platform engineering, capacity planning, training and inference reliability.

Portfolio framing: Apple-scale client-style AI infrastructure project using synthetic data only.

## Run

```bash
python3 gpu_binpacker.py sample_capacity.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

Batch workloads compete with inference for GPUs. A placement recommendation must account for reserved serving headroom.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 gpu_binpacker.py sample_capacity.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
