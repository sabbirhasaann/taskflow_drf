## Local Boilerplate Creation Workflow

Follow these steps locally to build and structure your custom Django boilerplate from scratch:

### 1. Create and Initialize the Virtual Environment
Create a virtual environment named .venv in your project root:

```bash
python -m venv .venv

```
### 2. Create Activation Helper Script (virtualenv.sh)
Create a quick shortcut script named virtualenv.sh to activate your environment easily:

```bash
#!/bin/bash
source .venv/bin/activate
```

### 3. Create Development Run Script (runserver.sh)
Create a utility script named runserver.sh to start the development server on 0.0.0.0:8000:

```bash
#!/bin/bash
python manage.py runserver 0.0.0.0:8000
```

### 4. Make Scripts Executable
Grant execution permissions to your helper shell scripts:

```bash
chmod +x -v virtualenv.sh runserver.sh
```

### 5. Create Dependencies File (requirements.txt)
Create a requirements.txt file and add your core packages:

```txt
django==6.0.1
python-dotenv==1.2.4
```

### 6. Activate Virtual Environment and Install Packages
Activate your virtual environment and install the requirements:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 7. Initialize the Django Project
Generate the base Django project structure, routing configurations into a folder named config:

```bash
django-admin startproject config .
```

### 8. Configure Version Control (.gitignore)
Create a .gitignore file in the root folder to exclude local files, caches, and secrets:

```txt
.venv/
.env
__pycache__/
db.sqlite3
....
```

### 9. Restructure Settings into a Modular Package
Organize your settings for multi-environment support (Development / Production):

1. Create a settings/ directory inside the config folder:

```bash
mkdir config/settings
```
2. Rename the default settings.py to base.py and move it into the settings/ folder:

```bash
mv config/settings.py config/settings/base.py
```

3. Turn the settings folder into a Python module by creating an empty __init__.py file inside it:

```bash
touch config/settings/__init__.py
```

4. Create environment-specific settings files (development.py and production.py) inside config/settings/:

```bash
touch config/settings/development.py config/settings/production.py
```

### 10. Update Environment Settings Imports

* In config/settings/development.py, import everything from base:

```bash
from .base import *
import os
DEBUG = os.getenv("DEBUG_DEV")
```

* In config/settings/production.py, import everything from base:

```bash
from .base import *
DEBUG = os.getenv("DEBUG")
```

### 11. Update Entry Points (manage.py, wsgi.py, asgi.py)
Modify manage.py, config/wsgi.py, and config/asgi.py to point to your new settings path (e.g., config.settings.development or config.settings.production):

* Example change in manage.py:

```bash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
```

### 12. Initialize Git and Make First Commit
Initialize your local git repository, stage all files, and make your initial commit:

```bash
git init
git add .
git commit -m "Initial boilerplate setup with modular settings and custom scripts"
```