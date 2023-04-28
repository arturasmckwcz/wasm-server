FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ARG PORT_FS

EXPOSE ${PORT_FS:-3000}
CMD ["python", "server.py"]