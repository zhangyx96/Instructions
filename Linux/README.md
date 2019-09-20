# 一、用户管理
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
>[更多详细内容参见网页](https://www.cnblogs.com/pengyunjing/p/8543026.html)

# 二、服务器管理
## 磁盘管理
```shell
df -hl
```
df 命令是linux系统上以磁盘分区为单位来查看文件系统的命令，后面可以加上不同的参数来查看磁盘的剩余空间信息。
```shell
df -hl 查看磁盘剩余空间
df -h 查看每个根路径的分区大小
du -sh [目录名] 返回该目录的大小
du -sm [文件夹] 返回该文件夹总M数
df --help 查看更多功能
```
```shell
sudo du -sh /home/* #查看Linux中各个用户使用的存储空间大小
du -h --max-depth=1 #查看各文件夹大小
```

# 二、Conda 
## 环境管理

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
# 三、进程管理
```shell
kill -9
```
表 1 kill命令常用信号及其含义    


信号编号|信号名|含义
:-:|-|-|
0|EXIT|程序退出时收到该信息。
1|HUP|挂掉电话线或终端连接的挂起信号，这个信号也会造成某些进程在没有终止的情况下重新初始化。
2|INT|表示结束进程，但并不是强制性的，常用的 "Ctrl+C" 组合键发出就是一个 kill -2 的信号。
3|QUIT|退出。
9|KILL|杀死进程，即强制结束进程。
11|SEGV|段错误。
15|TERM|正常结束进程，是kill命令的默认信号。

# 四、监控服务器显卡占用情况
[参见此网页](https://github.com/zhangwenxiao/GPU-Manager)

# 五、TZ一键脚本
```shell
wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh
chmod +x shadowsocks-all.sh
./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
```