# useful_logseq_scripts

- [Count all hours](#counthours)  
- [TODO 2 Calendar](#todocalendar)

## Count all hours (count_all_hours.py) <a name="counthours"/>
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

## TODO 2 Calendar (todo2cal.py) <a name="todocalendar"/>
This Python script parses a markdown file for tasks marked as TODO and automatically creates events in Google Calendar, stacking multiple events on the same day sequentially. It's designed to help you efficiently schedule your tasks by extracting dates, durations, and descriptions from a markdown-formatted TODO list and adding them to your Google Calendar.

### Features

- Markdown Parsing: Parses markdown files to find TODO tasks, extracting the date, duration, and description.
- Google Calendar Integration: Automatically creates events in your Google Calendar based on the TODOs.
- Sequential Scheduling: Stacks multiple events on the same day sequentially, starting from 8 AM.
- Logging: Utilizes Python's built-in logging to provide clear feedback and error messages.

### Prerequisites

- Python 3
- Access to the internet to authenticate with Google Calendar and to create events.
- `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib` libraries installed. Install them using pip if you haven't already:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Setup

1. Google Calendar API:
   - Go to the Google Developers Console.
   - Create a new project and enable the Google Calendar API.
   - Create credentials (OAuth 2.0 Client IDs) for your project.
   - Download the JSON file with your credentials and save it as credentials.json in the same directory as the script.

2. Script:
   - Place the todo2cal.py script in your desired directory.
   - Ensure that your markdown file is accessible to the script.

### Usage

1. Prepare Your Markdown File:
   - Format your TODOs in the markdown file as follows:
```lua
TODO [[Jan 27th, 2024]] dur: 1hr Description of the task
```
   - The script supports multiple TODOs and will schedule them sequentially if they are on the same day, starting at 8 AM local time.
   - Change your local time in loc:70/74, for example: `'timeZone': 'America/Los_Angeles'`.

2. Run the Script:
   - Use the command line to navigate to the directory containing the script and your markdown file.
   - Run the script with:
```bash
python3 todo2cal.py your_markdown_file.md
```
   - Follow the instructions for authenticating with Google on your first run.
   - The script will process the markdown file and add the events to your Google Calendar.

## Contributing

Contributions are welcome. Please feel free to submit a pull request or create an issue if you have suggestions for improvement.

## License

MIT
