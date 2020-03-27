broker_url = "redis://127.0.0.1:6379/6" #连接redis
broker_pool_limit = 10 # Borker 连接
timezone = "Asia/Shanghai"
accept_content = ["pickle"]
task_serializer = "piclke"


result_backend = "redis://127.0.0.1:6379/6"
result_serializer = "pickle"
result_cache_max = 10000  #任务结果最大缓存数量

result_expires = 3600 #任务 结束过期时间
worker_redirect_stdouts_level = "INFO"