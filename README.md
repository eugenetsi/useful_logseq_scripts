# useful_logseq_scripts

## Count all hours (count_all_hours.py)
This Python script is designed to parse a text file (usually markdown for logseq) containing hours logged for different projects and summarize the total hours spent on each project. It ignores any lines that are considered titles (lines containing #) and sums up the hours dedicated to each unique project. The total hours are then displayed in the console log.

### Features
- Regex Matching: Utilizes regular expressions to accurately parse and extract project names and the corresponding hours.
- Logging: Implements Python's built-in logging module to display the summarized hours and potential errors in a clear, standardized format.
- Error Handling: Checks for the correct number of command-line arguments to prevent unexpected behavior.

### Prerequisites
Before running this script, ensure you have Python installed on your system. The script is compatible with Python 3.

### Usage
1. Clone the repo
```bash
git clone https://github.com/eugenetsi/useful_logseq_scripts
cd useful_logseq_scripts
```
3. Input the filename you want to parse in the last line of the file -> `sum_project_hours('./path_to_file.md')`
4. Run the script
```bash
python3 count_all_hours.py 
```
The script will parse the file and use regular expressions to identify and sum the hours for each project. Results will be logged to the console.

5. Viewing Logs
   
The total hours for each project are logged in the console. If there are any issues with the file format or the command execution, error logs will be displayed.

### File Format
The script expects the timesheet file to be in a specific format:

>    Each line should contain the number of hours followed by the project name.
>    The hours and project name should be separated by a space.
>    Lines starting with # are considered titles/comments and are ignored.

```
# Week 1
5 ProjectAlpha
3 ProjectBeta
# Week 2
4 ProjectAlpha
2 ProjectGamma

```
### Contributing

Contributions are welcome. Please feel free to submit a pull request or create an issue if you have suggestions for improvement.

### License

MIT
