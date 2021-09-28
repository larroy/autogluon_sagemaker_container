FROM python:3.8-slim

RUN apt-get update
RUN apt install -y nginx build-essential
RUN rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash user
WORKDIR /home/user

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#RUN python setup.py bdist_wheel
RUN pip install .


#ENV PYTHONUNBUFFERED=TRUE
#ENV PYTHONDONTWRITEBYTECODE=TRUE
ENTRYPOINT ["bin/entrypoint.py"]

