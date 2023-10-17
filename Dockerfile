FROM python:3.11
WORKDIR /code
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 8000