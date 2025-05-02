# syntax=docker/dockerfile:1
FROM node:22-slim AS js_builder

RUN rm -f /etc/apt/apt.conf.d/docker-clean; \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y && apt-get upgrade -y

FROM python:3.12-slim-bullseye

WORKDIR /link_checker
ADD LICENSE requirements.txt ./
ADD link_checker ./link_checker/
ADD pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt .

# Change as required, eg
ENTRYPOINT ["python", "-m", "link_checker"]
