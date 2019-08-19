# 服务器管理
* **创建普通用户**
```shell
sudo useradd username -p password
```
* **删除用户**
```shell
userdel username
```
* **修改密码**
```shell
1. 修改当前用户密码
passwd 
2. 修改某个用户密码
passwd username
```

# conda 
* **环境管理**

a.创建环境
```shell
conda create --name myenv
conda create -n myenv python=3.4
conda create -n myenv scipy=0.15.0
```  
b.通过environment.yml文件创建环境
```shell
conda env create -f environment.yml
```

