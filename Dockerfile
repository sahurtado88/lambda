FROM public.ecr.aws/lambda/python:3.11

# Copiar requirements si los hay
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar código fuente
COPY src/ ${LAMBDA_TASK_ROOT}

# Comando por defecto
CMD ["lambda_function.lambda_handler"]