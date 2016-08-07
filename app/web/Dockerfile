FROM python:2
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . $INSTALL_PATH
ENV PYTHONUNBUFFERED 1
EXPOSE 5050
CMD python server.py
