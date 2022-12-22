## pull official base image
## FROM python:3.10.7
FROM python:3.10.7-alpine
RUN echo 'Creating image'

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## Instant Client on Windows requires an appropriate Visual Studio Redistributable. 
## On Linux, the libaio (sometimes called libaio1) package is needed. When using 
## Instant Client 19 on recent Linux versions, such as Oracle Linux 8, you may 
## also need to install the libnsl package. This is not needed from Instant Client 21 onward.

RUN apk add --no-cache libxml2-dev libxslt-dev gcc musl-dev && \
    apk add --no-cache libc-dev libnsl libnsl-dev libc6-compat libaio
# apk add python-dev python-distribute python-pip

WORKDIR /usr/lib
## Download the Oracle instant client and add to your project.
## Version `21` for Oracle Database >=12.1. 
## Version `19, 18 and 12.2` for Oracle Database >=11.2. 
## Version `12.1` client for Oracle Database >=10.2. 
## Version `11.2` client for Oracle Database >=9.2.

## COPY Local folder of client lib files
COPY instantclient_11_2_linux /usr/lib/instantclient 

RUN cd /usr/lib/instantclient* && \
    rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    ln -s /usr/lib/instantclient/libclntsh.so.11.1 /usr/lib/libclntsh.so && \
    ln -s /usr/lib/instantclient/libnnz11.so /usr/lib/libnnz11.so && \    
    ln -s /usr/lib/instantclient/libociicus.so /usr/lib/libociicus.so && \    
    # ln -s /usr/lib/libnsl.so.2 /usr/lib/libnsl.so.1 && \
    ## if Exception occurs then check version /usr/lib/libnsl.so.* in Docker terminal and
    ## do the following 
    ln -s /usr/lib/libnsl.so.3 /usr/lib/libnsl.so.1 && \
    ln -s /lib/libc.so.6 /usr/lib/libresolv.so.2 && \
    ln -s /lib64/ld-linux-x86-64.so.2 /usr/lib/ld-linux-x86-64.so.2

## set below to resolve error ora-01804    
ENV LD_LIBRARY_PATH /usr/lib/instantclient

## Application Directory
RUN mkdir -p /opt/imsapi
WORKDIR /opt/imsapi
RUN adduser -S imsapi
RUN chown -R imsapi /opt/imsapi

## COPY project from local directory myapp/*.* to docker /opt/imsapi
COPY myapp/ /opt/imsapi/


ADD requirements.txt /opt/imsapi/
RUN pip install --upgrade pip
## install dependencies
RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:9001","wsgi:app"]

EXPOSE 9001


