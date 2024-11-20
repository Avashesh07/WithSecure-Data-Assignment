import sys
import logging
from typing import List

# Constraints
MAX_RECORD_SIZE = 1 * 1024 * 1024       # 1 MB in bytes
MAX_BATCH_SIZE = 5 * 1024 * 1024        # 5 MB in bytes
MAX_RECORDS_PER_BATCH = 500

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def filter_records(records: List[str]) -> List[str]:
    """
    Filters out records larger than MAX_RECORD_SIZE.

    Args:
        records (List[str]): The input list of records.

    Returns:
        List[str]: The list of records that are within the size limit.
    """

    filtered = []
    for idx, record in enumerate(records):
        if not isinstance(record, str):
            logger.warning(f"Record at index {idx} is not a string and will be discarded.")
            continue
        record_size = len(record.encode('utf-8'))
        if record_size <= MAX_RECORD_SIZE:
            filtered.append(record)
        else:
            logger.warning(f"Record at index {idx} exceeds size limit and will be discarded.")
    return filtered




def batch_records(records: List[str]) -> List[List[str]]:
    """
    Splits records into batches based on size and count constraints.

    Args:
        records (List[str]): The filtered list of records.

    Returns:
        List[List[str]]: The list of batches.
    """
    batches = []
    current_batch = []
    current_batch_size = 0

    for idx, record in enumerate(records):
        record_size = len(record.encode('utf-8'))

        # Check if adding the record would exceed batch size or record count limits
        if (current_batch_size + record_size > MAX_BATCH_SIZE) or (len(current_batch) >= MAX_RECORDS_PER_BATCH):
            # Finalize the current batch
            batches.append(current_batch)
            # Start a new batch
            current_batch = []
            current_batch_size = 0

        # Add the record to the current batch
        current_batch.append(record)
        current_batch_size += record_size

    # Add the last batch if it's not empty
    if current_batch:
        batches.append(current_batch)

    return batches



def process_records(records: List[str]) -> List[List[str]]:
    """
    Processes the input records by filtering and batching them.

    Args:
        records (List[str]): The input list of records.

    Returns:
        List[List[str]]: The list of batches ready for delivery.
    """
    if not isinstance(records, list):
        raise TypeError("Input records must be a list.")
    filtered_records = filter_records(records)
    batches = batch_records(filtered_records)
    return batches



