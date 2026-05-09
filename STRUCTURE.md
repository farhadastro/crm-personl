crm-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── auth.py
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── models.py
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── clients.py
│   │   │   │   │   ├── orders.py
│   │   │   │   │   ├── projects.py
│   │   │   │   │   ├── services.py
│   │   │   │   │   ├── invoices.py
│   │   │   │   │   └── messages.py
│   │   │   │   └── api.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── client.py
│   │   │   ├── order.py
│   │   │   └── project.py
│   │   └── services/
│   │       └── business_logic.py
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   ├── ui/
│   │   │   └── glass/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   │   ├── admin/
│   │   │   └── client/
│   │   ├── services/
│   │   ├── styles/
│   │   │   └── glassmorphism.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── vite.config.js
│   └── package.json
├── docker-compose.yml
└── README.md
