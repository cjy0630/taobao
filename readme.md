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
第一次得到本程序时配置文件中[my_settings]部分的cookie、keyword和[db_settings]部分的passwd均为空，需进行设置后才可正常运行本程序。

有两种方式可以对配置文件进行设置

1、直接修改config/settings.cfg文件进行设置

2、运行run.py文件，根据控制台菜单选择相应功能进行设置

![image](https://github.com/cjy0630/taobao/blob/master/taobao/images/settings_menu.png)

2019/07/06更新：
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

========================================================================================================================================

更新：
增加设置爬取商品页数及评论页数功能，根据设置进行爬取

========================================================================================================================================

更新：
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

========================================================================================================================================

由于本程序仅用于测试，未使用任何需要付费的反爬措施，为避免触发滑动验证甚至封号，程序运行时间较长！
经过测试发现淘宝评论的反爬机制是滑动验证，同一ip短时间内多次访问相同url很容易触发滑动验证。
本程序正常运行中没有反复请求同一url的情况，使用随机延时来避免滑动验证的触发，每次请求间隔1-5秒不等。
由于本程序仅为简单测试数据获取，并未进行去重处理。

程序中我自己的cookie已经删掉，如需运行程序请先设置自己的cookie，本程序可以通过两种方法来设置Cookie：
1、直接修改配置文件（config/settings.cfg）中的cookie
2、运行run.py，通过引导菜单设置Cookie

本程序的所有api均通过config/settings.cfg进行设置，当爬取出现问题需要变更cookie或api都可运行run.py后选择相应菜单进行修改设置，也可直接打开配置文件进行修改
注意：config/settings.cfg配置文件中的keyword必须通过运行run.py后的菜单进行设置，其它项目都可直接修改配置文件进行设置

由于本程序在开始爬取前通过选择菜单进行了一些爬取前的必要设置，请运行run.py文件根据菜单选项来启动爬虫，否则爬虫将无法爬取

如果爬取中提示出现了滑动验证，可先尝试更换cookie解决问题，在不更换的前提下程序可继续运行，过一段时间滑动验证会消失可继续爬取
