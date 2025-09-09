import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    Lambda function simple que procesa eventos y retorna información
    """
    # Log del evento recibido
    print(f"Evento recibido: {json.dumps(event)}")

    # Obtener variables de entorno
    environment = os.environ.get('ENVIRONMENT', 'dev')
    version = os.environ.get('VERSION', '1.0.0')

    # Procesar el evento
    try:
        # Ejemplo: extraer datos del evento
        name = event.get('name', 'World')
        action = event.get('action', 'greet')
        
        # Lógica de negocio simple
        if action == 'greet':
            message = f"¡Hola {name}! Desde Lambda en {environment}"
        elif action == 'time':
            message = f"Hora actual: {datetime.now().isoformat()}"
        elif action == 'info':
            message = {
                "environment": environment,
                "version": version,
                "timestamp": datetime.now().isoformat(),
                "aws_region": os.environ.get('AWS_REGION', 'unknown')
            }
        else:
            message = f"Acción '{action}' no reconocida"
        
        # Respuesta exitosa
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'message': message,
                'environment': environment,
                'version': version,
                'timestamp': datetime.now().isoformat()
            })
        }
        
        print(f"Respuesta: {json.dumps(response)}")
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
        # Respuesta de error
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': False,
                'error': str(e),
                'environment': environment,
                'version': version,
                'timestamp': datetime.now().isoformat()
            })
        }
