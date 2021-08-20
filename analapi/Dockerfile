FROM python:3.9

EXPOSE 4100

COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD [ "python", "run.py" ]