FROM yml-api
WORKDIR /opt/app
EXPOSE 8000
ADD . .
ENTRYPOINT ["python", "manage.py", "startserver", "a2"]

FROM yml-api-test as test
WORKDIR /opt/app
ADD . .
ENTRYPOINT ["python", "manage.py", "test"]
