import asyncio
from websockets.asyncio.server import serve

async def hello(websocket):
    name = await websocket.recv()
    print("name - ",name)

    greeting = "hello" + name

    await websocket.send(greeting)
    print("greeting - ", greeting)

async def main():
    async with serve(hello , "localhost" , ) as server:
            await server.serve_forever()

if __name__=="__main__":
     asyncio.run(main())
