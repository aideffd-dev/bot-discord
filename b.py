from datetime import timedelta
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands 
import random 
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
lista = os.listdir('images/')
videos = ["https://www.youtube.com/watch?v=sfa-jnXtA84", "https://www.youtube.com/watch?v=ULqLyZglrj0", "https://www.youtube.com/watch?v=hvduGD9cPps", "https://www.youtube.com/watch?v=52pfRQawboA", "https://www.youtube.com/watch?v=1zJd9xcYl_o", "https://www.youtube.com/watch?v=UuOzQbBMm08", "https://www.youtube.com/watch?v=Vr4sNnyNxSU", "https://www.youtube.com/watch?v=8k3wlLBRWSI", "https://www.youtube.com/watch?v=WA_Z003LJNQ"]
@bot.event
async def on_ready():
    print("Bot online!")

    canais = bot.get_all_channels()

    for canal in canais:
        print(canal.name, canal.id)
    canal = await bot.fetch_channel(1482330498700152854)
    await canal.send("oiii, eu sou um bot orientador de cuidados com o lixo da sua casa, para que você e outros agentes externos n passem por incovenientes por causa do lixo mal colcado! Digite $ajuda para saber mais sobre mim e o que eu posso fazer por você!")

@bot.command()
async def youtube(ctx):
    await ctx.send(random.choice(videos))

@bot.command()
async def ajuda(ctx):
    await ctx.send("$acumulo(dicas para acumular o lixo de forma correta), $charge(charges de conscientização para o cuidadoo com o lixo), $youtube(vídeos de conscientização/informação sobre o cuidado com o lixo), $tempo(tempo ideal para acumular o lixo), $reciclagem(dicas para reciclar o lixo de forma correta), $saco(dicas para escolher o melhor saco de lixo)")

@bot.command()
async def acumulo(ctx):
    await ctx.send("a melhor forma de acumular o lixo é colocando latas de lixo em pontos estrátegicos da sua casa, com sacolas dentro ")

@bot.command()
async def charge(ctx):

    img = random.choice(lista)

    with open('images/' + img, 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def tempo(ctx):
    await ctx.send("O tempo ideal para acumular o lixo é de no máximo 3 dias, para evitar o mau cheiro e a proliferação de insetos e bactérias, além de evitar que o lixo se torne um ambiente propício para a reprodução de roedores e outros animais indesejados. É importante lembrar que o lixo deve ser descartado de forma adequada, seguindo as normas de coleta seletiva e separação de resíduos, para minimizar os impactos ambientais e promover a sustentabilidade.")

@bot.command()
async def reciclagem(ctx):
    await ctx.send("A reciclagem é um processo importante para reduzir a quantidade de resíduos que vão para os aterros sanitários e para preservar os recursos naturais. Para reciclar corretamente, é importante separar os materiais recicláveis dos não recicláveis, como papel, plástico, vidro e metal. Além disso, é importante limpar os materiais recicláveis antes de descartá-los, para evitar contaminação e facilitar o processo de reciclagem. Lembre-se de seguir as normas de coleta seletiva da sua região e de incentivar outras pessoas a fazerem o mesmo, para promover um ambiente mais sustentável e saudável para todos.")

@bot.command()
async def saco(ctx):
    await ctx.send("o melhor tipo de saco para se colocar todo lixo acumulado é o classico saco de lixo preto, pois sua escolha de desing tem a função de manter sua privacidade em realação ao seu lixo, que em público pode revelar muito de você, em termos de qualidade, o que mais tem que ser destacado em sua compra é a durabilidade do produto, a falta disso é o que mais pode lhe gerar problemas, e quanto tamanho isso já pode derivar de você, veja e compre o que achar melhor")

bot.run(TOKEN)
