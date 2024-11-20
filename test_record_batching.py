import unittest
from record_batching import *

class TestBatchingLibrary(unittest.TestCase):
    def test_empty_input(self):
        records = []
        expected_output = []
        self.assertEqual(process_records(records), expected_output)

    def test_all_records_within_limits(self):
        records = ['a' * 100] * 10  # 10 records, 100 bytes each
        batches = process_records(records)
        self.assertEqual(len(batches), 1)
        self.assertEqual(len(batches[0]), 10)

    def test_record_exceeding_size_limit(self):
        records = ['a' * (MAX_RECORD_SIZE + 1)]
        batches = process_records(records)
        self.assertEqual(batches, [])

    def test_records_exceeding_batch_size(self):
        record = 'a' * (MAX_RECORD_SIZE)
        records = [record] * 6  # Each record is half the batch size
        batches = process_records(records)
        self.assertEqual(len(batches), 2)
        self.assertEqual(len(batches[0]), 5)
        self.assertEqual(len(batches[1]), 1)

    def test_max_records_per_batch(self):
        records = ['a'] * (MAX_RECORDS_PER_BATCH + 5)
        batches = process_records(records)
        self.assertEqual(len(batches), 2)
        self.assertEqual(len(batches[0]), MAX_RECORDS_PER_BATCH)
        self.assertEqual(len(batches[1]), 5)

    def test_non_string_record(self):
        records = ['valid_record', 12345, 'another_valid_record']
        batches = process_records(records)
        self.assertEqual(len(batches), 1)
        self.assertEqual(len(batches[0]), 2)
        self.assertIn('valid_record', batches[0])
        self.assertIn('another_valid_record', batches[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
