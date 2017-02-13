FROM alpine:latest
MAINTAINER Michael Petersen "mpetason@gmail.com"
RUN apk add --update py2-pip
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
