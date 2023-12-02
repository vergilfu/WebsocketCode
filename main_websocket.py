# import sys
# sys.path.append('C:/Users/pc/AppData/Local/Programs/Python/Python312/Lib/site-packages')
import asyncio, websockets, logging, json, openai, jsonpath, ssl
from method import logsetter,gptmethod

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('./method/cert.pem', './method/key.pem')

async def echo(websocket, path):
    async for webmsg in websocket:
        webmsg = json.loads(webmsg)
        method = webmsg['method']
        if method == 'chat':
            await gptmethod.sendmsg(webmsg,websocket)
        elif method == 'audio':
            audiofile = webmsg['audiofile']




logsetter.logsetter()
logging.info('websocket服务启动成功')
start_server = websockets.serve(echo, "0.0.0.0", 8090)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
