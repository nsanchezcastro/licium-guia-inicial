from __future__ import annotations
import datetime as dt
from sqlalchemy import String, ForeignKey, DateTime, Text
from app.core.base import Base
from app.core.fields import field

class AssetLoan(Base):
    __tablename__ = "asset_lending_loan"
    __abstract__ = False
    __model__ = "loan"
    __service__ = "modules.asset_lending.services.loan.AssetLoanService"

    # Relaciones principales
    asset_id = field(
        ForeignKey("asset_lending_asset.id"),
        required=True,
        public=True,
        info={"label": {"es": "Recurso", "en": "Asset"}},
    )

    borrower_user_id = field(
        ForeignKey("core_user.id"),
        required=True,
        public=True,
        info={"label": {"es": "Prestatario", "en": "Borrower"}},
    )

    # Fechas del ciclo de vida del préstamo
    checkout_at = field(
        DateTime,
        required=True,
        default=lambda: dt.datetime.now(dt.timezone.utc),
        public=True,
        info={"label": {"es": "Fecha de Salida", "en": "Checkout At"}},
    )

    due_at = field(
        DateTime,
        required=True,
        public=True,
        info={"label": {"es": "Fecha de Devolución Prevista", "en": "Due At"}},
    )

    returned_at = field(
        DateTime,
        required=False,
        public=True,
        info={"label": {"es": "Fecha de Devolución Real", "en": "Returned At"}},
    )

    # Estado del préstamo
    status = field(
        String(20),
        required=True,
        default="open",
        public=True,
        info={
            "label": {"es": "Estado del Préstamo", "en": "Loan Status"},
            "choices": [
                {"label": {"es": "Abierto", "en": "Open"}, "value": "open"},
                {"label": {"es": "Devuelto", "en": "Returned"}, "value": "returned"},
                {"label": {"es": "Vencido", "en": "Overdue"}, "value": "overdue"},
            ],
        },
    )

    checkout_note = field(
        Text,
        public=True,
        info={"label": {"es": "Nota de Entrega", "en": "Checkout Note"}},
    )

    return_note = field(
        Text,
        public=True,
        info={"label": {"es": "Nota de Devolución", "en": "Return Note"}},
    )