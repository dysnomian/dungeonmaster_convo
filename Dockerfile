FROM python:3.11

WORKDIR /app

COPY . /app

EXPOSE 8081

RUN pip install -U setuptools setuptools_scm wheel langchain langchain-community langchain-openai

RUN python setup.py install

CMD ["python", "src/dungeonmaster_convo"]