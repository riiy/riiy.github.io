在mac上通过brew 安装php的memcache扩展（brew install php56-memcache）后运行

~  php -m
PHP Warning:  PHP Startup: memcache: Unable to initialize module
Module compiled with build ID=API20131226,NTS
PHP    compiled with build ID=API20131226,NTS,debug
These options need to match
 in Unknown on line 0

Warning: PHP Startup: memcache: Unable to initialize module
Module compiled with build ID=API20131226,NTS
PHP    compiled with build ID=API20131226,NTS,debug
These options need to match
 in Unknown on line 0

报了这样的警告信息

 

解决：

brew remove php56-memcache

brew install php56-memcahe --build-from-source

