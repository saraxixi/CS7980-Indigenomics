BOT_NAME = "indigenous_news"
SPIDER_MODULES = ["indigenous_news.spiders"]
NEWSPIDER_MODULE = "indigenous_news.spiders"

# User-Agent 模拟真实用户
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

# 不遵守 robots.txt
ROBOTSTXT_OBEY = False

# 下载延迟和并发设置
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# 默认请求头设置
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# 启用中间件
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    # "scrapy_proxy_pool.middlewares.ProxyPoolMiddleware": 610,
    # "scrapy_proxy_pool.middlewares.BanDetectionMiddleware": 620,
}

# 启用 AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# 启用 HTTP 缓存（可选）
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = [403, 500, 503]
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 设置未来兼容的默认值
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"