import csv

log_file = "sample_syslog.log"

error_count = 0
warning_count = 0

results = []

try:
    with open(log_file, "r") as file:
        for line in file:
            if "error" in line.lower():
                error_count += 1
                results.append(["ERROR", line.strip()])
            elif "warning" in line.lower():
                warning_count += 1
                results.append(["WARNING", line.strip()])

    with open("report.csv", "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["Type", "Log Message"])
        writer.writerows(results)

    print("Log Analysis Complete")
    print("Errors:", error_count)
    print("Warnings:", warning_count)

except FileNotFoundError:
    print("Log file not found. Please add 'sample_syslog.log' to the project folder.")