from enum import Enum


class ResultFlag(Enum):
    PASS = 0
    EXECUTION_FAIL = -100
    # We can add more flags here for different types of failures
