![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250824%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250824T202039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b71e5ef7c3dc8b677bf98c63f0cbf6c4ab823c97926e5b40279bb369af75747)

## Resources

**Read or watch:**

* [Redis commands](https://intranet.hbtn.io/rltoken/VOYtf-O0J8IniAaofOwoNQ "Redis commands")
* [Redis python client](https://intranet.hbtn.io/rltoken/yqIvla14uyQ2pBRk2i-tBQ "Redis python client")
* [How to Use Redis With Python](https://intranet.hbtn.io/rltoken/NxpS4PTyCpDK29oLyCBwHQ "How to Use Redis With Python")
* [Redis Crash Course Tutorial](https://intranet.hbtn.io/rltoken/vk2Wan5dEYyoGNwCIvoFaQ "Redis Crash Course Tutorial")

## Learning Objectives

* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Requirements

* All of your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All of your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* Your code should use the `pycodestyle` style (version 2.5)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Install Redis on Ubuntu 20.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: `service redis-server start`
