Módulo que permite la gestión de listas de tareas con lógica de negocio personalizada y configuración dinámica.

Estructura:

- `models.py`: Definición de tablas `PracticeChecklist` y `PracticeChecklistItem`.
- `services/checklist.py`: Lógica de negocio y acciones expuestas (`close`).
- `views/views.yml`: Definición de la interfaz de usuario (Table y Form views).
- `data/settings.yml`: Parámetro `enforce_all_items_done`.
- `i18n/`: Traducciones del módulo.
