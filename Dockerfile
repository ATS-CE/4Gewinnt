# ---- Build stage ----
FROM python:3.12-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --no-compile --target=/libs -r requirements.txt

COPY . .

# ---- Runtime stage (distroless) ----
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app

COPY --from=builder /libs /libs
COPY --from=builder /app /app

ENV PYTHONPATH="/libs"

CMD ["-m", "app"]
