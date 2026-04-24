from app.core.service import BaseService
from app.core.decorators import exposed_action
from app.core.exceptions import ValidationError
from ..models.events import Event

class EventService(BaseService):
    model = Event

    @exposed_action("write", groups=["core_group_authenticated", "staff_comunidad"])
    def register_participant(self, event_id: int):
        """
        Inscribe a un usuario en un evento verificando el aforo.
        """
        session = self.app.repo.session
        event = session.query(Event).filter(Event.id == event_id).first()

        if not event:
            raise ValidationError("El evento no existe.")

        #validación de aforo 
        if event.current_participants >= event.capacity:
            return {
                "status": "error",
                "message": f"Capacidad agotada para {event.name}. Máximo: {event.capacity} personas."
            }

        #inscripción
        event.current_participants += 1
        
        #settings 
        
        welcome_msg = self.app.core.setting.get("community_events.welcome_message", "Inscripción completada")

        session.commit()

        return {
            "status": "success",
            "message": f"{welcome_msg} Nos vemos en {event.name}.",
            "data": {"current_participants": event.current_participants}
        }

    @exposed_action("write", groups=["staff_comunidad"])
    def reset_participants(self, event_id: int):
        """ Acción administrativa para vaciar el aforo """
        session = self.app.repo.session
        event = session.query(Event).filter(Event.id == event_id).first()
        
        if event:
            event.current_participants = 0
            session.commit()
            return {"status": "success", "message": "Contador de participantes reiniciado."}