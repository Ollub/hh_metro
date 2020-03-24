FROM python:3.6

ENV TZ Europe/Moscow

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

RUN chmod a+x ./run_app.sh

CMD ["./run_app.sh"]