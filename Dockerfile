FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]