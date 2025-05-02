# syntax=docker/dockerfile:1
FROM node:22-slim AS js_builder
# FROM ubuntu:24.04
#
# RUN rm -f /etc/apt/apt.conf.d/docker-clean; \
#     echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
#
# RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
#     --mount=type=cache,target=/var/lib/apt,sharing=locked \
#     apt-get update -y && apt-get upgrade -y && apt-get install -y curl && apt-get install -y gnupg
#
#
# RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm python3 python3-pip python3-venv
#
#
# # RUN chown -R 50004:50004 "/.npm"
# # RUN npm install whatwg-url
# # RUN npm install linkinator
#
#
# RUN npm install

# RUN npm install npm@11.3.0
RUN npm cache clean --force
# RUN "npx linkinator $1
ENTRYPOINT ["npx", "linkinator", "--recurse", "--verbosity", "error"]

# FROM python:3.12-slim-bullseye

# WORKDIR /link_checker
# ADD LICENSE requirements.txt ./
# ADD link_checker ./link_checker/
# ADD pyproject.toml ./
# RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt .
#
# ENTRYPOINT ["python", "-m", "link_checker"]
