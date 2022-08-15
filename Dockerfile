FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN ["mkdir", "/myAPIshop"]
WORKDIR /myAPIshop
ADD . /myAPIshop
RUN pip install -r requirements.txt
