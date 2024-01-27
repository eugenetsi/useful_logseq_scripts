import re
import os
import sys
import logging
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Dictionary to keep track of the last end time for each date
last_end_time_per_date = {}

def parse_date(date_str):
    # Remove the 'st', 'nd', 'rd', 'th' from the day part
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)

    # Now parse the date
    return datetime.datetime.strptime(date_str, '%b %d, %Y')

def authenticate_google_calendar():
    creds = None
    # The file token.json stores the user's access and refresh tokens and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_calendar_event(date_str, duration_str, description):
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    date_object = parse_date(date_str)  # Use the new parse_date function
        # Check if there's a last end time for the given date, otherwise start at 8 AM
    if date_str in last_end_time_per_date:
        start_time = last_end_time_per_date[date_str]
    else:
        start_time = datetime.datetime(date_object.year, date_object.month, date_object.day, 8, 0, 0)

    duration_hours = int(duration_str.replace('hr', ''))
    end_time = start_time + datetime.timedelta(hours=duration_hours)

    # Update the last end time for the date
    last_end_time_per_date[date_str] = end_time

    # Convert start and end times to RFC3339 format
    start_time_rfc3339 = start_time.isoformat()
    end_time_rfc3339 = end_time.isoformat()

    event = {
        'summary': description,
        'start': {
            'dateTime': start_time_rfc3339,
            'timeZone': 'MiddleEarth/Shire',  # TODO Change this to your time zone
        },
        'end': {
            'dateTime': end_time_rfc3339,
            'timeZone': 'MiddleEarth/Shire',  # TODO Change this to your time zone
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    logging.info(f"Event created: {event.get('htmlLink')}")

def parse_todo_items(file_path):
    date_pattern = re.compile(r'\[\[([\w\s,]+)\]\]')
    duration_pattern = re.compile(r'dur:\s*(\d+hr)')
    todo_pattern = re.compile(r'TODO')

    with open(file_path, 'r') as file:
        for line in file:
            if todo_pattern.search(line):
                date_match = date_pattern.search(line)
                duration_match = duration_pattern.search(line)
                description = line.split('hr')[-1].strip() if date_match and duration_match else None

                if date_match and duration_match and description:
                    date = date_match.group(1)
                    duration = duration_match.group(1)
                    create_calendar_event(date, duration, description)
                else:
                    logging.warning(f"Line with TODO doesn't match expected format: {line.strip()}")

if len(sys.argv) != 2:
    logging.error("Usage: python3 todo2cal.py markdownfile.md")
    sys.exit(1)

parse_todo_items(sys.argv[1])
