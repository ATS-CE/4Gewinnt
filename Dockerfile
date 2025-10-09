# Single-stage distroless Python image
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app

# copy only the script we need
COPY 4gewinnt.py /app

# run Python unbuffered so prints appear immediately in -it sessions
ENTRYPOINT ["python3", "-u", "4gewinnt.py"]