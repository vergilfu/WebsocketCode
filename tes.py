#_*_coding:utf-8_*_
#!/usr/bin/env python
#Author:Vergil_Fu

import asyncio

async def outer_coroutine():
    print("外部协程开始")
    await inner_coroutine()
    print("外部协程结束")

async def inner_coroutine():
    print("内部协程开始")
    for i in range(10):
        print(i)
        await asyncio.sleep(1)
    print("内部协程结束")



# 创建事件循环并运行外部协程
loop = asyncio.get_event_loop()
loop.run_until_complete(outer_coroutine())