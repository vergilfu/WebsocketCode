# _*_coding:utf-8_*_
# !/usr/bin/env python
# Author:Vergil_Fu
import asyncio, websockets, logging, json, openai, jsonpath
import logsetter


async def echo(websocket, path):
    async for question in websocket:
        logging.info(str('用户提问：' + question))
        with open('configjson.json', encoding='utf-8') as f:
            configs = json.load(f)
        openai.api_base = configs['openai.api_base']
        openai.api_key = configs['openai.api_key']
        response = openai.ChatCompletion.create(
            model='gpt-4-32k',
            messages=[
                {'role': 'user', 'content': question}
            ],
            temperature=0,
            stream=True  # again, we set stream=True
        )
        tem = ''
        for reply in response:
            if jsonpath.jsonpath(reply, "$..content"):
                logging.info(jsonpath.jsonpath(reply, "$..content")[0])
                tem+= jsonpath.jsonpath(reply, "$..content")[0]
                await websocket.send(jsonpath.jsonpath(reply, "$..content")[0])
        logging.info(tem)


logsetter.logsetter()
logging.info('websocket服务启动成功')
start_server = websockets.serve(echo, "172.20.200.121", 8090)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
