FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt ./
RUN apt-get update \
&& apt-get install -y --no-install-recommends git sqlite3\
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/* \ 
&& pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

# CMD ["python", "src/mysite/manage.py", "runserver" ]