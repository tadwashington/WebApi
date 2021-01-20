# coding: utf-8

from flask import Flask, request, jsonify, make_response
from wsgiref.simple_server import make_server
import ssl
import http
import socket
import socketserver
import json
import random

apps = Flask(__name__)


# 支払確認API
@apps.route("/gateway/api/v1/qr/checkorder", methods=['GET'])
def getCPMReq():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    response = {}
    resjson: bytes = json.dumps({'message': 'getMethod'}).encode("utf-8")
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    # return make_response(jsonify(resp))
    # JSONファイルを読込んで還す
    p = ['cpmGetting.json', 'cpmGettingING.json']
    pt = random.choice(p)
    f = open(pt, 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)


# 返金確認API
@apps.route("/gateway/api/v1/qr/checkrefunds", methods=['GET'])
def getRefundReq():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    # JSONファイルを読込んで還す
    p = ['refundGet.json', 'refundGetF.json', 'refundGetW.json']
    pt = random.choice(p)
    f = open(pt, 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)


# 取引照会(店舗単位)API
@apps.route("/gateway/api/v1/qr/orders", methods=['GET'])
def getOrdersReq():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    # JSONファイルを読込んで還す
    p = ['refundGet.json', 'refundGetF.json', 'refundGetW.json']
    pt = random.choice(p)
    f = open(pt, 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)


# QRコード支払 API
@apps.route("/gateway/api/v1/qr/orders", methods=['PUT'])
def putReqOrder():
    '''
    Http Request Header 確認
    '''
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))

    payload = request.json
    print("Can You Get Json Params [order_id]? " + payload.get('order_id'))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))
    print("Can You Get Json Params [description]? " + payload.get('description'))
    print("Can You Get Json Params [price]? " + str(payload.get('price')))
    print("Can You Get Json Params [auth_code]? " + payload.get('auth_code'))
    print("Can You Get Json Params [currency]? " + payload.get('currency'))
    print("Can You Get Json Params [operator]? " + payload.get('operator'))
    '''
    # windowsで動かす場合にテキストファイルをloadすると勝手に「cp932」でloadされてしまうらしい
      ので、open関数にencoding="utf-8_sig"を明示的に指定する
    '''
    p = ['cpmResponse.json', 'cpmResponseIng.json']
    pt = random.choice(p)
    # f = open('cpmResponse.json', 'r', encoding="utf-8_sig")
    f = open(pt, 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)
    # resjson: bytes = json.dumps(jsn).encode("utf-8")
    # resjson: bytes = json.dumps({'message': 'putMethod'}).encode("utf-8")


# 返金 API
@apps.route("/gateway/api/v1/qr/refunds", methods=['PUT'])
def putReqRefund():
    '''
    Http Request Header 確認
    '''
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))

    payload = request.json
    print("Can You Get Json Params [refund_id]? " + payload.get('refund_id'))
    print("Can You Get Json Params [order_id]? " + payload.get('order_id'))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))
    print("Can You Get Json Params [fee]? " + str(payload.get('fee')))
    '''
    # windowsで動かす場合にテキストファイルをloadすると勝手に「cp932」でloadされてしまうらしい
      ので、open関数にencoding="utf-8_sig"を明示的に指定する
    '''
    p = ['refundPutR.json', 'refundPutR_F.json','refundPutR_P.json']
    pt = random.choice(p)
    # f = open('cpmResponse.json', 'r', encoding="utf-8_sig")
    f = open(pt, 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)


@apps.route("/gateway/api/v1/login", methods=['POST'])
def postAuthReq():
    params = request.json
    response = {}
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))

    payload = request.json
    print("Can You Get Json Params [loginId]? " + payload.get('loginId'))
    print("Can You Get Json Params [userPassword]? " + payload.get('userPassword'))
    print("Can You Get Json Params [osName]? " + payload.get('osName'))
    print("Can You Get Json Params [osVersion]? " + str(payload.get('osVersion')))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))

    f = open("authPut.json", 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)
    '''
    resjson: bytes = json.dumps({'message': 'postMethod'}).encode("utf-8")
    return make_response(resjson)
    '''


@apps.route("/portal/queryapi/v1/qr/ordersforpartner", methods=['POST'])
def postTradeReq():
    params = request.json
    response = {}
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-LAKALA-Time? " + headers.get('X-LAKALA-Time'))
    print("Can You See a X-LAKALA-NonceStr? " + headers.get('X-LAKALA-NonceStr'))
    print("Can You See a X-LAKALA-Sign? " + headers.get('X-LAKALA-Sign'))
    print("Can You See a X-LAKALA-loginId? " + headers.get('X-LAKALA-loginId'))
    print("Can You See a X-LAKALA-serialNo? " + headers.get('X-LAKALA-serialNo'))

    payload = request.json
    print("Can You Get Json Params [loginId]? " + payload.get('loginId'))
    print("Can You Get Json Params [userPassword]? " + payload.get('userPassword'))
    print("Can You Get Json Params [osName]? " + payload.get('osName'))
    print("Can You Get Json Params [osVersion]? " + str(payload.get('osVersion')))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))

    f = open("authPut.json", 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    resjson: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(resjson)


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # データ受信
        self.data = self.request.recv(1024)
        print("Receiving: " + self.data)


def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]
    start_response(status, headers)
    return [json.dumps({'message':'hoge'}).encode("utf-8")]


# 自身のIPアドレスを取得する
def getaddr():
    host = socket.gethostname()
    print("Host=: {}".format(host))

    ip = socket.gethostbyname_ex(host)[2]
    tp = ""
    for t in ip:
        tp = t
    '''
    for t in ip:
        print("Ip=: {}".format(t))
        if len(readjson(t)) > 0:
            tp = t
            break
    '''
    return tp


# Main Start
if __name__ == "__main__":
    print("Starting Main")
    addrs = getaddr()
    HOST, PORT = addrs, 3000
    print("ip address:{}".format(addrs))
    dPort = "80"
    apps.run(host=addrs, port=dPort)

    '''
    with make_server(HOST, PORT, app) as server:
        server.serve_forever()
    with socketserver.TCPServer((HOST, PORT), MyTcpHandler) as server:
        server.serve_forever()
    '''
