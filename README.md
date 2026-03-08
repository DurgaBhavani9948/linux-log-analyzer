\# Linux Log Analyzer



A Python-based CLI tool to analyze Linux system logs (`syslog`) for \*\*errors\*\* and \*\*warnings\*\*, generate a CSV report, and summarize critical issues. This project demonstrates practical skills in Python scripting, log monitoring, and software development — ideal for system engineering or Red Hat internship roles.



---



\## Features



\- Detects \*\*ERROR\*\* and \*\*WARNING\*\* messages in Linux logs.

\- Generates a \*\*`report.csv`\*\* containing all error and warning entries.

\- Prints a summary of total errors and warnings.

\- Highlights the \*\*top 3 repeated log messages\*\* to identify recurring issues.

\- Works with \*\*any log file\*\* specified via command-line argument.

\- Compatible with \*\*PowerShell, Command Prompt, and Linux terminals\*\*.

\- Gracefully handles missing log files.



---



\## Project Structure





linux-log-analyzer/

│

├─ log\_analyzer.py # Main Python script

├─ sample\_syslog.log # Example log file

├─ report.csv # Generated report after analysis

└─ README.md # Project documentation





---



\## Installation



1\. \*\*Clone the repository:\*\*



```bash

git clone https://github.com/DurgaBhavani9948/linux-log-analyzer.git

cd linux-log-analyzer



Ensure Python 3.8+ is installed.



Place your log file in the project folder (default: sample\\\_syslog.log).



Usage



Analyze default log file (sample\\\_syslog.log):



python log\\\_analyzer.py



Analyze a custom log file:



python log\\\_analyzer.py -f my\\\_syslog.log



Sample console output:



=== Log Analysis Summary ===

Total Errors: 2

Total Warnings: 2



Top 3 repeated logs:

1x | Jul 10 10:10:12 server1 sshd: ERROR Failed login attempt

1x | Jul 10 10:10:11 server1 kernel: WARNING Disk space low

1x | Jul 10 10:10:14 server1 kernel: WARNING CPU temperature high



Generated report.csv:



Type	Log Message

ERROR	Jul 10 10:10:12 server1 sshd: ERROR Failed login attempt

ERROR	Jul 10 10:10:15 server1 sshd: ERROR Authentication failure

WARNING	Jul 10 10:10:11 server1 kernel: WARNING Disk space low

WARNING	Jul 10 10:10:14 server1 kernel: WARNING CPU temperature high

Skills Demonstrated



Python programming and file handling



Command-line tools with argument parsing (argparse)



CSV report generation for structured data



Log monitoring and analysis



Error/warning detection and data summarization



Git version control and GitHub repository management



This project highlights practical experience in software development, system monitoring, and data analysis.


