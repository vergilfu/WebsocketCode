import openai, jsonpath, json, asyncio, time

async def sendAnswer(data,websocket):
    chunk_message = jsonpath.jsonpath(data, "$..content")[0]  # extract the message
    print(chunk_message)
    await websocket.send(chunk_message)

def getanswer(data,websocket):
    with open('configjson.json', encoding='utf-8') as f:
        configs = json.load(f)
    openai.api_base = configs['openai.api_base']
    openai.api_key = configs['openai.api_key']
    question = data

    start_time = time.time()
    response = openai.ChatCompletion.create(
        model='gpt-4-32k',
        messages=[
            {'role': 'user', 'content': question}
        ],
        temperature=0,
        stream=True  # again, we set stream=True
    )

    for chunk in response:
        if jsonpath.jsonpath(chunk, "$..content"):
            finish_reason = chunk["choices"][0]["finish_reason"]

            if "content" in chunk["choices"][0]["delta"]:
                # 创建事件循环
                loop = asyncio.get_event_loop()
                # 调用异步函数
                loop.run_until_complete(sendAnswer(chunk,websocket))


            elif finish_reason:
                return 'done'
