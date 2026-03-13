Módulo que permite la gestión de listas de tareas con lógica de negocio personalizada y configuración dinámica.

Estructura:

- `models.py`: Definición de tablas `PracticeChecklist` y `PracticeChecklistItem`.
- `services/checklist.py`: Lógica de negocio y acciones expuestas (`close`).
- `views/views.yml`: Definición de la interfaz de usuario (Table y Form views).
- `data/settings.yml`: Parámetro `enforce_all_items_done`.
- `i18n/`: Traducciones del módulo.

Mejoras incrementales:

- Bulk Actions: Implementación de `set_done` masivo en la vista de lista para mejorar la eficiencia operativa.
- Settings: Sistema de ajustes dinámicos, incluyendo políticas de validación y cierre automático.
- i18n: Soporte para multi-idioma mediante archivos `es.yml` y `en.yml` para etiquetas y mensajes del sistema.
- Testing: Cobertura de lógica de negocio mediante tests unitarios de servicio para las acciones críticas (`close`, `set_done`) utilizando Mocks.


