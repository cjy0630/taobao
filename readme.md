淘宝商品评价爬虫
===============
输入要爬取的商品后自动爬取相关商品评论，数据异步持久化至MySQL数据库，支持增量爬取。

效果预览：
![image](https://github.com/cjy0630/taobao/blob/master/taobao/images/taobaoSpider.gif)

上手指南
=======
为使程序使用更加灵活，该程序通过配置文件对爬虫进行了各种爬取设置，可以在爬取前根据控制台菜单选项进行各种设置。

当前版本功能及可设置项目：

1、搜索指定商品

2、显示当前设置

3、设置Cookie

4、修改搜索商品API

5、修改获取评论API

6、设置爬取页数

7、初始化配置

以下指南将帮助你正确的使用该程序。

安装要求
-------
1、Anaconda3

2、MySQL

3、Scrapy

安装步骤
-------
1、官网下载Anaconda3

下载地址：https://www.anaconda.com/distribution/

根据操作系统下载对应的版本

![image](https://github.com/cjy0630/taobao/blob/master/taobao/images/anaconda_download.png)

安装过程此处不赘述

2、官网下载MySQL

下载地址：https://dev.mysql.com/downloads/mysql/

根据操作系统下载对应的版本

![image](https://github.com/cjy0630/taobao/blob/master/taobao/images/mysql_download.png)

安装过程此处不赘述，注意：安装时设置好密码，如需远程跨域写入数据需对用户进行权限设置，否则写入时会被数据库拒绝。

3、安装Scrapy

打开命令行输入pip install scrapy进行安装

如安装遇到问题请进行环境变量设置，也可使用Anaconda Prompt进行安装，同样输入pip install scrapy进行安装。

运行程序
-------
第一步：在MySQL中执行database/create_db.sql脚本创建数据库及数据表

第二步：设置爬虫

第一次得到本程序时配置文件中[my_settings]部分的cookie、keyword和[db_settings]部分的passwd以及settings.py文件中尾部的MySQL相关设置均为空，需进行设置后才可正常运行本程序。

有两种方式可以对配置文件进行设置

1、直接修改config/settings.cfg文件进行设置

2、运行run.py文件，根据控制台菜单选择相应功能进行设置

![image](https://github.com/cjy0630/taobao/blob/master/taobao/images/settings_menu.png)

第三步：修改settings.py文件尾部的MySQL设置，填写自己的数据库信息

说明
---
本程序目前仅用于测试，并未使用任何需要付费的反爬措施，爬取页数有限，登陆是使用Cookie模拟登陆，需要先使用浏览器进行登陆并复制Cookie。

如需改善可使用代理IP创建代理池、创建Cookie池等方法，进行抓取时随机选择代理IP及随机选择Cookie发出请求。

出于效率及资源消耗问题考虑，本程序未使用Selenium，并且在后续更新中也将尽量避免或巧妙使用Selenium。

如果爬取中提示出现了滑动验证，可先尝试更换cookie解决问题。

后续版本将更新自动登陆功能。

作者
---
崔佳毅（JiayiCui）

版权声明
-------
版权所有：崔佳毅(JiayiCui)

未经本人许可不得应用于商业用途

如需转载请联系作者并注明出处

免责声明
-------
本程序仅用于测试学习，如他人擅自应用于商业用途，造成的法律后果与作者无关。


版本更新
=======

2019/07/06更新
--------------
本次更新加入了去重功能，程序可以断点续爬

新增模块：converter.py  removal.py

converter.py用于各种转换，如：md5  unicode，当前版本仅编写了md5功能

removal.py用于进行重复验证，实现去重功能，在向服务器发送请求前进行验证，如果已爬取过则不会向服务器发起请求

新增数据库表：grab_records

此表用于记录商品评论页

配合新添加的模块对spiders/alcohol.py  config/config_operate.py  items.py  pipelines.py  config/settings.cfg中的代码进行了修改



下一版本预计功能：

1、根据需求动态创建爬虫

2、根据需求添加爬虫爬取队列


更新
----
增加设置爬取商品页数及评论页数功能，根据设置进行爬取



更新
----
此版本修复了一些BUG并已经将数据以并发的形式持久化到本地mysql

运行前请先设置settings.py文件中的

MYSQL_HOST = ""

MYSQL_PORT = 

MYSQL_DBNAME = ""

MYSQL_USER = ""

MYSQL_PASSWORD = ""

已去除BUG：上一版本每件商品只爬取到1页评论，第二页开始报错

BUG原因：爬取评论递归时漏写了meta参数

修改位置：taobao/spiders/alcohol.py中的parse_comment(self, response)函数

上一版本：yield scrapy.Request(comment_url, headers=headers, callback=self.parse_comment, dont_filter=True)

本次修复后：yield scrapy.Request(comment_url, headers=headers, meta={'headers': headers, 'item_id': item_id, 'user_id': user_id, 'title': title}, callback=self.parse_comment, dont_filter=True)
