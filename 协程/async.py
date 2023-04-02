import asyncio
import datetime

async def my_coroutine(name):
    print(f'{name} coroutine started')
    await asyncio.sleep(1)
    print(f'{name} coroutine finished')

async def main():
    tasks = []
    for i in range(3):
        task = asyncio.create_task(my_coroutine(f'Coroutine-{i}'))
        tasks.append(task)
    await asyncio.gather(*tasks)

now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
print("当前时间是:", time_str)
asyncio.run(main())
now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
print("结束时间是:", time_str)







