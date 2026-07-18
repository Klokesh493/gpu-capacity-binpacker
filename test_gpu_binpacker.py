import unittest

from gpu_binpacker import available_for_batch, placement_decision


class GpuBinpackerTest(unittest.TestCase):
    def test_preserves_inference_reservation(self):
        row = {"gpus_total": "64", "gpus_used": "54", "reserved_inference_gpus": "12", "requested_gpus": "8"}
        self.assertEqual(available_for_batch(row), -2)
        self.assertEqual(placement_decision(row), "queue")

    def test_places_when_capacity_exists(self):
        row = {"gpus_total": "128", "gpus_used": "96", "reserved_inference_gpus": "8", "requested_gpus": "16"}
        self.assertEqual(placement_decision(row), "place")


if __name__ == "__main__":
    unittest.main()
