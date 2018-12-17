> 可以在 kibana 中查看 elasticsearch集群状态
>
> kibana 访问地址 http://{es_master_ip}:5601
>
> 2.0.0版本以后才会安装kibana 低版本无法使用 kibana



日志存储，查询，主要包括以下数据：

- 服务器监控日志
- 系统日志
- 地图服务访问、监控日志
- 系统操作、访问日志
- 数据库监控日志
- 微服务运行日志
- 管理类数据
- ... ...



### shell 脚本

- 查看 elasticsearch 启动状态

  ```shell
  systemctl status elasticsearch
  ```

- 启动 elasticsearch

  ```shell
  systemctl start elasticsearch
  ```

- 关闭 elasticsearch

  ```shell
  systemctl stop elasticsearch
  ```

- 重启 elasticsearch

  ```shell
  systemctl restart elasticsearch
  ```

### httpd 请求

- 查看 elasticsearch 节点

  ```http
  http://{es_ip}:9200/_cat/nodes?format=json&pretty
  ```

- 查看 elasticsearch 集群健康状态

  ```http
  http://10.0.7.220:9200/_cat/health?format=json&pretty
  ```


### 日志位置

/var/log/elasticsearch