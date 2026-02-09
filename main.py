#------------------------Outer_libs------------------------
import asyncio
from aiogram import Bot, Dispatcher, Router
from routers import register_handlers
#---------------------------------------------------------⯾


#------------------------Inner_libs-------------------------
from config import API_KEY
#----------------------------------------------------------⯾


bot = Bot(token = API_KEY)
dp = Dispatcher()
router = Router()
dp.include_router(router)
register_handlers(router)


#-----------------------Initialization-----------------------
async def main():
    print('bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
#----------------------------------------------------------⯾