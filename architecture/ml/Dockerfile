FROM python:3.10

COPY . .

RUN echo "Installing zsh..." && \
    apt-get update && \
    apt-get install -y zsh curl git wget locales python3 ripgrep && \
    locale-gen en_US.UTF-8


RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales


RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true

RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

ENV SHELL="zsh"

RUN git clone https://github.com/wting/autojump.git && cd autojump && ./install.py

SHELL ["/bin/zsh", "-c"]

EXPOSE 8003
