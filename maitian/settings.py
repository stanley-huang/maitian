# -*- coding: utf-8 -*-

# Scrapy settings for maitian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maitian'

SPIDER_MODULES = ['maitian.spiders']
NEWSPIDER_MODULE = 'maitian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maitian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maitian.middlewares.MaitianSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'maitian.middlewares.MaitianDownloaderMiddleware': 300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'maitian.pipelines.MaitianPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline':400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 爬取深度
DEPTH_LIMIT = 1

# ################################### Redis相关配置 ######################################
#
# # Redis 主机名
REDIS_HOST = '127.0.0.1'
# # Redis 服务端口
REDIS_PORT = 6379
#
# # redis编码类型
REDIS_ENCODING = "utf-8"
#

# # 启用Redis调度存储请求队列，替换掉scrapy 原来的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 启用所有爬虫都使用redis的去重规则
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

SHEDULTER_QUEUE_KEY = '%(spider)s:requests'

SHEDULTER_PERSIST = True
SHEDULTER_FLUSH_ON_START = False
# ########################################################################################
#
# ################################### MongoDB相关配置 ######################################
# Mongodb连接配置
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'scrapy_db'

# 启用持久化配置
ITEM_PIPELINES = {
   'maitian.pipelines.MongoDBPipeline':400,
}
# ########################################################################################