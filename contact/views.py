from django.http import HttpResponse
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

# Create your views here.
def requestHandler(request):
    if (request.method == 'POST'):
        response = HttpResponse(check_valid(request), content_type="text/plain")
    return response


def check_valid(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echostr = request.GET.get("echostr", None)
    wechat = init_wechat_sdk()
    if wechat.check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return None


def init_wechat_sdk():
    conf = WechatConf(
        token='pHmNrfXUFhKlpScFA1vYjTIZr',
        appid='wx9f17765d31c60590',
        appsecret='-akqs0eCRlzg8ZLxexjV0Z9z8eCIuwU-azj--LVyDJ6BID_-XYQQ_g9rXJhvovCD',
        encrypt_mode='safe',
        encoding_aes_key='WlT2qlLR6VBTDzPuTpLzPeL4aGd6OyrtaBKLhzQ8Dwj'
    )
    return WechatBasic(conf)