from record_batching import process_records

# Sample input records
records = [
    "First record",
    "Second record",
    "Third record",
    # ... more records ...
]

# Process records
batches = process_records(records)

# Output batches
for i, batch in enumerate(batches):
    print(f"Batch {i + 1} ({len(batch)} records):")
    for record in batch:
        print(record)