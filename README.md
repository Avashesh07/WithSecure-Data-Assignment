
# Record Batching Library

  

## Overview

  

This Python library processes a list of records (strings) and splits them into batches according to specified constraints:

  

-  **Maximum record size**: 1 MB (1,048,576 bytes)

-  **Maximum batch size**: 5 MB (5,242,880 bytes)

-  **Maximum records per batch**: 500

  

Records exceeding the maximum record size are discarded. The order of records is preserved in the output batches.

  

## Installation

  

No installation required. Simply import the functions into your project.

## Usage  

```

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

```

## Functions
`process_records(records)`
Processes the input records by filtering and batching them.

 - **Parameters**: `records` (List of strings)
 - **Returns**: List of batches (each batch is a list of strings)

`filter_records(records)`
Filters out records larger than the maximum record_size.

`batch_records(records)`
Splits records into batches based on size and count constraints.

## Logging
The library uses the `logging` module to report discarded records due to size limits or invalid types.

## Testing
Unit tests are provided in `test_record_batching.py`. Run the tests using:
```
python -m unittest test_record_batching.py
```
