# Mudassir Latif — Portfolio (Django)

This repository contains a small Django-based portfolio website for Mudassir Latif. The site is a single-page portfolio with contact form that sends email using Django's SMTP mailing support.

This README describes the project layout, how to run it locally on Windows (PowerShell), required environment variables, and a few deployment notes.

## Project snapshot

- Framework: Django 5.2.4
- Python: developed with CPython 3.12 (recommended)
- Database: SQLite (file: `db.sqlite3`)

## What I read in the project

- `manage.py` — standard Django management wrapper
- `portfolio/settings.py` — project settings (SMTP email configuration, static files, CSRF trusted origins)
- `portfolio/urls.py` — routes: `''` (home) and `contact/` (contact form POST)
- `portfolio/views.py` — two views: `simple_view` (renders `layout.html`) and `contact` (handles POST, sends email)
- `portfolio/asgi.py`, `portfolio/wsgi.py` — server entrypoints
- `static/layout.html` — single template used for the whole site; loads static assets in `static/assets/...`
- `static/assets/css/style.css`, `static/assets/js/main.js` — styling and client JS
- `portfolio/requirements.txt` — pinned Python packages used by the project

## File structure (important files)

```
portfolio/
  db.sqlite3
  manage.py
  portfolio/            # Django project package
    settings.py
    urls.py
    views.py
    wsgi.py
    asgi.py
    requirements.txt    # existing inner requirements
  static/               # templates + static assets
    layout.html
    assets/
      css/
      js/
      img/
```

## Setup — Local development (Windows PowerShell)

1. Install Python 3.11+ (3.12 recommended). Confirm with:

```powershell
python --version
```

2. Create and activate a virtual environment (PowerShell):

```powershell
# create
python -m venv venv

# Activate in PowerShell
.\venv\Scripts\Activate.ps1

# If PowerShell execution policy blocks activation, you can run this once as Administrator:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Install dependencies (the root `requirements.txt` was added to this repository):

```powershell
pip install -r requirements.txt
```

4. Apply migrations and run the development server:

```powershell
python manage.py migrate
python manage.py runserver
```

5. Open http://127.0.0.1:8000/ in your browser.

## Environment variables

- `Email_HOST_PASSWORD` — the SMTP account password used by the project. The project reads this from `os.environ.get('Email_HOST_PASSWORD')` in `portfolio/settings.py`. Set it in your shell before running the server, for example in PowerShell:

```powershell
$env:Email_HOST_PASSWORD = 'your-smtp-password-here'
```

Notes about email: settings currently use `smtp.gmail.com:587` with TLS and `DEFAULT_FROM_EMAIL` = `latif4505017@cloud.neduet.edu.pk`. If you use Gmail, you may need to create an App Password or enable the account appropriately.

## Contact form

- The contact form in `layout.html` posts to the `contact` view and triggers `send_mail(...)` using the `DEFAULT_FROM_EMAIL` and `CONTACT_RECEIVER_EMAIL` configured in `settings.py`.
- On successful submission the view re-renders `layout.html` with `{'success': True}`.

## Notes on configuration and security

- `DEBUG` is set to `True` in `settings.py`. Turn this off for production.
- `SECRET_KEY` is present in `settings.py` — for a real deployment, move it into an environment variable and never commit it to version control.
- `CSRF_TRUSTED_ORIGINS` includes a Railway app origin (present in `settings.py`) — add any production hostnames you use.
- Static files are expected under the `static/` folder (the project uses `STATICFILES_DIRS = [BASE_DIR / 'static']`).

## Deployment tips

- For simple deployments you can use an app host (Railway, Heroku alternatives, etc.) but make sure to:
  - Move sensitive settings (SECRET_KEY, EMAIL password) into environment variables.
  - Serve static files through a static host (or configure whitenoise / webserver)
  - Set `DEBUG = False` in production

## Troubleshooting

- If contact emails fail, check the `Email_HOST_PASSWORD` env var and SMTP settings and review server logs for SMTP errors.
- If static files are not found in production, ensure collectstatic or web server static file config is in place.

## Licensing & attribution

This repository appears to be a personal portfolio site. Check with the project owner for license preferences if you plan to reuse or redistribute code or assets.

---

If you'd like, I can also:
- Add a minimal `.env.example` showing which environment variables to set.
- Create a GitHub Actions workflow to run tests/lint on push.

Tell me which of those you'd like next.
