#!/bin/bash

installation_python(){
    yum install -y libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel wget llvm ncurses-devel openssl-devel lzma-sdk-devel epel-release redhat-rpm-config  vim wget git 
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    echo '
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ' >> ~/.bashrc
    source ~/.bashrc
    pyenv install 2.7.17
    pyenv install 3.8.0
}

create_and_activate_env(){
    pyenv virtualenv 2.7.17 venv2.7.17
    pyenv virtualenv 3.8.0 venv3.8
    pyenv activate venv3.8
}
installation_python
create_and_activate_env

/vagrant/helloworld.py







