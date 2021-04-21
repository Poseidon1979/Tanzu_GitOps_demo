FROM python:3.7
WORKDIR /usr/src/app
COPY ./python ./python
COPY ./bin ./bin
RUN chmod a+x ./bin/*.*
RUN export PATH=./bin:$PATH
RUN pip install requests
CMD ["python", "./python/main.py"]