## Django Boilerplate Setup Guide
Get up and running with your new Django project in seconds by following these steps:

### Requirements

* Python 3.x installed on your system
* Git installed on your system
---

### 1. Open Your Terminal
Navigate to the directory where you want to clone the project repository:

```bash
cd path/to/your/workspace
```

### 2. Clone the Repository
Clone the boilerplate using either SSH or HTTPS:

#### Using SSH:
```bash
git clone git@github.com:abualam/boilerplate-django.git
```

#### Using HTTPS:

```bash
git clone https://github.com/abualam/boilerplate-django.git
```

### 3 Navigate into the Project Directory
```bash
cd boilerplate-django
```

### 4. Detach from the Boilerplate Remote
Remove the original remote origin so you can link the project to your own repository:
```bash
git remote remove origin
```

### 5. Link to Your New Repository
Add your own remote repository URL as the new origin:

```bash
git remote add origin [your_remote_repo_url]
```

### 6. Push to Your Repository
Push the initial codebase to your newly created repository:

```bash
git push -u origin main
```

### 7. Open in Your IDE
Open the project folder in VS Code or your preferred code editor:

```bash
code .
```

### 8. Create & Activate a Virtual Environment
Isolate your Python dependencies by creating and activating a virtual environment:

On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows (Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate
```

On Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 9. Install Dependencies
Install all required packages listed in the project configuration:

```bash
pip install -r requirements.txt
```

### 10. Configure Environment Variables
Create a .env file in the root directory of your project and add the following configuration variables:

```txt
SECRET_KEY='Your_Secret_Key'
DJANGO_SETTINGS_MODULE=config.settings.development

DEBUG_DEV=False
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE_DEV='django.db.backends.sqlite3'
DB_NAME_DEV='db.sqlite3'

```

### 11. Generate and Append SECRET_KEY
Run the following command in your terminal inside the project root to generate a secure random secret key and append it directly to your .env file:

```bash
echo "SECRET_KEY='$(python -c 'import django.core.management.utils; print(django.core.management.utils.get_random_secret_key())')" >> .env
```

### 12. Run Migrations
Apply database migrations to setup standard Django tables (users, sessions, admin, etc.):

```bash
python manage.py migrate
```

### 13. Test the Server
Start the development server to verify everything is configured correctly:

```bash
python manage.py runserver
```
