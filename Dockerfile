FROM python:3.8-alpine

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pymongo
RUN pip install requests

COPY . .

EXPOSE 3000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "3000"]
