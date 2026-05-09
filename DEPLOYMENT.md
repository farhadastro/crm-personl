# Final Deployment Guide

### Final Production Folder Structure
- `backend/` (FastAPI + SQLAlchemy)
- `frontend/` (React + Vite)
- `docker-compose.yml`

### Render Deployment Settings (Backend)
- **Root Directory:** `backend`
- **Runtime:** `Docker`
- **Build Command:** (Dockerfile handles this)
- **Start Command:** (Dockerfile CMD handles this)
- **Environment Variables:**
  - `DATABASE_URL`: `postgres://user:pass@neon-host/dbname?sslmode=require`
  - `SECRET_KEY`: `your-random-secure-string`
  - `ALLOWED_ORIGINS`: `https://your-vercel-domain.com`

### Vercel Deployment Settings (Frontend)
- **Framework:** `Vite`
- **Root Directory:** `frontend`
- **Environment Variables:**
  - `VITE_API_URL`: `https://your-render-app.onrender.com/api/v1`

### Neon Setup
1. Create project.
2. Ensure SSL is enabled.
3. Copy connection string as `DATABASE_URL`.

### Deployment Checklist
- [ ] Neon DB accessible from Render.
- [ ] Frontend `.env.production` set correctly.
- [ ] Backend CORS origins updated.
- [ ] All Pydantic models validated.

### Deployment Order
1. Deploy Backend to Render.
2. Update Frontend `VITE_API_URL` to match Backend URL.
3. Deploy Frontend to Vercel.

### Common Errors
- CORS: Backend origin must match Vercel URL.
- DB: Connection strings require `sslmode=require`.

### Git/Render Commands
```bash
git add .
git commit -m "Production ready"
git push
```
