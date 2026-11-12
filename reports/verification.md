# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 gpu_binpacker.py sample_capacity.csv
us-east-train-a: place available=24
us-west-serve-b: queue available=-2
eu-train-c: place available=20
test_places_when_capacity_exists (test_gpu_binpacker.GpuBinpackerTest) ... ok
test_preserves_inference_reservation (test_gpu_binpacker.GpuBinpackerTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
