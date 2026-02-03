# FairlyUsed Marketplace Backend

A FastAPI backend for a simple marketplace. It provides authentication, user profiles, and listings APIs, backed by PostgreSQL via SQLModel, with Alembic migrations.

**Core Features**
1. Auth: signup, login (JWT), and `/me`.
2. Profiles: create and fetch the current user profile.
3. Listings: create, read, update, delete listings.
4. Health check: status endpoint.

**Tech Stack**
1. FastAPI + Uvicorn
2. SQLModel (SQLAlchemy) + PostgreSQL
3. Alembic migrations
4. JWT auth

**Project Structure (Backend)**
1. `app/main.py` — FastAPI app and middleware
2. `app/api/` — API routes and dependencies
3. `app/models/` — SQLModel database models
4. `app/schemas/` — Pydantic/SQLModel schemas
5. `app/services/` — domain services (auth/profile/listings)
6. `alembic/` — migrations

## Setup

**Prerequisites**
1. Python 3.12+
2. PostgreSQL

**Install Dependencies**
Choose one of the following:

```powershell
cd backend
uv sync
```

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

**Environment Variables**
Create a `.env` file at the repo root (same level as `backend/`). If you keep it elsewhere, update `env_file` in `app/core/config.py`.



**Database Migrations**
```powershell
cd backend
alembic upgrade head
```

## Run the API

```powershell
cd backend
uvicorn app.main:app --reload
```

The API will be served at `http://127.0.0.1:8000` with base path `/api/v1`.

## API Overview

**Auth**
1. `POST /api/v1/auth/signup` — Create a new user.
2. `POST /api/v1/auth/login` — Obtain access token.
3. `GET /api/v1/auth/me` — Current user (requires auth).

**Profiles**
1. `POST /api/v1/profiles/me` — Create profile (requires auth).
2. `GET /api/v1/profiles/me` — Get profile (requires auth).

**Listings**
1. `POST /api/v1/listings` — Create listing (requires auth + seller).
2. `GET /api/v1/listings` — List active listings.
3. `GET /api/v1/listings/{listing_id}` — Get a listing.
4. `PUT /api/v1/listings/{listing_id}` — Update listing (owner only).
5. `DELETE /api/v1/listings/{listing_id}` — Delete listing (owner only).

**Status**
1. `GET /api/v1/status` — Health check.

## Example Requests

**Signup**
```powershell
curl -X POST http://127.0.0.1:8000/api/v1/auth/signup `
  -H "Content-Type: application/json" `
  -d '{"email":"user@example.com","full_name":"User One","password":"strongpassword"}'
```

**Login**
```powershell
curl -X POST http://127.0.0.1:8000/api/v1/auth/login `
  -H "Content-Type: application/x-www-form-urlencoded" `
  -d "username=user@example.com&password=strongpassword"
```

**List Listings**
```powershell
curl http://127.0.0.1:8000/api/v1/listings
```

## Notes

1. The OpenAPI spec is available at `/api/v1/openapi.json`.
2. Swagger UI and ReDoc are available at `/docs` and `/redoc`.
