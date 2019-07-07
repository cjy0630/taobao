# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     ':authority': 's.taobao.com',
#     ':method': 'GET',
#     ':path': '/search?q=%E8%8C%85%E5%8F%B0&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190703&ie=utf8',
#     ':scheme': 'https',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'cookie': 'cna=eRpfFSQ/oFgCAXL1PV77YkyL; t=36778dd604d00ba8001dc47d6bd9e818; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=232293011727815606; uc3=vt3=F8dBy3jc5SHqWSQOuw8%3D&id2=UUkGUYyXZqM%3D&nk2=AHDYax8iWw%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D; tracknick=cjy0630; lgc=cjy0630; _cc_=UtASsssmfA%3D%3D; tg=0; enc=EfNORQXAfCl2iPKt2ZTQMxqEIERzhz1%2BWrD39ZSYuQ%2FhIEs0l%2BSYiZWsTe8QtNwRHPmZjBa7lKw8zk1ZruGXpA%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; mt=ci=-1_0; cookie2=1af4f1f6d46f0437e1ba4320b2c63fcc; _tb_token_=ee383b785e71; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=292025; JSESSIONID=6C307E79FD7803439D7E5A5C7CA88885; uc1=cookie14=UoTaGqymsIcsiA%3D%3D; isg=BFhY9M-6sSemBJxb3i7K7eMpKYYq6dnJyFFr0pJLrBJ4LfsXOlUfWyrPZSW4PXSj; l=bBNxpH8ev5OF57KQBOfwquI8S87toQAbzsPzw4GXGIB1tQ13QdQHmHwQG3Z9I3Q_E_fQ9etPjJDd8REpyizKg',
#     'referer': 'https://s.taobao.com/search?q=%E8%8C%85%E5%8F%B0&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190703&ie=utf8'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'taobao.pipelines.TaobaoPipeline': 300,
    'taobao.pipelines.MysqlTwistedPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3307
# MYSQL_HOST = "18044s8b29.imwork.net"
# MYSQL_PORT = 10658
MYSQL_DBNAME = "taobao"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""

COMMANDS_MODULE = 'taobao.commands'
