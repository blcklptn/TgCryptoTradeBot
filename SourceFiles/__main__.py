from dispatcher import *
from frontend.handlers import public
import asyncio

async def main():
    print('Bot started!')
    dp.include_router(public.router)
    #dp.include_router(admin.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())