# Gpu Capacity Binpacker walkthrough

## Business problem

Batch workloads compete with inference for GPUs. A placement recommendation must account for reserved serving headroom.

## Reproduce the workflow

Run `python3 gpu_binpacker.py sample_capacity.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
us-east-train-a: place available=24
us-west-serve-b: queue available=-2
eu-train-c: place available=20
```

The sample supplies these fields. `cluster`, `gpus_total`, `gpus_used`, `requested_gpus`, `reserved_inference_gpus`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
