# MACHINE_LEARNING

Repository for learning of Machine Learning.

## Environment

> Assumed development on MacOS

* MacOS 10.14.1
* Python 3.6.5
* pyenv 1.2.8
* pylint 2.2.2
* Docker 18.09.0

``` shell
# install pyenv
$ brew install pyenv

# use python 3.6.5
$ pyenv install 3.6.5
$ pyenv local 3.6.5

# install modules
$ pip install -r requirements.txt

# install tensorflow
$ pip install --upgrade pip
$ pip install tensorflow
```

### Install VSCode Extensions

```shell
# install extensions
$ cat .vscode/extensions.txt | xargs -L 1 echo code --install-extension
```

### Install Docker image

``` shell
# get docker image for tensorflow
$ docker pull tensorflow/tensorflow

# get docker image for pytorch
$ docker pull pytorch/pytorch
```

## Library

* Tensorflow
  * [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)
* Pytorch
  * [pytorch/pytorch](https://github.com/pytorch/pytorch)
