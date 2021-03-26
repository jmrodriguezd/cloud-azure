# Docker file for a slim Ubuntu-based Python3 image

FROM ubuntu:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

ENTRYPOINT ["python3"]

# Set the folder where uwsgi looks for the app
WORKDIR /perp

# Copy the app contents to the image
COPY . /perp

RUN make /perp

# If you have additional requirements beyond Flask (which is included in the
# base image), generate a requirements.txt file with pip freeze and uncomment
# the next three lines.
#COPY requirements.txt /
#RUN pip install --no-cache-dir -U pip
#RUN pip install --no-cache-dir -r /requirements.txt
#RUN pip install sqlalchemy
#RUN pip install psycopg2
#RUN pip install requests

CMD python /perp/dummy.py