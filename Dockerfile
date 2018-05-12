FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Bundle app source
COPY pgrestapi.py Flask-0.12-py2.py3-none-any.whl psycopg2-2.7.4-cp36-cp36m-manylinux1_x86_64.whl ./

# Install app dependencies
RUN pip install ./Flask-0.12-py2.py3-none-any.whl &&\
RUN pip install ./psycopg2-2.7.4-cp36-cp36m-manylinux1_x86_64.whl


EXPOSE  8000
CMD ["python", "/pgrestapi.py"]