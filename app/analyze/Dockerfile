FROM python:2
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY analyze.py analyze.py
COPY attacks.py attacks.py
ENV PYTHONUNBUFFERED 1
CMD python analyze.py
