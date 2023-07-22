from flask import Flask, render_template, request, redirect
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__, static_url_path='/static')

# Load Google Calendar API credentials for the service account
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar']
)
service = build('calendar', 'v3', credentials=credentials)

# Set up the calendar ID for appointments (Replace with the shared calendar ID)
calendar_id = 'petgroomingapptsystem@gmail.com'


@app.route('/')
def home():
    return render_template('about.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    pet_name = request.form.get('pet_name')
    appointment_date = request.form.get('appointment_date')
    appointment_time = request.form.get('appointment_time')

    # Extract the hour and minute from the selected time
    hour, minute = map(int, appointment_time.split(':'))

    # Create start and end datetime objects with Central US timezone
    start_datetime = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').replace(hour=hour, minute=minute)
    end_datetime = start_datetime + datetime.timedelta(hours=1)

    # Create event for appointment
    event = {
        'summary': f'Pet Grooming: {pet_name}',
        'description': f'Owner: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}',
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'America/Chicago'
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'America/Chicago'
        },
    }

    # Insert the event to the shared calendar using the service account credentials
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()

    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)