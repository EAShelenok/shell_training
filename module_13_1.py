import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i + 1} шар.')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Минимус', 3))
    task_2 = asyncio.create_task(start_strongman('Средниус', 4))
    task_3 = asyncio.create_task(start_strongman('Максимус',10))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())