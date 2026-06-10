import csv
import json
from pathlib import Path
from typing import Any, Dict, List

JSON_FILE = Path("data.json")
CSV_FILE = Path("data.csv")

sample_records: List[Dict[str, Any]] = [
    {"id": 1, "name": "Alice", "score": 95},
    {"id": 2, "name": "Ben", "score": 82},
    {"id": 3, "name": "Clara", "score": 88},
]


def load_json(filepath: Path) -> List[Dict[str, Any]]:
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return []
    with filepath.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filepath: Path, data: List[Dict[str, Any]]) -> None:
    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_csv(filepath: Path) -> List[Dict[str, Any]]:
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return []
    with filepath.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_csv(filepath: Path, data: List[Dict[str, Any]]) -> None:
    if not data:
        return
    fieldnames = list(data[0].keys())
    with filepath.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def add_record(data: List[Dict[str, Any]], record: Dict[str, Any]) -> List[Dict[str, Any]]:
    data.append(record)
    return data


def main() -> None:
    # Example usage:
    save_json(JSON_FILE, sample_records)
    save_csv(CSV_FILE, sample_records)

    json_data = load_json(JSON_FILE)
    print("JSON data:", json_data)
    print("JSON record count:", len(json_data))

    csv_data = load_csv(CSV_FILE)
    print("CSV data:", csv_data)
    print("CSV record count:", len(csv_data))

    new_record = {"id": 4, "name": "Dina", "score": 91}
    updated_data = add_record(json_data, new_record)
    save_json(JSON_FILE, updated_data)


if __name__ == "__main__":
    main()
