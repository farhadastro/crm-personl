# Seed script for ML CRM
from app.db.session import SessionLocal
from app.db.models import User, Client, Service, UserRole, Order

db = SessionLocal()

# Add Admin
admin = User(email="admin@consultancy.com", password_hash="hashed_pw", role=UserRole.ADMIN)
db.add(admin)

# Add ML Service
service = Service(name="Model Training Pipeline", description="Scalable PyTorch pipeline for LLM fine-tuning", base_price=5000.0)
db.add(service)

db.commit()
print("Database seeded.")
