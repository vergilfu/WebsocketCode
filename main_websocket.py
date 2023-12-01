import asyncio, websockets, logging, json, openai, jsonpath,time,ssl
import logsetter

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('./cert.pem', './key.pem')

async def echo(websocket, path):
    async for webmsg in websocket:
        method = webmsg['method']
        if method == 'chat':
            logging.info('用户提问：'+str(webmsg))
            question = webmsg['question']
            model = webmsg['model']
            with open('configjson.json', encoding='utf-8') as f:
                configs = json.load(f)
            openai.api_base = configs['openai.api_base']
            openai.api_key = configs['openai.api_key']

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {'role': 'user', 'content': question}
                ],
                stream=True  # again, we set stream=True
            )
            await sendmsg(response,websocket)
        elif method == 'audio':
            audiofile = webmsg['audiofile']
            logging.info(audiofile)

async def sendmsg(response,websocket):
    tem = ''
    for reply in response:
        content = jsonpath.jsonpath(reply, "$..content")
        if content:
            if len(tem)<5:
                tem += content[0]
            else:
                tem += content[0]
                logging.info(tem)
                await websocket.send(tem)
                await asyncio.sleep(0.3)
                tem = ''
    await websocket.send(tem)
    await asyncio.sleep(0.3)


logsetter.logsetter()
logging.info('websocket服务启动成功')
start_server = websockets.serve(echo, "0.0.0.0", 8090,ssl=ssl_context)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
