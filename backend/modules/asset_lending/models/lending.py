from __future__ import annotations
from sqlalchemy import Boolean, String
from app.core.base import Base
from app.core.fields import field
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.registry import register_model

@register_model
class Location(Base):
    __tablename__ = "asset_lending_location"
    __abstract__ = False
    _name = "asset_lending.location"

    name = field(
        String(180),
        required=True,
        public=True,
        editable=True,
        info={"label": {"es": "Nombre", "en": "Name"}},
    )
    code = field(
        String(20),
        required=True,
        public=True,
        editable=True,
        info={"label": {"es": "Código", "en": "Code"}},
    )
    is_active = field(
        Boolean,
        default=True,
        public=True,
        editable=True,
        info={"label": {"es": "Activo", "en": "Active"}},
    )

@register_model
class Asset(Base):
    __tablename__ = "asset_lending_asset"
    __abstract__ = False
    _name = "asset_lending.asset"  
    _description = "Asset Management" 
    __service__ = "modules.asset_lending.services.lending.AssetLoanService"

    name = field(String(180), required=True, public=True, info={"label": {"es": "Recurso"}})
    asset_code = field(String(50), required=True, public=True, info={"label": {"es": "Código de Activo"}})
    status = field(
        String(20), 
        default="available", 
        public=True,
        info={
            "label": {"es": "Estado"},
            "choices": [
                {"label": "Disponible", "value": "available"},
                {"label": "Prestado", "value": "loaned"},
                {"label": "Mantenimiento", "value": "maintenance"}
            ]
        }
    )
    location_id = field(Integer, ForeignKey("asset_lending_location.id"), public=True)
    location = relationship("Location", info={"public": True})
    notes = field(Text, public=True)
    loans = relationship("Loan", back_populates="asset", info={"public": True})

@register_model
class Loan(Base):
    __tablename__ = "asset_lending_loan"
    __abstract__ = False
    _name = "asset_lending.loan"

    asset_id = field(Integer, ForeignKey("asset_lending_asset.id"), required=True, public=True)
    asset = relationship("Asset", back_populates="loans", info={"public": True})
    
    # En Licium, los usuarios suelen ser 'core.user'
    borrower_user_id = field(UUID(as_uuid=True), ForeignKey("core_user.id"), required=True, public=True)
    
    status = field(
        String(20), 
        default="open", 
        public=True,
        info={
            "label": {"es": "Estado Préstamo"},
            "choices": [
                {"label": "Abierto", "value": "open"},
                {"label": "Devuelto", "value": "returned"},
                {"label": "Vencido", "value": "overdue"}
            ]
        }
    )
    checkout_at = field(DateTime(timezone=True), public=True)
    due_at = field(DateTime(timezone=True), public=True)
    returned_at = field(DateTime(timezone=True), public=True)
    checkout_note = field(Text, public=True)
    return_note = field(Text, public=True)