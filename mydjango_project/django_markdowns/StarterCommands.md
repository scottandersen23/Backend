# Useful Terminal Commands

Here are the terminal commands to create and start a Django application on a Mac:

---

### 1. **Set Up a Virtual Environment**
Using a virtual environment isolates your project’s dependencies.

```bash
# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate
```

---

### 2. **Install Django**
Install Django using pip (the Python package manager).

```bash
pip install django
```

---

### 3. **Create a Django Project**
A Django **project** is the overall application configuration and settings.

```bash
django-admin startproject project_name
```

This creates a directory structure like:

```
project_name/
    manage.py
    project_name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

### 4. **Navigate to the Project Directory**
Move into the project’s root directory to run Django commands.

```bash
cd project_name
```

---

### 5. **Create a Django App**
A Django **app** is a modular component of the project that handles specific functionality.

```bash
python manage.py startapp app_name
```

This creates a directory structure like:

```
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

---

### 6. **Add the App to the Project**
Register the app in the `INSTALLED_APPS` list in `project_name/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'app_name',
]
```

---

### 7. **Run Database Migrations**
Set up the initial database structure.

```bash
python manage.py migrate
```

---

### 8. **Run the Development Server**
Start the Django development server to test the application.

```bash
python manage.py runserver
```

- The server will start on **http://127.0.0.1:8000** by default.
- To use a custom port, append it to the command (e.g., `python manage.py runserver 8080`).

---

### 9. **Access Your Application**
Open your browser and navigate to:

```
http://127.0.0.1:8000
```

You’ll see Django’s default welcome page if everything is set up correctly.

---

### Recap of Commands
```bash
# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install Django
pip install django

# Create a project
django-admin startproject project_name
cd project_name

# Create an app
python manage.py startapp app_name

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

These steps will get your Django project up and running on a Mac.