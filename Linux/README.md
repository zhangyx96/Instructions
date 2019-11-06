# 一、服务器管理
## 用户管理
* **创建普通用户**
```shell
sudo useradd username -p password
sudo useradd -d /space2/*** -m ***   #在指定目录创建用户
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
## 进程管理
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

### 批量kill掉包含某个关键字得进程
```shell
ps -ef | grep stress | grep -v grep | cut -c 9-15 | xargs kill -9
```
运行这条命令将会杀掉所有含有关键字"stress"的进程  
下面将这条命令作一下简单说明:  
管道符"|"用来隔开两个命令，管道符左边命令的输出会作为管道符右边命令的输入。  
"ps -ef" 是linux里查看所有进程的命令。这时检索出的进程将作为下一条命令"grep stress"的输入。  
"grep stress" 的输出结果是，所有含有关键字"stress"的进程。  
"grep -v grep" 是在列出的进程中去除含有关键字"grep"的进程。  
"cut -c 9-15" 是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。  
"xargs kill -9" 中的 xargs 命令是用来把前面命令的输出结果（PID）作为"kill -9"命令的参数，并执行该命令。"kill -9"会强行杀掉指定进程。  
其它类似的情况，只需要修改"grep LOCAL=NO"中的关键字部分就可以了。  
另一种方法，使用awk  
```shell
ps x | grep gas | grep -v grep | awk '{print $1}' | xargs kill -9
```

## 监控服务器显卡占用情况
[参见此网页](https://github.com/zhangwenxiao/GPU-Manager)

# 二、基础命令
## chmod
Linux/Unix 的文件调用权限分为三级 : 文件拥有者、群组、其他。利用 chmod 可以藉以控制文件如何被他人所调用。
```shell
chmod ugo+r file1.txt #将文件 file1.txt 设为所有人皆可读取
chmod a+r file1.txt  #将文件 file1.txt 设为所有人皆可读取
chmod ug+w,o-w file1.txt file2.txt #将文件 file1.txt 与 file2.txt 设为该文件拥有者，与其所属同一个群体者可写入，但其他以外的人则不可写入
chmod -R a+r * #将目前目录下的所有文件与子目录皆设为任何人可读取 :
```
此外chmod也可以用数字来表示权限
```shell
chmod 777 file
```
```shell
chmod abc file
```
其中a,b,c各为一个数字，分别表示User、Group、及Other的权限。

**r=4，w=2，x=1**
* 若要rwx属性则4+2+1=7；
* 若要rw-属性则4+2=6
* 若要r-x属性则4+1=5



# 三、Conda命令 
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

# 三、VPN一键脚本
```shell
wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh
chmod +x shadowsocks-all.sh
./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
```