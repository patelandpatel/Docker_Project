FROM python:3.8-alpine 
WORKDIR /count_visit
ENV FLASK_APP=app_2.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . /count_visit
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run"]
