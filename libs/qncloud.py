
from qiniu import Auth, put_file, etag
from swiper import conf
#需要填写你的 Access Key 和 Secret Key
def upload_to_qn(filepath,filename):
    """将本地文件上传到七牛云"""
    #构建鉴权对象 完成通讯
    qn_auth = Auth(conf.QN_AccessKey, conf.QN_SecretKey)
    #生成上传 Token，可以指定过期时间等
    token = qn_auth.upload_token(conf.QN_BUCKET, filename, 3600)
    #要上传文件的本地路径
    put_file(token, filename, filepath)


    #生成文件的 url

    file_url = "%s/%s" % (conf.QN_BASE_URL,filename)
    return file_url
