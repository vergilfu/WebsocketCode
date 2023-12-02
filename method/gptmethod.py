import openai, jsonpath, json, asyncio, time,asyncio,logging

async def sendmsg(webmsg,websocket):
    question = webmsg['question']
    model = webmsg['model']
    with open('./configjson.json', encoding='utf-8') as f:
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
    tem = ''
    for reply in response:
        content = jsonpath.jsonpath(reply, "$..content")
        if content:
            if len(tem)<5:
                tem += content[0]
            else:
                tem += content[0]
                await websocket.send(tem)
                await asyncio.sleep(0.3)
                tem = ''
    await websocket.send(tem)
    await asyncio.sleep(0.3)



