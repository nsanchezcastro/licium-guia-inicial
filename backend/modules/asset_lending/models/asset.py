from __future__ import annotations
from sqlalchemy import String, ForeignKey, Text
from app.core.base import Base
from app.core.fields import field

class Asset(Base):
    __tablename__ = "asset_lending_asset"
    __abstract__ = False
    __model__ = "asset"
    __service__ = "modules.asset_lending.services.asset.AssetService"

    name = field(
        String(100),
        required=True,
        public=True,
        info={"label": {"es": "Nombre del Recurso", "en": "Asset Name"}},
    )

    asset_code = field(
        String(50),
        unique=True,
        required=True,
        public=True,
        info={"label": {"es": "Código de Inventario", "en": "Asset Code"}},
    )

    status = field(
        String(20),
        required=True,
        default="available",
        public=True,
        info={
            "label": {"es": "Estado", "en": "Status"},
            "choices": [
                {"label": {"es": "Disponible", "en": "Available"}, "value": "available"},
                {"label": {"es": "Prestado", "en": "Loaned"}, "value": "loaned"},
                {"label": {"es": "Mantenimiento", "en": "Maintenance"}, "value": "maintenance"},
            ],
        },
    )

   
    location_id = field(
        ForeignKey("asset_lending_location.id"),
        required=True,
        public=True,
        info={"label": {"es": "Ubicación", "en": "Location"}},
    )

    
    responsible_user_id = field(
        ForeignKey("core_user.id"),
        required=False,
        public=True,
        info={"label": {"es": "Responsable", "en": "Responsible User"}},
    )

    notes = field(
        Text,
        public=True,
        info={"label": {"es": "Notas", "en": "Notes"}},
    )