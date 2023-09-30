#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
import signal


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0


def print_metrics():
    """
    Print the computed metrics.
    """
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def process_line(line):
    """
    Process a single line of input and update metrics.
    """
    global total_file_size, line_count
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[8])
            file_size = int(parts[10])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        line_count += 1
    except ValueError:
        pass


# Register a signal handler for Ctrl+C
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass

# Print final metrics
print_metrics()
