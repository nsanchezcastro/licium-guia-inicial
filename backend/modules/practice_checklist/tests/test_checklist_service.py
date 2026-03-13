import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from modules.practice_checklist.services.checklist import PracticeChecklistService

def test_close_checklist_with_pending_items():
    """Prueba que no se pueda cerrar si hay items pendientes."""
    mock_db = MagicMock()
    service = PracticeChecklistService(mock_db)
    service.repo = MagicMock()
    service.repo.get_setting.return_value = True
    
    mock_checklist = MagicMock()
    mock_checklist.id = 1
    
    # Ítem pendiente
    mock_item_pendiente = MagicMock()
    mock_item_pendiente.is_done = False
    mock_checklist.items = [mock_item_pendiente]
    
    service.repo.session.get.return_value = mock_checklist

    with pytest.raises(HTTPException) as excinfo:
        service.close(1)
    
    assert excinfo.value.status_code == 400
    assert "pendientes" in excinfo.value.detail.lower()

def test_close_checklist_successfully():
    """Prueba el cierre exitoso cuando todos los items están listos."""
    mock_db = MagicMock()
    service = PracticeChecklistService(mock_db)
    service.repo = MagicMock()
    service.repo.get_setting.return_value = True
    
    mock_checklist = MagicMock()
    mock_checklist.id = 2
    mock_checklist.status = "open"
    
    # Ítem terminado
    mock_item_finalizado = MagicMock()
    mock_item_finalizado.is_done = True
    mock_checklist.items = [mock_item_finalizado]
    
    service.repo.session.get.return_value = mock_checklist

    # Usamos patch para que el test no intente ejecutar el serializador real
    # Asegúrate de que la ruta 'modules.practice_checklist.services.checklist.serialize' sea correcta
    with patch('modules.practice_checklist.services.checklist.serialize', return_value={}):
        service.close(2)
    
    # VERIFICACIONES CLAVE:
    assert mock_checklist.status == "closed"  # ¿Cambió el estado?
    assert service.repo.session.commit.called # ¿Se guardó en DB?