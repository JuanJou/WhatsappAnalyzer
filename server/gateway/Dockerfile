FROM ubuntu:latest

RUN echo "Installing zsh..." && \
    apt-get update && \
    apt-get install -y zsh curl git wget

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true

RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

#RUN git clone git://github.com/wting/autojump.git && cd autojump && ./install.py

SHELL ["/bin/zsh", "-c"]

