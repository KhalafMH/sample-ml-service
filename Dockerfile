FROM tensorflow/tensorflow:latest-py3

WORKDIR /app
ADD requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt
ADD src /app/
RUN python train.py

ENV PORT=8080

ENTRYPOINT python /app/service.py

HEALTHCHECK --interval=15s --timeout=3s CMD /app/health-check.sh
