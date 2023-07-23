from flask import Flask, render_template, request, redirect
import datetime
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Load Google Calendar API credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar']
)
service = build('calendar', 'v3', credentials=credentials)

# Set up the calendar ID for appointments
calendar_id = 'petgroomingapptsystem@gmail.com'

central_timezone = pytz.timezone('America/Chicago')

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

    start_datetime = datetime.datetime.strptime(appointment_date + ' ' + appointment_time, '%Y-%m-%d %H:%M')
    end_datetime = start_datetime + datetime.timedelta(hours=1)

    start_datetime_central = central_timezone.localize(start_datetime)
    end_datetime_central = central_timezone.localize(end_datetime)

    event = {
        'summary': f'Pet Grooming: {pet_name}',
        'description': f'Customer Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}',
        'start': {
            'dateTime': start_datetime_central.isoformat(),
            'timeZone': 'America/Chicago',
        },
        'end': {
            'dateTime': end_datetime_central.isoformat(),
            'timeZone': 'America/Chicago',
        },
    }

    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()

    # Pass appointment details to the success.html template
    appointment_time_display = start_datetime_central.strftime('%I:%M %p')

    return render_template('success.html', pet_name=pet_name, appointment_date=appointment_date, appointment_time=appointment_time_display)


if __name__ == '__main__':
    app.run(debug=True)
