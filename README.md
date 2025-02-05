# WeatherApp Backend

The **WeatherApp Backend** provides weather analytics, real-time data visualization, user authentication, and role-based access control. This backend is built with Django and integrated with a React + Redux frontend.

---
## Features

- **Weather Data Retrieval**: Fetches real-time weather information using a public weather API.
- **User Authentication**: Implements secure login with Google OAuth.
- **Role-Based Authorization**: Controls access to features based on user roles.
- **Interactive Data Visualizations**: Supports bar charts and line graphs for a better user experience.

---
## API Endpoints

- **GET /weather/<city>/**: Fetch weather information for the given city.
- **POST /auth/google/**: Google OAuth authentication for login.
- **GET /users/**: Retrieve a list of all users.
- **POST /users/block_unblock/<user_id>/**: Block or unblock a user by their ID.

---
## Tech Stack

- **Backend:** Django
- **Frontend:** React + Redux
- **Database:** PostgreSQL
- **Authentication:** Google OAuth
- **Styling:** Bootstrap

---
## Local Setup

### Prerequisites

Ensure you have the following installed before proceeding:

- **Python 3.x**
- **pip** (Python package manager)
- **Virtualenv** (Recommended for creating an isolated environment)

### Installation Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/rahulxqmoz/weatherapp_backend.git
cd weatherapp_backend
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Create a `.env` File

In the root directory, create a `.env` file with the following content:

```env
WEATHER_API_KEY=<your_weather_api_key>
GOOGLE_CLIENT_ID=<your_google_client_id>
```

Replace `<your_weather_api_key>` and `<your_google_client_id>` with actual API keys. **Do not push the `.env` file to GitHub.**

#### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will run at **http://localhost:8000** by default.

---
## Notes

- **Sensitive Information**: Never commit your `.env` file or any other files containing sensitive data (such as API keys) to a public repository. Each user should create their own `.env` file.
- **Requirements File**: Ensure all dependencies are listed in `requirements.txt`. You can generate it using:

  ```bash
  pip freeze > requirements.txt
  ```

---
## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

