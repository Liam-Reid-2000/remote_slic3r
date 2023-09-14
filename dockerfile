FROM ubuntu:22.04

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y tar bzip2 && \
    apt-get install -y python3 && \ 
    apt-get clean 


RUN tar -xjf slic3r-1.3.0-linux-x64.tar.bz2

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]