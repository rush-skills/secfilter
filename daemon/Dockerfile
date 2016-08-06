FROM python:2
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN mkdir cache
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY parser.py parser.py
VOLUME ["/app/cache/"]
ENV PYTHONUNBUFFERED 1
CMD python parser.py
