FROM python:3.11

WORKDIR /home/runner/work/server/TechnicalSupportCenterProject

COPY . /home/runner/work/server/TechnicalSupportCenterProject

RUN make init

CMD ["sh", "-c", "make app-run-release"]
