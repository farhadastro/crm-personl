from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .session import Base

class UserRole(enum.Enum):
    ADMIN = "admin"
    CLIENT = "client"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CLIENT)
    created_at = Column(DateTime, default=func.now())

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_name = Column(String)
    contact_person = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime, default=func.now())

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    base_price = Column(Float)
    is_archived = Column(Integer, default=0) # 0 False, 1 True

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    tech_stack = Column(String)
    dataset_size = Column(String)
    deadline = Column(DateTime)
    model_type = Column(String)
    status = Column(String, default="pending") # pending, accepted, declined
    created_at = Column(DateTime, default=func.now())

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    name = Column(String)
    status = Column(String, default="backlog") # backlog, in_progress, review, done
    last_activity = Column(DateTime, default=func.now())

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Float)
    status = Column(String, default="draft") # draft, sent, paid
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=func.now())

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    attachment_metadata = Column(String, nullable=True) # JSON string
    created_at = Column(DateTime, default=func.now())
