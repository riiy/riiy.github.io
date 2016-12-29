> 阿里云服务器centos安装wkhtmltopdf,以及中文乱码解决方法

## 安装依赖

xorg-x11-fonts-Type1 xorg-x11-fonts-75dpi

## 安装wkthmltopdf

1. 下载 wkthmltopdf.org
2. 解压到/usr/local/bin/wkhtmltopdf
3. 注意添加执行权限

## 中文乱码问题

1. 下载中文字体文件
2. 上传至/usr/share/fonts/XXX.ttf  # 注意ttf格式字体，其它字体可能无效
3. 执行下列命令，使字体文件生效

```
mkfontscale && mkfontdir && fc-cache -f 
```

## 测试
