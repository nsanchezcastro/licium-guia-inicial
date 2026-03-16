from __future__ import annotations
from sqlalchemy import String, Boolean
from app.core.base import Base
from app.core.fields import field

class AssetLocation(Base):
    __tablename__ = "asset_lending_location"
    __abstract__ = False
    __model__ = "location"
    __service__ = "modules.asset_lending.services.location.AssetLocationService"

    
    __selector_config__ = {
        "label_field": "name",
        "search_fields": ["name", "code"],
        "columns": [
            {"field": "name", "label": "Nombre"},
            {"field": "code", "label": "Código"},
            {"field": "is_active", "label": "Activo"},
        ],
    }

    name = field(
        String(100),
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
        required=True,
        public=True,
        editable=True,
        default=True,
        info={"label": {"es": "Activo", "en": "Active"}},
    )