# Github Instructions
## 配置Github
1. 首先在本地创建ssh key 
```shell
$ ssh-keygen -t rsa -C "your_email@youremail.com"
//验证是否成功
$ ssh -T git@github.com
```

2. 如果是第一次的会提示是否continue，输入yes就会看到：You've successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。接下来要做的就是把本地仓库传到github上去，在此之前还需要设置username和email，因为github每次commit都会记录他们。

```shell
$ git config --global user.name "your name"
$ git config --global user.email "your_email@youremail.com"
```


