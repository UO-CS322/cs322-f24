#!/bin/bash

# Using bash in the autograder since part of the project is to create the PyTests

SCRIPT_DIR=$(dirname "$0")
PYCODE_DIR=$(dirname "$SCRIPT_DIR")

# Expected times were obtained with the calculator at https://rusa.jkassen.org/time/

# Brevet start time in ISO format
brevet_start_time="2024-01-01T00:00:00Z"
ret_code=0

# Calculate the control opening time via Python
run_test() {
    description=$1
    which=$2
    control_distance=$3
    brevet_distance=$4
    brevet_start_time=$5
    expected=$6
    actual_iso=$(cd ${PYCODE_DIR} && python3 -c "import arrow, acp_times; print(acp_times.${which}_time($control_distance, $brevet_distance, '$brevet_start_time'))" | tail -n 1)
    expected_iso=$(cd ${PYCODE_DIR} && python3 -c "import arrow; print(arrow.get('$expected').isoformat())")
    if [ "$expected_iso" == "$actual_iso" ]; then
        echo "$description: Passed"
    else
        echo "$description: Failed"
        echo "Expected: $expected_iso"
        echo "Actual:   $actual_iso"
	    ret_code=1
    fi
}

# Run the tests
# Start open/close times
run_test " OPEN time for 0 km in a 400 km brevet" "open"  0 400 $brevet_start_time "2024-01-01 00:00"
run_test "CLOSE time for 0 km in a 400 km brevet" "close" 0 400 $brevet_start_time "2024-01-01 01:00"

# Control open/close times
run_test " OPEN time for 250 km in a 400 km brevet" "open"  250 400 $brevet_start_time "2024-01-01 07:27"
run_test "CLOSE time for 250 km in a 400 km brevet" "close" 250 400 $brevet_start_time "2024-01-01 16:40"

run_test " OPEN time for 400 km in a 400 km brevet" "open"  400 400 $brevet_start_time "2024-01-01 12:08"
run_test "CLOSE time for 400 km in a 400 km brevet" "close" 400 400 $brevet_start_time "2024-01-02 03:00"

run_test " OPEN time for 883 km in a 1000 km brevet" "open"  883 1000 $brevet_start_time "2024-01-02 04:54"
run_test "CLOSE time for 883 km in a 1000 km brevet" "close" 883 1000 $brevet_start_time "2024-01-03 16:46"

# Finish open/close times
run_test " OPEN time for 1000 km in a 1000 km brevet" "open"  1000 1000 $brevet_start_time "2024-01-02 09:05"
run_test "CLOSE time for 1000 km in a 1000 km brevet" "close" 1000 1000 $brevet_start_time "2024-01-04 03:00"

exit $ret_code
