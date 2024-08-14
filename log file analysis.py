import re
from collections import defaultdict

ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
timestamp_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
error_pattern = re.compile(r'ERROR (\w+):')  # Updated to capture error type

error_count = defaultdict(int)

with open('application.log', 'r', encoding='utf-8') as log_file:
    lines = log_file.readlines()

with open('error_summary.txt', 'w') as summary_file:
    summary_file.write("IP Address\tTimestamp\tError Type\tError Message\n")
    summary_file.write("=" * 60 + "\n")

    for line in lines:
        ip_address = ip_pattern.search(line)
        timestamp = timestamp_pattern.search(line)
        error_message = error_pattern.search(line)

        if error_message:
            error_type = error_message.group(1)
            error_count[error_type] += 1

            summary_file.write(f"{ip_address.group() if ip_address else 'N/A'}\t"
                               f"{timestamp.group() if timestamp else 'N/A'}\t"
                               f"{error_type}\t"
                               f"{line.strip()}\n")

    summary_file.write("\n" + "=" * 60 + "\n")
    summary_file.write("Error Summary\n")
    summary_file.write("=" * 60 + "\n")

    for error, count in error_count.items():
        summary_file.write(f"{error}: {count} occurrences\n")

print("Summary has been saved to 'error_summary.txt'")
