# Inventory Manager

Inventory Manager is a modern web application built with Django for managing products and brands. It features a sleek glassmorphism user interface and is designed to be easily deployable.

**Inspiration:** This project is explicitly inspired by the excellent Django tutorial series available on YouTube: [Django Tutorial Playlist](https://youtube.com/playlist?list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw&si=JI5cnNNnxc7Ock_i).

## Features

- **Product Management:** Add, edit, and track products, including their SKU, price, and stock quantity.
- **Brand Management:** Organize products by brand.
- **Glassmorphism UI:** A modern, clean, and responsive user interface using a glassmorphism design theme.
- **Production-Ready:** Configured for deployment on Vercel with PostgreSQL database integration and Whitenoise for efficient static file serving.

## Technology Stack

- **Backend:** Python >= 3.13, Django
- **Database:** PostgreSQL
- **Package Management:** `uv`
- **Static Files:** Whitenoise
- **Deployment:** Vercel

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

## Running Tests

To run the test suite, ensure you are in the `InventoryManager` directory and have the necessary environment variables set:

```bash
cd InventoryManager
SECRETKEY=test DATABASE_URL=postgres://test uv run python manage.py test
```

## Deployment

The application is configured for deployment on Vercel.
- It uses `vercel.json` and a `build.sh` script to handle the build process.
- Static files are served using Whitenoise (`whitenoise.storage.CompressedStaticFilesStorage`), configured directly from app directories to avoid `collectstatic` issues on Vercel.
- The production database should be a PostgreSQL instance, configured via the `DATABASE_URL` environment variable.
