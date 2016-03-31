import logging
from django.core.handlers.wsgi import WSGIRequest

from django.http import HttpResponse

from wechatpy.enterprise.crypto import WeChatCrypto
from wechatpy.enterprise.exceptions import InvalidCorpIdException
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.enterprise import parse_message, create_reply
from django.views.decorators.csrf import csrf_exempt

TOKEN = 'pHmNrfXUFhKlpScFA1vYjTIZr'
CORP_ID = 'wx9f17765d31c60590'
AES_KEY = 'WlT2qlLR6VBTDzPuTpLzPeL4aGd6OyrtaBKLhzQ8Dwj'


# Create your views here.
def requestHandler(request):
    response = HttpResponse(process_request(request), content_type="text/plain")
    return response


# @csrf_exempt
def process_request(request):
    signature = request.GET.get("msg_signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echostr = request.GET.get("echostr", None)
    crypto = WeChatCrypto(TOKEN, AES_KEY, CORP_ID)
    if request.method == 'GET':
        echostr = crypto.check_signature(signature, timestamp, nonce, echostr)
        return echostr
    elif request.method == 'POST':
        try:
            msg = crypto.decrypt_message(request.body, signature, timestamp, nonce)
        except (InvalidCorpIdException, InvalidSignatureException):
            return None
        msg = parse_message(msg)
        if msg.type == 'text':
            reply = create_reply(msg.content, msg).render()
        else:
            reply = create_reply('Can not handle this for now', msg).render()
        res = crypto.encrypt_message(reply, nonce, timestamp)
        return res