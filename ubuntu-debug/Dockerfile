FROM ubuntu:22.04

RUN apt-get update

ARG DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get install -y python3 python3-pip python3-venv python3-requests python3-flask python3-pytest

# Install build essential for compiling packages
RUN apt-get install -y build-essential

RUN apt-get install -y git curl dnsutils

RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
