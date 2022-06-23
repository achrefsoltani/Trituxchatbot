import datetime
from datetime import timedelta
from datetime import datetime as datet
import pickle
import os.path


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'app/static/assets/credentialsDesktop.json'

def get_calendar_service():
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)

       # Save the credentials for the next run
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service

def list_calendars():
    service = get_calendar_service()
    # Call the Calendar API
    print('Getting list of calendars')
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])

    if not calendars:
        print('No calendars found.')
    for calendar in calendars:
        summary = calendar['summary']
        id = calendar['id']
        primary = "Primary" if calendar.get('primary') else ""
        print("%s\t%s\t%s" % (summary, id, primary))

def list_events(calendarId):
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting List o 10 events')
    events_result = service.events().list(
        calendarId=calendarId, timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def create_event():
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    d = datet.now().date()
    tomorrow = datet(d.year, d.month, d.day, 9) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": 'Calendar from Django',
                                               "description": 'This is a tutorial example of automating google calendar with Django',
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

def update_event(calendarId, eventId, email):

    # update the event to tomorrow 9 AM IST
    service = get_calendar_service()

    d = datet.now().date()
    tomorrow = datet(d.year, d.month, d.day, 9) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=2)).isoformat()

    event_result = service.events().update(
        calendarId=calendarId,
        eventId=eventId,
        body={
            "summary": 'Updated Automating calendar',
            "description": 'This is a tutorial example of automating google calendar with python, updated time.',
            "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
            "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
            "attendees": [{"email": email}]
        },
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])



