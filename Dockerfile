FROM python:slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["sh", "entrypoint.sh"]


