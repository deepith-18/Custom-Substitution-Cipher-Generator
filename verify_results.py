import unittest
import sys

# Redirect stdout/stderr to files so we can debug if needed, 
# but mostly we want to run the tests and capture the result code.
# Since we can't capture stdout easily in this environment apparently,
# we will write a file 'status.txt' with the outcome.

from test_cipher import TestCipherTool

def run_tests_and_report():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCipherTool)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    with open("status.txt", "w") as f:
        if result.wasSuccessful():
            f.write("PASS")
        else:
            f.write("FAIL")
            f.write(f"\nErrors: {len(result.errors)}")
            f.write(f"\nFailures: {len(result.failures)}")

if __name__ == "__main__":
    try:
        run_tests_and_report()
    except Exception as e:
         with open("status.txt", "w") as f:
            f.write(f"CRASH: {e}")

