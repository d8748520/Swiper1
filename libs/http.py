import json
from django.http import HttpResponse
from common import stat
from swiper import settings

def render_json(data=None,code=stat.OK):
    """渲染需要的JSON数据"""
    result = {
        "data":data,
        "code":code
    }
    if settings.DEBUG:
        #调试环境的格式
        json_data = json.dump(result,ensure_ascii=False,indent=4,sort_keys=True)
    else:
        # 生产环境的格式
        json_data = json.dump(result,ensure_ascii=False,separators=(",",":"))
    return json_data