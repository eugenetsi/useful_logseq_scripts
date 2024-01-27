import re
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sum_project_hours(file_path):
    project_hours = {}
    # Regex pattern to match "number" followed by "project name"
    project_pattern = re.compile(r'(\d+)\s+(\w+)', re.IGNORECASE)

    with open(file_path, 'r') as file:
        for line in file:
            match = project_pattern.search(line)
            if match and ('#' not in line): # match regex and ignore titles
                hours, project = int(match.group(1)), match.group(2)
                project_hours[project] = project_hours.get(project, 0) + hours

    for project, total_hours in project_hours.items():
        logging.info(f'Total hours for {project:15} -  {total_hours}')

# Check if the correct number of arguments are provided
if len(sys.argv) != 1:
    logging.error("Usage: python3 sum_hours.py")
    sys.exit(1)

sum_project_hours('./path_to_file.md')
