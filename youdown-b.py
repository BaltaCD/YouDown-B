from pytube import YouTube
from tqdm import tqdm

loop = tqdm(total = 30000, position=0, leave=False)
for k in range(30000):
    loop.set_description('Abriendo scrip'.format(k))
    loop.update(1)
loop.close()

RED = '\033[31m'
WHITE = '\033[37m'

print("\n\n◈ ━━━━━━━━━━ ◆ ━━━━━━━━━━ ◈")
print(RED+ "╔═╦╗   ╔══╗          ╔══╗")
print("╚╗║╠═╦╦╬╗╗╠═╦╦╦╦═╦╦══╣╔╗║")
print("╔╩╗║╬║║╠╩╝║╬║║║║║║╠══╣╔╗║")
print("╚══╩═╩═╩══╩═╩══╩╩═╝  ╚══╝")

print("-Programado por:", WHITE+"Balta")
print(RED+"-Contacto:", WHITE+ "baltaprogramadorniu05@gmail")

url = input(RED+"\nIntroduzca la URL del Video: ")

print(WHITE+ "(･ิᴗ･ิ)", RED+"\nDescargando...")
# YouTube(url).streams.get_by_resolution()
# YouTube(url).streams.first().download()
YouTube(url).streams.get_highest_resolution().download()
# YouTube(url).streams.get_audio_only()
print(WHITE+"( ^-^)/", RED+"\n¡Su video se ha descargado satisfactoriamente!")


