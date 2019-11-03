## run project
pip install -r requirements.txt   
python sanic_server.py
#### 通过url 重写达到破解limneos 插件(指纹保护,通话录音,callbarxs等)
http://limneos.net http://localhost:8037/hello header 

#### 将ssr/ss订阅写进requests请求,通过base64解析出相关配置,通过text 返回surge需要等list文件


## 新加API 将 ss订阅转成surge list文件
http://118.24.42.159:8037/rixcloud/list?url=订阅链接
