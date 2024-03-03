# Input and output file paths
input_file_path = "ssl_tls_scan_results.txt"
output_file_path = "scan_output.txt"

# Read input file
with open(input_file_path, "r") as input_file:
    input_lines = input_file.readlines()

# Initialize variables
current_ip_domain_info = ""
current_scan_result = ""
target_results = []

# Iterate through input lines
for line in input_lines:
    # Check for IP/Domain information
    if line.startswith(" SCAN RESULTS FOR"):
        current_ip_domain_info = line.strip()
    #elif line.startswith(" -----------------"):
        # Check if the current result matches the target pattern
        if '''SSL 2.0 Cipher Suites:
     Attempted to connect using 7 cipher suites; the server rejected all cipher suites.''' in current_scan_result and \
           '''SSL 3.0 Cipher Suites:
     Attempted to connect using 80 cipher suites; the server rejected all cipher suites.''' in current_scan_result and \
           '''TLS 1.0 Cipher Suites:
     Attempted to connect using 80 cipher suites; the server rejected all cipher suites.''' in current_scan_result and \
           '''TLS 1.1 Cipher Suites:
     Attempted to connect using 80 cipher suites; the server rejected all cipher suites.''' in current_scan_result:
            target_results.append((current_scan_result))
        current_scan_result = ""

    current_scan_result += line

# Write target results to output file
with open(output_file_path, "w") as output_file:
    for result in target_results:
        output_file.write(f"{result}\n\n")

print(f"Output written to {output_file_path}")
