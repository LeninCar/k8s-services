FROM python:3.9-slim

WORKDIR /usr/src/app
COPY ./serviciolenin.py .
RUN pip install --no-cache-dir fastapi uvicorn
EXPOSE 8000
CMD ["uvicorn", "serviciolenin:app", "--host", "0.0.0.0", "--port", "8000"]