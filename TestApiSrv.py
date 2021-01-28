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
def get_cpm_req():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    # JSONファイルを読込んで還す
    p = ['cpmGetting.json', 'cpmGettingING.json', 'cpmGetErrorResponse.json']
    pt = random.choice(p)
    f = open(pt, 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    reason = json.dumps(jsn).encode("utf-8")
    return make_response(reason)


# 返金確認API
@apps.route("/gateway/api/v1/qr/checkrefunds", methods=['GET'])
def get_refund_req():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    # JSONファイルを読込んで還す
    p = ['refundGet.json', 'refundGetF.json', 'refundGetW.json']
    pt = random.choice(p)
    f = open(pt, 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    reasons: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(reasons)


# 取引照会(店舗単位)API
@apps.route("/gateway/api/v1/qr/orders", methods=['GET'])
def get_orders_req():
    params = request.args
    headers = request.headers
    # print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))
    for p in params:
        print("Can You See a RequestHeader? " + p)
    # JSONファイルを読込んで還す
    '''
    p = ['refundGet.json', 'refundGetF.json', 'refundGetW.json']
    pt = random.choice(p)
    '''
    f = open('ordersRes.json', 'r', encoding="utf-8_sig")
    # f = open('cpmGetting.json', 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    reasons: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(reasons)


# QRコード支払 API
@apps.route("/gateway/api/v1/qr/orders", methods=['PUT'])
def put_req_order():
    '''
    Http Request Header 確認
    '''
    headers = request.headers
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))

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
    p = ['cpmResponse.json', 'cpmResponseIng.json', 'cpmErrorResponse.json']
    pt = random.choice(p)
    # f = open('cpmResponse.json', 'r', encoding="utf-8_sig")
    f = open(pt, 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    res_json: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(res_json)


# 返金 API
@apps.route("/gateway/api/v1/qr/refunds", methods=['PUT'])
def put_req_refund():
    '''
    Http Request Header 確認
    '''
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))

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
    reasons: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(reasons)


@apps.route("/gateway/api/v1/login", methods=['POST'])
def post_auth_req():
    params = request.json
    response = {}
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))

    payload = request.json
    print("Can You Get Json Params [loginId]? " + payload.get('loginId'))
    print("Can You Get Json Params [userPassword]? " + payload.get('userPassword'))
    print("Can You Get Json Params [osName]? " + payload.get('osName'))
    print("Can You Get Json Params [osVersion]? " + str(payload.get('osVersion')))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))

    f = open("authPut.json", 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    reasons: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(reasons)


@apps.route("/portal/queryapi/v1/qr/ordersforpartner", methods=['POST'])
def post_trade_req():
    params = request.json
    response = {}
    headers = request.headers
    print("Can You See a Content-Type? " + headers.get('Content-Type'))
    '''
    Http Request Header 確認
    '''
    print("Can You See a X-GCP-Time? " + headers.get('X-GCP-Time'))
    print("Can You See a X-GCP-NonceStr? " + headers.get('X-GCP-NonceStr'))
    print("Can You See a X-GCPGCP-Sign? " + headers.get('X-GCPGCP-Sign'))
    print("Can You See a X-GCPGCP-loginId? " + headers.get('X-GCPGCP-loginId'))
    print("Can You See a X-GCPGCP-serialNo? " + headers.get('X-GCPGCP-serialNo'))

    payload = request.json
    print("Can You Get Json Params [loginId]? " + payload.get('loginId'))
    print("Can You Get Json Params [userPassword]? " + payload.get('userPassword'))
    print("Can You Get Json Params [osName]? " + payload.get('osName'))
    print("Can You Get Json Params [osVersion]? " + str(payload.get('osVersion')))
    print("Can You Get Json Params [serialNo]? " + payload.get('serialNo'))

    f = open("authPut.json", 'r', encoding="utf-8_sig")
    jsn = json.load(f)
    reasons: bytes = json.dumps(jsn).encode("utf-8")
    return make_response(reasons)


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
    return [json.dumps({'message': 'hoge'}).encode("utf-8")]


# 自身のIPアドレスを取得する
def getaddr():
    host = socket.gethostname()
    print("Host=: {}".format(host))

    ip = socket.gethostbyname_ex(host)[2]
    tp = ""
    for t in ip:
        tp = t
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
