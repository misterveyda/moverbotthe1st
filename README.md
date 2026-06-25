# moverbotthe1st
Robotics Company - This descr will be updated soon

## Backend

This repository now includes a Django backend in `backend/` with a PostgreSQL configuration.

### Local setup

```bash
cd /workspaces/moverbotthe1st
python3 -m pip install Django psycopg[binary] python-dotenv
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

### PostgreSQL configuration

The Django settings are currently configured for:

- `NAME`: `moverbot_db`
- `USER`: `moverbot_user`
- `PASSWORD`: `moverbot_password`
- `HOST`: `localhost`
- `PORT`: `5432`

Adjust `backend/settings.py` or use environment variables when deploying.

### Notes

- The Django app is in `core/`.
- The admin site is available at `/admin/`.
- The Angular frontend remains in `moverbot/`.
