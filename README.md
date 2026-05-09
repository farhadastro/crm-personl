# ML Consultancy CRM 🚀

A purpose-built, self-hostable CRM designed specifically for ML and programming consultancies. Built with a premium, glassmorphic aesthetic to differentiate your client-facing interactions.

## 🌌 Design Philosophy
This is not a generic CRUD app. It is a portal for high-end technical consultancies:
- **Glassmorphic System:** A deep dark-themed UI (#0a0a1a) with refined blur effects.
- **ML-First Workflow:** Capture tech stacks, model architectures, and dataset sizes natively.
- **Role-Gated Portals:** Separate, secure experiences for Admins and Clients.

---

## 🛠 Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React (Vite)
- **Database:** PostgreSQL (Prod) / SQLite (Dev)
- **Deployment:** Containerized via Docker Compose

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd crm-system
   ```

2. **Configure your environment:**
   Create a `.env` file based on the example structure.

3. **Launch the platform:**
   ```bash
   docker-compose up -d --build
   ```

4. **Initialize Database:**
   ```bash
   docker-compose exec backend alembic upgrade head
   docker-compose exec backend python seed.py
   ```

---

## 🏗 Portal Overview

### Admin Portal
- **Dashboard:** KPI-driven analytics for your ML consultancy.
- **Pipeline:** Kanban board for tracking model development and deployment milestones.
- **Billing:** Integrated invoicing with status tracking.

### Client Portal
- **Service Catalog:** Browse professional ML services tailored for businesses.
- **Order Workflow:** Domain-specific form submission for model training and deployment.
- **Project Tracking:** Real-time visibility into project timelines and deliverables.

---

*Built with precision for solo/small ML consultancies.*
