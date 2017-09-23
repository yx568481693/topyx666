
《Linux系统及程序设计》实验报告
=======

## 实验名称：

### 实验一 Linux环境使用

## 学生姓名（班级、学号）：

### 王雨轩（信安1503班，5120152632）

## 指导教师：

### 韦勇

## 实验时间：

### 2016年9月18日晚上19～22点

# 1. 实验记录

（记录针对实验指导书中提出的*任务*，描述操作的结果、遇到的问题、解决的方法、实验的效果等内容，注意截图与文字说明相结合）

#### 首先先把权限切换为管理员权限
![](images/sudo.png)

## 安装Tomcat

1. **首先查询一下APT源空间中有没有tomcat的安装包，如下：**
![](images/tomcat_search.png)

2. **发现有tomcat7和tomcat8两个版本，选择tomcat8安装**
![](images/tomcat_install_1.png)
![](images/tomcat_insatll_2.png)

3. **看回显是安装好了，但是还是需要验证一下，先使用dokg命令来查看相关的安装信息。找到路劲/etc/init.d/tomcat8**
![](images/tomcat_dpkg_1.png)
![](images/tomcat_dpkg_2.png)

4. **最后看一下tomcat命令**
![](images/tomcat_help.png)

5. **安装成功**

6. **过程中出现的问题：**
    1）bin目录下没有tomcat的相关命令，一度以为是安装失败，最后在网上查到ubuntu版本下tomcat命令在/etc/init.d/下。
    2）apt-get命令前两次安装失败，第三次安装成功，应该是因为源空间是国外站点导致链接不稳定。

## 安装MySQL

1. **同样先查询源空间内有无MySQL的安装包**
![](images/mysql_search.png)

2. **mysql需要mysql_server.mysql_client,libmysqlclient_dev这三个服务才能正常使用，所以三个服务都要安装。mysql安装过程中需要设置root的密码**
![](images/mysql_install_1.png)
![](images/root=root,password=123.png)
![](images/mysql_install_2.png)

3. **安装完成之后用dpkg命令来查看安装包的信息**
![](images/mysql_dpkg.png)

4. **尝试连接本地mysql**
![](images/mysql_start.png)

5. **安装成功**

# 2.  思考题回答

（实验指导书后提出的思考题的回答）

1. **使用apt-cache search 命令查询有无相关安装包，并根据对应的描述来选择**
2. **要验证是否调用成功只需调用相关命令，如果命令能成功执行，则安装成功。如果系统中没有这些命令则表示安装失败**
3. **tomcat8安装到系统中的文件可用dpkg -L tomcat8命令查看：**

# 3. 实验体会

（实验后对*实验知识点*的理解，特别是发生错误的地方，特别需要注意避免空洞的个人感受，比如“通过实验，我掌握了……提高了我对……的兴趣”，必须是*技术性的总结*，比如“通过实验，我理解了设计SHELL程序的过程，首先……然后……，调试SHELL程序的方法是……”，可以提出意见和建议。)

    1）Linux中简化了软件安装的操作，在源空间存在相关安装包的时候可以使用apt，yum等命令快速安装软件。但是首先应该先使用查询命令以获得正确的安装包名称，然后再使用命令安装。
    2）验证安装是否成功是非常重要的，特别是一些对于服务类功能，需要先了解其常用命令并尝试使用这些命令。因为在不同的系统上安装后其操作方式可能有细微的差别，列如在ubuntu上利用apt安装tomcat后不同于其他系统会将tomcat命令存放在/bin目录下，而是存放于/etc/init.d目录下。不了解这些差别又未经过验证，则很可能在需要用到这些服务时产生很大的麻烦。
