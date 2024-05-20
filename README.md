# Leaderboard Web Application

This is a web application that displays a dynamic leaderboard, allowing users to switch between different time periods (e.g., "This Month" and "All Time"). The application is built using Aiohttp for the server-side handling and Jinja2 for templating. HTMX is used for dynamic content loading without full page reloads.

## Features

-   Display leaderboard entries with ranks, avatars, names, and points.
-   Switch between different leaderboard views using tabs.
-   Dynamic content loading using HTMX.

## Technologies Used

-   [Aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP client/server framework
-   [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) - Templating engine for Python
-   [HTMX](https://htmx.org/) - Library for dynamic HTML content updates

## Setup Instructions

### Prerequisites

-   Python 3.7 or higher
-   pip (Python package installer)

### Installation

1. **Clone the repository**

2. **Create a virtual environment**

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```bash
        .venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

4. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set .env variables**
    - Set the enviornment variables in `.env.example` to the correct strings and remove `.example` from file name

### Running the Application

1. **Start the server**

    ```bash
    python app.py
    ```

2. **Open your browser and navigate to**

    ```
    http://localhost:8080
    ```
