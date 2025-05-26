# Use Ubuntu as the base image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Update and install basic tools
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    dnsutils \
    git \
    vim \
    build-essential \
    ca-certificates \
    unzip \
    python3 \
    python3-venv \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create symlink for python3.12 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Environment variables for NVM, Rust, Emscripten, Micromamba
ENV NVM_DIR=~/.nvm
ENV RUSTUP_HOME=~/.rustup
ENV CARGO_HOME=~/.cargo
ENV MAMBA_ROOT_PREFIX=/opt/micromamba
ENV EMSDK=/opt/emsdk

RUN mkdir -p $NVM_DIR $RUSTUP_HOME $CARGO_HOME $MAMBA_ROOT_PREFIX $EMSDK
# Set environment variables for PATH
ENV PATH=$NVM_DIR/versions/node/v18.18.2/bin:$CARGO_HOME/bin:$MAMBA_ROOT_PREFIX/bin:$EMSDK:$PATH

# Install NVM and Node.js
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash && \
    . "$NVM_DIR/nvm.sh" && \
    nvm install 18.18.2 && \
    nvm use 18.18.2 && \
    nvm alias default 18.18.2

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Install Emscripten SDK
RUN git clone https://github.com/emscripten-core/emsdk.git $EMSDK && \
    cd $EMSDK && \
    ./emsdk install latest && \
    ./emsdk activate latest

# Install Micromamba (static binary)
RUN curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C /usr/local/bin/ --strip-components=1 bin/micromamba && \
    micromamba shell init -s bash

# Default shell
CMD ["/bin/bash"]
