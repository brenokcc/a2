FROM yml-api
WORKDIR /opt/app
EXPOSE 8000
ADD . .
ENTRYPOINT ["python", "manage.py", "startserver", "a2"]
