FROM python:slim

WORKDIR /code

COPY ./requirements.txt ./
RUN apt-get update \
&& apt-get install -y --no-install-recommends git sqlite3\
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/* \ 
&& pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]