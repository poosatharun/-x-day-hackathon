from flask import Flask
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Twilio configuration
app.config['TWILIO_ACCOUNT_SID'] = os.environ.get('TWILIO_ACCOUNT_SID')
app.config['TWILIO_AUTH_TOKEN'] = os.environ.get('TWILIO_AUTH_TOKEN')
app.config['TWILIO_PHONE_NUMBER'] = os.environ.get('TWILIO_PHONE_NUMBER')
app.config['ALERT_PHONE_NUMBER'] = os.environ.get('ALERT_PHONE_NUMBER')

twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])

def send_alert(message):
    twilio_client.messages.create(
        body=message,
        from_=app.config['TWILIO_PHONE_NUMBER'],
        to=app.config['ALERT_PHONE_NUMBER']
    )
  # Import routes after app initialization