FROM public.ecr.aws/docker/library/python:3.7-slim

WORKDIR /

COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "--host=0.0.0.0", "main:app"]