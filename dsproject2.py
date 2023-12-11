import aiohttp
import asyncio
import sqlite3
from datetime import datetime

#creating an async functions that waits for a minute before executing the rest of the code
async def wait():
    print("Waiting for one minute...")
    await asyncio.sleep(60)
    print("One minute has passed, now executing the code.")

#An async function that pulls from the given api
async def getData():
    api_url = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(api_url) as response:
            data = await response.json()
            return data

#creating a function that takes the data from the api and puts it into a database
async def assertData(cursor, data):
# creating a database if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY,
            factor INTEGER,
            pi REAL,
            time TEXT
        )
    ''')

# dumping the data into an existing table
    cursor.execute('INSERT INTO api_data (factor, pi, time) VALUES (?, ?, ?)',
                   (data['factor'], data['pi'], data['time']))

#creating main that call the previous functions and have it run for the full hour
async def main():
    connect = sqlite3.connect('api_data.db')
    db = connect.cursor()
    for _ in range(60):
        await wait()
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        data = await getData()
        await assertData(db, {**data, 'time': now})
        connect.commit()
    connect.close()

# executing the main
if __name__ == "__main__":
    asyncio.run(main())