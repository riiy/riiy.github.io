> 用过的网站访问日志分析工具：后端的有大而全的有elk,简单易用的有awstats、goaccess;前端的访问统计有google analytics(开源替代版本piwik),国内有cnzz、百度统计等。有的时候，用一些shell命令更为方便一些。

#### 日志格式

> nginx log format
```
 log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
```

#### 脚本命令

1. 统计每url流量

 ```
cat access.log | awk '{url=$7; requests[url]++;bytes[url]+=$10} END{for(url in requests){printf("%sKB\t%sKB/req\t%s\t%s\n", bytes[url] / 1024 , bytes[url] /requests[url] / 1024, requests[url], url)}}' | sort -nr | head -n 15
```

1. 统计每ua访问

 ```
cat access.log| awk -F '"' '{ua=$6; requests[ua]++;} END{for(ua in requests){printf("%s\t%s\n",  requests[ua], ua)}}' | sort -nr | head -n 150
```

1. 统计每IP访问

 ```
cat access.log| awk   '{ip=$1; requests[ip]++;} END{for(ip in requests){printf("%s\t%s\n",  requests[ip], ip)}}' | sort -nr | head -n 150
```

1. 统计每小时访问

 ```
cat access.log| awk -F ':'  '{time=$2; requests[time]++;} END{for(time in requests){printf("%s\t%s\n",  requests[time], time)}}' | sort -nr
```
