# group_1
Group 1 project

# Pet Grooming Appointment System

The Pet Grooming Appointment System is a web application built using Flask and Google Calendar API that allows pet owners to schedule grooming appointments for their pets.

## Getting Started

To run the Pet Grooming Appointment System on your local machine, follow the instructions below:

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/CSU-CPSC4205-2023-Summer/group_1

2. Install the required Python packages:

```bash
pip install flask
pip install google-api-python-client
pip install pytz

3. Set up Google Calendar API:

Go to the Google Developers Console.
Create a new project and enable the Google Calendar API.
Create credentials for the API and download the credentials.json file.
Place the credentials.json file in the root directory of the project.

Usage:

Run the Flask app:

'''bash
flask run

Open your web browser and navigate to http://localhost:5000/ to access the home page.

On the home page, click on 'Schedule' on navigation bar. This will take you to the index.html page. You can enter your personal information and schedule a grooming appointment for your pet.

After scheduling an appointment, you will be redirected to the success page, which will display the details of the appointment.

Customization:

You can modify the about.html, index.html and success.html files in the templates folder to change the appearance of the web pages.

To update the Google Calendar ID, open app.py and find the calendar_id variable. Replace the value with your target Google Calendar ID.

Credits:

The Pet Grooming Appointment System has been developed by Samuel Renner, Kayla Smith, and Gerri Barnes.


