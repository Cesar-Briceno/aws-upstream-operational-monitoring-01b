AWS Upstream Operational Monitoring - 01B

- DESCRIPCIÓN DEL PROYECTO

Sistema serverless de monitoreo operacional upstream desarrollado en AWS para detectar anomalías en variables críticas de perforación y generar alertas automáticas en tiempo real.

El sistema analiza datos operacionales simulados y los compara contra umbrales configurables almacenados en Amazon DynamoDB. Cuando se detecta una desviación, se registra el evento y se envía una notificación automática mediante Amazon SNS.

Este proyecto fue desarrollado como ejercicio práctico dentro del alcance de la certificación AWS Certified Cloud Practitioner, con enfoque aplicado al sector energético.

- PROBLEMA QUE RESUELVE

En operaciones upstream, variables como:

    * ROP (Rate of Penetration)
    * Torque
    * Standpipe Pressure
    * Mud Density

pueden indicar fallas operacionales si salen de rangos normales.

En muchos entornos tradicionales, el monitoreo depende de revisión manual o sistemas poco integrados.

Este sistema permite:

Detectar anomalías automáticamente
Registrar eventos para trazabilidad
Generar alertas en tiempo real
Desacoplar procesamiento y notificación
Sentar base para monitoreo remoto escalable

- ARQUITECTURA DEL SISTEMA

 ![Arquitectura del Sistema](architecture/architecture-01b-upstream-operational-alerts.png.drawio (1)) 

Flujo del sistema:

EventBridge

    → AWS Lambda
    → DynamoDB (tabla de umbrales)
    → DynamoDB (tabla de eventos)
    → SNS
    → Notificación por correo electrónico

Arquitectura 100% serverless y orientada a eventos.

Principios aplicados:

Desacoplamiento de servicios
Escalabilidad automática
Bajo costo operativo
Configuración dinámica
Observabilidad mediante logs

- SERVICIOS DE AWS UTILIZADOS
 
AWS Lambda
Amazon DynamoDB
Amazon SNS
Amazon EventBridge
AWS IAM

- CARACTERISTICAS TÉCNICAS

Comparación dinámica contra umbrales almacenados en base de datos
Registro persistente de anomalías
Generación automática de eventos de alerta
Arquitectura basada en eventos (event-driven)
Diseño modular y extensible

- EJEMPLO DE EVENTO DETECTADO
  
Ejemplo real de alerta generada:

{
"event_id": "1fc48558-cfa6-4dee-8393-20b6739b9489",
"asset_id": "WELL-01",
"variable": "rop",
"measured_value": "35.66",
"severity": "HIGH",
"timestamp": 1771948749,
"max_threshold": "35"
}

- POSIBLES EVOLUCIONES

El sistema puede evolucionar hacia:

Integración con AWS IoT Core para datos en tiempo real
Streaming con Amazon Kinesis
Visualización ejecutiva con Amazon QuickSight
Integración con sistemas SCADA
Arquitectura multi-activo (múltiples pozos o rigs)
Integración con modelos predictivos basados en IA

- ESTRUCTURA DEL REPOSITORIO

/lambda → Función principal de detección de anomalías

/architecture → Diagrama de arquitectura

/evidence → Evidencias de ejecución

- CONTEXTO PROFESIONAL

Ingeniero de Petróleo con experiencia en operaciones upstream y gestión corporativa en entornos operacionales críticos.
Actualmente AWS Certified Cloud Practitioner, desarrollando un perfil híbrido que integra conocimiento profundo de procesos operativos reales con competencias en cloud computing e inteligencia artificial.
Interesado en la intersección entre energía y tecnología, con foco en:

    * Digitalización de procesos operativos
    * Monitoreo remoto escalable
    * Trazabilidad documental
    * Control de no conformidades
    *Automatización de reporting ejecutivo

Este proyecto forma parte del desarrollo práctico de soluciones cloud aplicadas a problemáticas reales del sector energético.

- USO DE HERRAMIENTAS DE ASISTENCIA

El diseño de la arquitectura y la estructuración del código fueron desarrollados como ejercicio práctico de arquitectura serverless en AWS.
Durante el proceso se utilizó asistencia de modelos de lenguaje (LLMs) como herramienta de apoyo para:

Validación de decisiones arquitectónicas
Optimización de estructura de código
Revisión de buenas prácticas
Aceleración del proceso de documentación
La implementación, comprensión y validación funcional del sistema fueron realizadas de forma consciente y orientadas al aprendizaje práctico de los servicios utilizados.

Este proyecto representa la transición estratégica hacia un perfil profesional híbrido energía + tecnología, combinando experiencia operacional real con arquitectura cloud moderna.
