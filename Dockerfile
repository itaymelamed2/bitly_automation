FROM python:3.7
RUN pip install pytest
WORKDIR /bitly_automation
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
ENV BROWSER "chrome"
ENV ENV "production"
WORKDIR tests

CMD pytest --browser=$BROWSER --env=$ENV