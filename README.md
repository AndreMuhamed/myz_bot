Цей код створює Discord-бота, який може приєднуватися до голосового каналу, відтворювати музику з YouTube та Spotify та від'єднуватися від каналу. пыпцрпркцрцркцркцркцркц

Він використовує бібліотеки discord, discord.ext.commands, spotipy та youtube_dl. 
Бот має три команди:

`join` - команда, що дозволяє боту приєднатися до голосового каналу, в якому перебуває користувач, який відправляє команду.

`leave` - команда, що дозволяє боту від'єднатися від голосового каналу, в якому він перебуває.

`play` - команда, що дозволяє боту відтворювати музику за URL-адресою, яку користувач передає як аргумент команди. Бот може відтворювати музику як з YouTube, так і з Spotify. 

Якщо переданий URL-адреса належить до Spotify, бот користується бібліотекою Spotipy для отримання прев'ю-файлу трека, який потім відтворюється. Якщо ж переданий URL-адреса належить до YouTube, бот використовує бібліотеку youtube_dl для отримання аудіофайлу за цим URL-адресою. Після відтворення музики бот відправляє повідомлення з назвою треку до текстового каналу.

# I am not responsible for the functionality of the bot
