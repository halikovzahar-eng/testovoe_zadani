FROM python:3.12-slim

WORKDIR /app

RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 appuser

COPY app.py .

EXPOSE 8080

USER appuser

CMD ["python", "app.py"]