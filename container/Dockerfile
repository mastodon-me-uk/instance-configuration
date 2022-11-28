FROM ubuntu

ARG PROJECT
WORKDIR /opt/${PROJECT}

RUN apt-get update && apt-get install -y make python3.10 python3-pip git

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

COPY docker-config/bashrc /root/.bashrc
COPY ./requirements.txt ${WORKDIR}
RUN python -m pip install -r requirements.txt
