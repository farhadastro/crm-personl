from fastapi import APIRouter
from .endpoints import invoices, messages, projects, services, orders

api_router = APIRouter()
api_router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
