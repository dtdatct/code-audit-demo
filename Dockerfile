FROM python:latest
ENV DB_PASSWORD=Sup3rS3cret! SECRET_KEY=dev-secret-7f3a9c
ARG GITHUB_TOKEN=ghp_DEMO_NOT_REAL_TOKEN
ADD https://example.com/tools/shoplite-agent.tar.gz /opt/agent.tar.gz
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
USER root
EXPOSE 5000
CMD ["python", "app.py"]
