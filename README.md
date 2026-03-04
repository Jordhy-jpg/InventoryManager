# Inventory Manager

A modern, Glassmorphism-themed Django web application for managing inventory, specifically designed to handle Brands and Products. Built with Django 6.0 and Python 3.13+, and designed for deployment on Vercel with a PostgreSQL database.

## Features

- **Brand Management**: Create, Read, Update, and Delete (CRUD) operations for product brands.
- **Product Management**: Full CRUD operations for products, including SKU, price, quantity, and brand association.
- **Modern UI**: Clean and responsive Glassmorphism design system.
- **PostgreSQL Ready**: Configured to work out-of-the-box with PostgreSQL.
- **Vercel Deployment**: Pre-configured `vercel.json` and `build.sh` for seamless deployment to Vercel.

## Technologies Used

- **Backend**: Django 6.0, Python 3.13+
- **Database**: PostgreSQL (psycopg 3)
- **Frontend**: HTML5, CSS3 (Glassmorphism), Django Templates
- **Package Management**: `uv`
- **Static Files**: WhiteNoise
- **Deployment**: Vercel

## Prerequisites

- [Python 3.13+](https://www.python.org/downloads/)
- [`uv`](https://github.com/astral-sh/uv) (Extremely fast Python package installer and resolver)
- PostgreSQL database (local or cloud)

## Local Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up the environment:**

   Create a `.env` file in the `InventoryManager/Main` directory (or wherever your `manage.py` is executed from) and add the following variables:

   ```env
   SECRETKEY=your-super-secret-key-here
   DATABASE_URL=postgres://username:password@host:port/database_name
   DEBUG=True
   ```
   *Note: Ensure `DEBUG` is set to `False` in a production environment.*

3. **Install dependencies using `uv`:**

   ```bash
   uv pip install -r InventoryManager/requirements.txt
   ```
   *Alternatively, if you are using `uv` as your project manager, you can use `uv sync` if applicable.*

4. **Navigate to the project directory:**

   ```bash
   cd InventoryManager
   ```

5. **Run database migrations:**

   ```bash
   uv run python manage.py migrate
   ```

6. **Collect static files (Optional for local, required for production):**

   ```bash
   uv run python manage.py collectstatic --noinput --clear
   ```

7. **Run the development server:**

   ```bash
   uv run python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Deployment to Vercel

This project is configured for deployment on Vercel.

1. Install the Vercel CLI or connect your GitHub repository to Vercel.
2. Ensure you set the environment variables (`SECRETKEY`, `DATABASE_URL`) in your Vercel project settings.
3. The `vercel.json` and `build.sh` files handle the build process, including dependency installation, static file collection, and database migrations.

## Project Structure

- `InventoryManager/Main/`: The core Django project settings.
- `InventoryManager/InvApp/`: The main application handling Brands, Products, and views.
- `InventoryManager/InvApp/static/`: Contains the Glassmorphism CSS (`style.css`).
- `InventoryManager/InvApp/templates/`: HTML templates for the UI.
