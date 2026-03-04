# Inventory Manager

This project is inspired by the excellent Django tutorial series available on YouTube: [Django Tutorial Playlist](https://youtube.com/playlist?list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw&si=JI5cnNNnxc7Ock_i).

## Features

- **Product Management:** Add, edit, and track products, including their SKU, price, and stock quantity.
- **Brand Management:** Organize products by brand.
- **Deployment:** Features a build.sh file to assist deployment.

## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Package Management:** `uv`
- **Static Files:** Whitenoise
- **Deployment:** Render

## Local Development Setup

To run this project locally, you will need `uv` installed.

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Environment Variables:**
   The project requires `SECRETKEY` and `DATABASE_URL` environment variables to be set for local execution.
   ```bash
   export SECRETKEY=your-local-secret-key
   export DATABASE_URL=postgres://user:password@localhost:5432/inventory_db
   ```
   *(For testing purposes, you can use dummy values like `SECRETKEY=test DATABASE_URL=postgres://test`)*

3. **Run Migrations:**
   Execute Django commands within the `InventoryManager` directory using `uv`.
   ```bash
   cd InventoryManager
   uv run python manage.py migrate
   ```

4. **Start the Development Server:**
   ```bash
   uv run python manage.py runserver
   ```
   The application will be available at `http://127.0.0.1:8000/`.