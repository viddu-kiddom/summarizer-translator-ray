# File name: Dockerfile
FROM rayproject/ray:latest

# Set the working dir for the container to /serve_app
WORKDIR /serve_app
COPY requirements.txt /serve_app/requirements.txt
COPY main.py /serve_app/main.py
COPY summarizer.py /serve_app/summarizer.py
COPY translator.py /serve_app/translator.py

RUN pip install -r requirements.txt