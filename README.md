# Accident Detection System

This project is an accident detection system that uses a trained model to detect accidents from video footage and sends alerts.


Dataset drive link : https://drive.google.com/file/d/10L1okwD1UXaQtmLcrwFYfZAQMhHDm1or/view?usp=drivesdk
## Project Structure

```
├── __pycache__/
├── .env
├── accident-classification.ipynb
├── alert.py
├── camera.py
├── data/
│   ├── test/
│   │   ├── Accident/
│   │   ├── Non Accident/
│   │   └── Pictures - Shortcut.lnk
│   ├── train/
│   │   ├── Accident/
│   │   ├── Non Accident/
│   ├── val/
│   │   ├── Accident/
│   │   ├── Non Accident/
├── detection.py
├── model.json
```

## Setup

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your credentials:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   ALERT_PHONE_NUMBER=alert_phone_number
   ```

## Usage

Run the application:
```sh
python camera.py
```

