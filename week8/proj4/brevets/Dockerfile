FROM python:3.12-slim
LABEL maintainer="Boyana Norris <norris@cs.uoregon.edu>"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flask_brevets.py"]
