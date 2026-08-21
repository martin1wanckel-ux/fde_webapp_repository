FROM python:3.11-slim
# is this the actual path that I am interested in?
WORKDIR /app 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn" , "src.api.main:app" , "--host", "0.0.0.0" , "--port", "8000"]


