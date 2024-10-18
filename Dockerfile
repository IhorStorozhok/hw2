FROM python:3.10.12
ENV dist /dist
WORKDIR ${dist}
RUN pip install --no-cache-dir poetry
COPY . .
CMD ["poetry", "run", "python", "main.py"]
