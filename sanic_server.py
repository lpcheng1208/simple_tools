import base64
import requests
from sanic import Sanic
from sanic.response import html, text, redirect

app = Sanic(__name__)


def fill_padding(text):
    need_padding = len(text) % 4 != 0
    if need_padding:
        need_count = 4 - need_padding
        text += '='*need_count
    return text

def base64_decode(text):
    text = fill_padding(text)
    return base64.urlsafe_b64decode(text).decode("utf-8")

@app.route('/hello/ping.php', methods=['GET'])
async def lim_ping(request):
    return text("1")


@app.route('/hello', methods=['GET'])
async def lim_buy(request):

    return text("1")

@app.route('/hello/buy.php', methods=['GET'])
async def lim_buy(request):
    return text("1")


@app.route('/rixcloud/list', methods=['GET'])
async def ssrlink_to_surge(request):
    '''
    通过 ssr 或者 ss 链接转surge list 配置
    '''
    r = requests.get("ss/ssr 订阅链接")
    res = r.text
    ssr_list = base64_decode(res).split("\n")
    ssr_text_ = ""
    for ssr_text in ssr_list:
        if ssr_text.startswith("ssr://"):
            text_ = ssr_text[6:]
        elif ssr_text.startswith("ss://"):
            text_ = ssr_text[5:]
        else:
            continue
        parse_text = base64_decode(text_)
        parts = parse_text.split(":")
        server_ip = parts[0]
        server_port = parts[1]
        protocl = parts[2]
        onfs = parts[4]
        method = parts[3]
        passwd_and_params = parts[5].split("/?")
        passwd = base64_decode(passwd_and_params[0])
        params = passwd_and_params[1].split("&")
        param_dict = {}
        for param in params:
            temp = param.split("=")
            param_dict[temp[0]] = base64_decode(temp[1])

        # print("ip: %s port %s passwd %s 协议 %s 加密方法 %s 混淆 %s 混淆参数 %s 协议参数 %s 备注 %s 分组 %s"
        #       % (server_ip, server_port, passwd, protocl, method, onfs, param_dict["obfsparam"], "", param_dict["remarks"], param_dict["group"]))
        ssr_text_ += "%s = ss, %s, %s, encrypt-method=%s, password=%s, tfo=true\n" % (param_dict["remarks"], server_ip, server_port, method, passwd)

    return text(ssr_text_)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8037, debug=False, workers=1, access_log=False)
