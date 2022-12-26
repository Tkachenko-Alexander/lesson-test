    from aiogram import Bot, Dispatcher, executor, types
    import python_weather


    #bot init
    bot = Bot(token="")
    dp = Dispatcher(bot)
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # echo
    @dp.message_handler()
    async def echo(message: types.Message):
        weather = await client.get(message.text)
        celsius = round((weather.current.temperature - 32) / 1.8)

        resp_msg = f"Текущая температура: {celsius}°"

        if celsius <= 10:
            resp_msg += "\n\nПрохладно! Одевайтесь потеплее!"
        else:
            resp_msg += "\n\nТепло! Одевайтесь полегче!"

        await message.answer(resp_msg)

    # run long-polling
    if __name__ == "__mail__":
        executor.start_polling(dp, skip_updates=True)
