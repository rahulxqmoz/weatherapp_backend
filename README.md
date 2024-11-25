# WeatherApp Backend

This is the backend for the WeatherApp, providing weather information and user authentication. The backend is deployed on [Heroku](https://weather-appxqmoz-b8bc0ab20be7.herokuapp.com) and is integrated with the frontend.

## API Base URL

The backend API is hosted on Heroku and can be accessed via the following URL:

- [https://weather-appxqmoz-b8bc0ab20be7.herokuapp.com](https://weather-appxqmoz-b8bc0ab20be7.herokuapp.com)

### API Endpoints

- **GET /weather/<city>/**: Fetch weather information for the given city.
- **POST /auth/google/**: Google OAuth authentication for login.
- **GET /users/**: Get a list of all users.
- **POST /users/block_unblock/<user_id>/**: Block or unblock a user by their ID.

## Local Setup

To run the backend locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended to create isolated environments)

### Installation Steps

1. **Clone the Repository**
   
   Clone the backend repository to your local machine:

   ```bash
   git clone https://github.com/rahulxqmoz/weatherapp_backend.git
   cd weatherapp_backend
Create a Virtual Environment

It's highly recommended to set up a virtual environment for Python dependencies:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

Install the required Python packages:


pip install -r requirements.txt
Create a .env File

In the root directory of the project, create a .env file with the following content:

WEATHER_API_KEY=<your_weather_api_key>
GOOGLE_CLIENT_ID=<your_google_client_id>
Replace <your_weather_api_key> and <your_google_client_id> with your actual API keys. Do not push the .env file to GitHub.

Run the Development Server
Once dependencies are installed and the .env file is set up, run the server:
python manage.py runserver
The application will run at http://localhost:8000 by default.

Notes
Sensitive Information: Never commit your .env file or any other files containing sensitive information (such as API keys or credentials) to a public repository. Instead, each user should create their own .env file.
Heroku Deployment: For deploying to Heroku, follow their documentation on setting environment variables using the Heroku Dashboard.

Requirements
requirements.txt: Make sure to include all your backend dependencies in this file for easy installation. You can generate it by running:
pip freeze > requirements.txt

License
This project is licensed under the MIT License - see the LICENSE file for details.
This README provides clear instructions for setting up the backend locally, explains how to configure environment variables, and ensures that sensitive information is not exposed.










