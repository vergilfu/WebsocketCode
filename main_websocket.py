#_*_coding:utf-8_*_
#!/usr/bin/env python
#Author:Vergil_Fu
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)
print('websocket服务启动成功')
start_server = websockets.serve(echo, "localhost", 8090)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()