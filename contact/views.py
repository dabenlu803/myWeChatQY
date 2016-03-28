import logging

from django.http import HttpResponse
from wechat_sdk import WechatBasic
from wechat_sdk import WechatConf

from lib.WXBizMsgCrypt import WXBizMsgCrypt


# Create your views here.
def requestHandler(request):
    if (request.method == 'GET'):
        response = HttpResponse(check_valid(request), content_type="text/plain")
        return response
    else:
        return None

def check_valid(request):
    token = 'pHmNrfXUFhKlpScFA1vYjTIZr'
    appid = 'wx9f17765d31c60590'
    appsecret = '-akqs0eCRlzg8ZLxexjV0Z9z8eCIuwU-azj--LVyDJ6BID_-XYQQ_g9rXJhvovCD'
    encrypt_mode = 'safe'
    encoding_aes_key = 'WlT2qlLR6VBTDzPuTpLzPeL4aGd6OyrtaBKLhzQ8Dwj'
    signature = request.GET.get("msg_signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echostr = request.GET.get("echostr", None)
    wxcpt= WXBizMsgCrypt(token, encoding_aes_key, appid)
    logging.warning('signature = %s', signature)
    logging.warning('timestamp = %s', timestamp)
    logging.warning('nonce = %s', nonce)
    logging.warning('echostr = %s', echostr)
    ret,sEchoStr=wxcpt.VerifyURL(signature, timestamp,nonce,echostr)
    logging.warning('sEchoStr = %s', sEchoStr)
    # wechat = init_wechat_sdk()
    # if wechat.check_signature(signature, timestamp, nonce):
    #     print(echostr)
    #     return echostr
    # else:
    #     return None
    if (ret != 0):
        return None
    else:
        return sEchoStr


def init_wechat_sdk():
    conf = WechatConf(
        token='pHmNrfXUFhKlpScFA1vYjTIZr',
        appid='wx9f17765d31c60590',
        appsecret='-akqs0eCRlzg8ZLxexjV0Z9z8eCIuwU-azj--LVyDJ6BID_-XYQQ_g9rXJhvovCD',
        encrypt_mode='safe',
        encoding_aes_key='WlT2qlLR6VBTDzPuTpLzPeL4aGd6OyrtaBKLhzQ8Dwj'
    )
    return WechatBasic(conf)