import csv
import sys


def available_for_batch(row):
    return int(row["gpus_total"]) - int(row["gpus_used"]) - int(row["reserved_inference_gpus"])


def placement_decision(row):
    available = available_for_batch(row)
    if available >= int(row["requested_gpus"]):
        return "place"
    if available > 0:
        return "queue_partial"
    return "queue"


def decisions(rows):
    return [{"cluster": row["cluster"], "available": available_for_batch(row), "decision": placement_decision(row)} for row in rows]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in decisions(csv.DictReader(handle)):
            print(f'{item["cluster"]}: {item["decision"]} available={item["available"]}')


if __name__ == "__main__":
    main(sys.argv[1])
