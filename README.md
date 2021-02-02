# WebApi
QR決済テスト用WebApi
開発検証およびテスト用API(Python3.8～)
【実行環境】
windows10
python3.8～(開発環境は3.8)
※実行環境はwindows10を想定しています。他のOSで実行する場合はutfへのエンコードで相違が出る場合があります。

【プログラム概要】
ローカルPC上でHttpApiサーバーを実行します。
ポートはデフォルトで80
その他のポートを割り当てたい場合は指定ができます。

pythonのapi用フレームワークはflaskを使用(難しい処理は不要なので簡単、軽量なものを選択)
※Djangoだとやりすぎ

クライアント側からは「http://192.168.xxx.xxx」でPOST,GET,PUTメソッドアクセスが可能
ただし、接続ポートを80番以外のものを指定した場合はポート指定必須
「http://192.168.xxx.xxx:0000」とこんな感じ

APIアクセスURL一覧
ユーザー認証
/gateway/api/v1/login
QRコード支払(CPM)
/gateway/api/v1/qr/orders
支払結果確認
/gateway/api/v1/qr/checkorder
返金
/gateway/api/v1/qr/refunds
返金結果確認
/gateway/api/v1/qr/checkrefunds
取引記録照会(店舗単位)
/gateway/api/v1/qr/orders
取引記録照会(企業単位)
/portal/queryapi/v1/qr/ordersforpartner

【簡単な仕様】
各メソッドのリターン値を設定したJSONファイルをプロジェクト内に用意
支払APIの場合だと
「cpmResponse.json(正常), cpmResponseIng.json(処理中), cpmErrorResponse.json(エラー)」
それらをランダムに読込、リターンさせて本体モジュールの挙動を確認している。
なお項目値は仕様上の相違がない程度のものなので実際値とは異なる。(スタブ形式)

ベンダーからリターン値サンプルが貰えればそれをあてることで
よりリアルな挙動を確認出来るのだが…な