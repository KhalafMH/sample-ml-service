FROM tensorflow/tensorflow:latest-py3

WORKDIR /app
ADD requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt
ADD src /app/
RUN mkdir model && python train.py
ENTRYPOINT python /app/service.py
