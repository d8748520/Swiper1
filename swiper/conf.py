"""程序逻辑和第三方平台的配置"""

#云之讯短信平台配置
YZX_SMS_API = "https://open.ucpaas.com/ol/sms/sendsms"
YZX_SMS_ARGS = {
    "sid": "1214636c97ad4d19391ee8bcd2a90b53",
    "token": "daa881ddeb960ae1e394ac630f1c43e3",
    "appid": "272a342d047a4206936ec2fa00ad1c12",
    "templateid": "533721",  # 模板
    "param": None,  # 验证码
    "mobile": None # 手机号
}

#七牛云配置
QN_AccessKey = "UYa9TK0V-wLabVW7ev5gqZWnXsRb1q6LBh494T3C"
QN_SecretKey = "eacCN0qLKU7wWyMPLioqxiKB81oz58hd7UTxu-3N"
QN_BUCKET = "swiper-tiger"
QN_BASE_URL = "http://q7qudtwqq.bkt.clouddn.com"