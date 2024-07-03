FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

COPY web /app/web
COPY allure-results /app/allure-results
COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && playwright install chrome