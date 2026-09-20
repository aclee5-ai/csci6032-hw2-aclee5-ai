FROM python:3.12-slim-bookworm

ARG COPILOT_CLI_VERSION=1.0.85

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
        git \
        gnupg; \
    install -d -m 0755 /etc/apt/keyrings; \
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        -o /etc/apt/keyrings/githubcli-archive-keyring.gpg; \
    chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg; \
    printf '%s\n' \
        'deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main' \
        > /etc/apt/sources.list.d/github-cli.list; \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
        | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg; \
    printf '%s\n' \
        'deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_22.x nodistro main' \
        > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install --no-install-recommends -y \
        gh \
        nodejs; \
    npm install --global "@github/copilot@${COPILOT_CLI_VERSION}"; \
    npm cache clean --force; \
    apt-get purge --auto-remove -y \
        gnupg; \
    rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash dev \
    && mkdir --parents /workspace \
    && chown --recursive dev:dev /workspace

USER dev
WORKDIR /workspace

CMD ["/bin/bash"]

