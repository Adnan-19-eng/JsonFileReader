import json


def clean_phone(s):
    try:
        if s is None:
            return ""

        return "".join(char for char in str(s) if char.isdigit())

    except Exception:
        return ""


with open("JsonFileReader/records.json", "r") as file:
    records = json.load(file)


status_counts = {}

for record in records:
    record["phone"] = clean_phone(record["phone"])

    status = record["status"]
    status_counts[status] = status_counts.get(status, 0) + 1


print("Records:")
print(records)

print("\nStatus counts:")
print(status_counts)