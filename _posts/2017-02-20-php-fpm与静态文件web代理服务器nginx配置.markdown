
> nginx 版本：1.10.1。 主要涉及到的方面有：静态文件缓存、ip访问限制、目录保护、静态文件防盗链及文件下载速度限制等，后端php框架单一路由入口配置。如无特殊说明，下列代码是nginx配置文件，具体使用方法可以查询[nginx官方文档](https://nginx.org/en/docs/)


#### 静态文件缓存

```
#更新静态文件可以使用gulp
location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
{
      expires 1M; 	#  	1M代表一个月，1y代表一年，1s代表一秒
}
location ~ .*\.(js|css)$
{
       expires 1d; 	# 	代表缓存一天
}
```

#### ip访问限制

```
# allow支持子网掩码
allow 114.245.32.39; allow 101.226.0.0/16;
deny all;
```

#### 目录保护
如果打开的是静态页面或图片等非php文件，会提示要输入密码，但是，如果打开的是php文件，则设置无效，会直接执行php文件。

Nginx保护目录的配置如下，目录密码保护文件是 /etc/nginx/htpasswd,生成密码文件：

```htpasswd -b -c  /etc/nginx/htpasswd username password;```

```
location ~ /admin {								#admin为要保护的目录名称，location 的意思就是保护从网页根目录算起的admin 目录
	auth_basic          ”PLEASE LOGIN”;			#就是进入资料夹时会显示的信息
	auth_basic_user_file /etc/nginx/htpasswd;	#验证用户及密码文件
}
```

#### 静态文件防盗链

```
location ~* \.(txt|ico|gif|png|bmp|jpg|jpeg|zip|rar|gz|7z|exe|mp3|flv|swf)$ {
	valid_referers none blocked easygaokao.com www.easygaokao.com;
	if ($invalid_referer) {
		rewrite ^/ http://www.easygaokao.com/dev.html;	# 盗链跳转地址
	}
}
```

#### 文件下载速度限制

设定一个叫做 crawler 的区域，大小为 20MB

```limit_zone crawler $binary_remote_addr 20m;```

然后在 server 的区段加上

```
location ~ .*\.(zip|rar|gz|tar|exe|mp3|flv|swf|jpg|jpeg)$
{
	limit_conn crawler 1; 	# 限制档案类型只能单线下载
	limit_rate 500k; 		# 再加上限速速率
}
```

#### 后端php框架单一路由入口配置及fpm配置

这是laravel的入口配置
```    
location / {
	try_files $uri $uri/ /index.php?$query_string;
}
```
php-fpm的sock配置
```
location ~ \.php$ {
    fastcgi_split_path_info ^(.+\.php)(/.+)$;
    #fastcgi_pass 127.0.0.1:9000;				# 端口配置
    fastcgi_pass unix:/var/run/php7.0-fpm.sock;	# socket文件配置，性能更优
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    fastcgi_intercept_errors off;
    fastcgi_buffer_size 16k;
    fastcgi_buffers 4 16k;
    fastcgi_connect_timeout 300;
    fastcgi_send_timeout 300;
    fastcgi_read_timeout 300;
}
```
#### https配置

```
server {
    listen 443;										# 默认端口443
    server_name easygaokao.com;
    ssl on; 										# 开启ssl
    ssl_certificate   cert/214016068200359.pem;		# 证书文件
    ssl_certificate_key  cert/214016068200359.key;	# 证书文件
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    # 以下省略其它配置
}
```