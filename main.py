import asyncio
import socket

async def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        await asyncio.to_thread(s.connect, (ip, port))
        s.send(b'Connect')
        s.close()
        print(f'[Port] Opened {port}')
        return port
    except Exception:
        return None

async def runAsync():
    opens = await asyncio.gather(*[check_port('ip', i) for i in range(1, 65536)])
    opens = [i for i in opens if i != None]
    print(f'Opened Ports: {opens}')

asyncio.run(runAsync())
