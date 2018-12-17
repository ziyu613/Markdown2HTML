### 系统服务相关

> 要使用此命令，软件必须得加入到*systemctl* 服务管理中

- 启动某服务

  ```shell
  sudo systemctl start <service-name>
  
  #比如tomcat
  sudo systemctl start tomcat
  ```
- 关闭某服务

  ```shell
  sudo systemctl stop <service-name>
  
  #比如tomcat
  sudo systemctl stop tomcat
  ```
- 查看某服务状态

  ```shell
  sudo systemctl status <service-name>
  
  #比如tomcat
  sudo systemctl status tomcat
  ```

- 设置某服务开机启动

  ```shell
  sudo systemctl enable <service-name>
  
  #比如tomcat
  sudo systemctl enable tomcat
  ```

### 防火墙

- 开启、关闭、禁用防火墙

  ```shell
  #开启
  systemctl start firewalld.service
  
  #关闭
  systemctl stop firewalld.service
  
  #禁用
  systemctl disable firewalld.service
  ```

- 开启某端口号

  ```shell
  firewall-cmd --zone=public --add-port=80/tcp --permanent
  firewall-cmd --reload
  ```

### 磁盘

- 查看分区大小

  ```shell
  df -h
  ```

- 查看当前目录占用空间大小

  ```shell
  du -h --max-depth=1 ./
  ```

### 主机相关

- 修改主机名

  ```shell
  hostnamectl set-hostname <host-name>
  ```
