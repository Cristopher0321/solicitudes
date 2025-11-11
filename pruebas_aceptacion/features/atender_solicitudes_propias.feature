Característica: Seguimiento de solicitudes propias
    Como usuario del sistema
    Quiero poder gestionar el seguimiento de mis solicitudes
    Para conocer el estado y progreso de mis documentales


    Escenario: Visualizar lista de mis solicitudes
        Dado que he iniciado sesión en el sistema con mi perfil de usuario
        Cuando navego a la sección "Mis Solicitudes"
        Entonces debo ver una lista con todas mis solicitudes creadas
        Y cada solicitud debe mostrar su estado actual entre en proceso, Cancelado o Completado


    Escenario: Ver detalles completos de una solicitud propia
        Dado que tengo una solicitud creada en el sistema
        Cuando selecciono una solicitud específica de mi lista
        Entonces puedo ver el estado de la solicitud


    Escenario: Marcar solicitud como completada
        Dado que tengo una solicitud en estado "En proceso"
        Cuando cambio el estado a "Completado"
        Entonces el sistema registra la fecha de completado
        Y la solicitud aparece como finalizada en mi lista
        Y ya no permite más cambios de estado


    Escenario: Cancelar solicitud propia
        Dado que tengo una solicitud en cualquier estado
        Cuando selecciono la opción "Cancelar solicitud"
        Entonces el sistema solicita confirmación de cancelación
        Y al confirmar, el estado cambia a "Cancelado"


    Escenario: Filtrar solicitudes por estado específico
        Dado que tengo solicitudes en diferentes estados
        Cuando aplico filtro por estado "En proceso"
        Entonces solo veo las solicitudes en estado "En proceso"
        Y el contador de resultados se actualiza según el filtro aplicado
        Y puedo remover el filtro para ver todas las solicitudes


