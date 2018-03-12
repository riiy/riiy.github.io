#### 安装

```
$ sudo yum install tigervnc-server
```

#### 设置密码

```bash
$ su - your_user  # 如果您想将VNC服务器配置为直接从CLI下运行，无需从GUI切换用户
$ vncpasswd
```

#### 修改配置文件

```
# cp /lib/systemd/system/vncserver@.service  /etc/systemd/system/vncserver@:1.service
# vi /etc/systemd/system/vncserver@\:1.service
```

写入以下内容：
```
[Unit]
Description=Remote desktop service (VNC)
After=syslog.target network.target
[Service]
Type=forking
ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
ExecStart=/sbin/runuser -l my_user -c "/usr/bin/vncserver %i -geometry 1280x1024"
PIDFile=/home/my_user/.vnc/%H%i.pid
ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
[Install]
WantedBy=multi-user.target
```
ps: my_user 替换成你的用户名

#### 启动并加入开机启动

接下来，运行以下命令重新加载systemd守护程序，并确保VNC在引导时为用户启动。

``` 
sudo systemctl daemon-reload
```

启用第一个服务器实例：

```
sudo systemctl enable vncserver @:1.service
```

#### 配置防火墙

检查防火墙状态
 ```
 sudo firewall-cmd --state
 ```
开启vnc的端口
 ```bash
 sudo firewall-cmd --permanent --zone=public --add-port=5901/tcp # 假如是5901
 ```
重新启动防火墙
 ```
 sudo firewall-cmd --reload
 ```

