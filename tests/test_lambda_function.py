import json\
import pytest\
import sys\
import os

# Agregar el directorio src al path

sys.path.insert(0, os.path.join(os.path.dirname(**file**), '..', 'src'))

from lambda_function import lambda_handler

class TestLambdaFunction:

```
def test_greet_action(self):
    """Test acción de saludo"""
    event = {
        "name": "Juan",
        "action": "greet"
    }
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert "¡Hola Juan!" in body['message']

def test_time_action(self):
    """Test acción de tiempo"""
    event = {
        "action": "time"
    }
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert "Hora actual:" in body['message']

def test_info_action(self):
    """Test acción de información"""
    event = {
        "action": "info"
    }
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert isinstance(body['message'], dict)
    assert 'environment' in body['message']
    assert 'version' in body['message']

def test_unknown_action(self):
    """Test acción desconocida"""
    event = {
        "action": "unknown"
    }
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert "no reconocida" in body['message']

def test_default_values(self):
    """Test valores por defecto"""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert "World" in body['message']
```