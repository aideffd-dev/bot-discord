import discord
from discord.ext import commands
import random
receitas_bolo = ["Para fazer um bolo de chocolate, você vai precisar de ovos, açúcar, farinha de trigo, chocolate em pó, leite, manteiga ou margarina e fermento em pó. Em uma tigela, coloque os ovos, o açúcar e a manteiga e misture bem até formar um creme. Depois acrescente o leite e o chocolate em pó e continue mexendo até ficar bem misturado. Em seguida, adicione a farinha de trigo aos poucos, mexendo até a massa ficar homogênea. Por último, coloque o fermento e misture delicadamente. Depois disso, unte uma forma com manteiga e um pouco de farinha e despeje a massa na forma. Leve ao forno preaquecido a 180 °C e deixe assar por cerca de 35 a 40 minutos. Para verificar se o bolo está pronto, espete um palito no meio do bolo; se ele sair limpo, o bolo já pode ser retirado do forno. Deixe esfriar um pouco antes de desenformar e servir.", "Para fazer um bolo de cenoura, você vai precisar de cenouras, ovos, açúcar, óleo, farinha de trigo e fermento em pó. Primeiro, corte as cenouras em pedaços e coloque no liquidificador junto com os ovos, o açúcar e o óleo. Bata até formar uma mistura bem lisa. Depois despeje essa mistura em uma tigela e acrescente a farinha de trigo aos poucos, mexendo bem até a massa ficar homogênea. Por último, adicione o fermento em pó e misture delicadamente. Em seguida, unte uma forma com manteiga e farinha e despeje a massa nela. Leve ao forno preaquecido a 180 °C e deixe assar por cerca de 35 a 40 minutos. Para saber se o bolo está pronto, espete um palito no centro; se ele sair limpo, o bolo pode ser retirado do forno. Depois deixe esfriar um pouco, desenforme e o bolo de cenoura estará pronto para servir.", "Para fazer um bolo de banana, você vai precisar de bananas maduras, ovos, açúcar, óleo ou manteiga, farinha de trigo e fermento em pó. Primeiro, amasse bem as bananas em uma tigela. Depois acrescente os ovos, o açúcar e o óleo e misture bem até formar uma massa cremosa. Em seguida, adicione a farinha de trigo aos poucos, mexendo até a mistura ficar homogênea. Por último, coloque o fermento em pó e misture delicadamente. Depois disso, unte uma forma com manteiga e um pouco de farinha e despeje a massa nela. Leve ao forno preaquecido a 180 °C e deixe assar por cerca de 35 a 40 minutos. Para verificar se o bolo está pronto, espete um palito no centro; se ele sair limpo, o bolo pode ser retirado do forno. Deixe esfriar um pouco antes de desenformar e servir.", "Para fazer um bolo de fubá, você vai precisar de ovos, açúcar, óleo ou manteiga, leite, fubá, farinha de trigo e fermento em pó. Primeiro, em uma tigela, coloque os ovos, o açúcar e o óleo e misture bem até formar um creme. Depois acrescente o leite e o fubá e mexa até ficar bem misturado. Em seguida, adicione a farinha de trigo aos poucos, mexendo até a massa ficar homogênea. Por último, coloque o fermento em pó e misture delicadamente. Depois disso, unte uma forma com manteiga e um pouco de farinha e despeje a massa nela. Leve ao forno preaquecido a 180 °C e deixe assar por cerca de 35 a 40 minutos. Para verificar se o bolo está pronto, espete um palito no centro; se ele sair limpo, o bolo pode ser retirado do forno. Deixe esfriar um pouco antes de desenformar e servir."]
jogos = ["lol", "csgo", "minecraft", "valorant", "fortnite", "amongus", "roblox", "gta5", "apexlegends", "overwatch", "league of legends", "call of duty", "fifa", "pes", "pubg", "rust", "ark survival evolved", "the sims 4", "fall guys", "rocket league", "dota 2", "world of warcraft", "diablo 3", "starcraft 2", "hearthstone", "overcooked 2", "dead by daylight", "phasmophobia", "left 4 dead 2", "terraria", "stardew valley", "hollow knight", "celeste", "undertale", "hades", "slay the spire", "dark souls 3", "bloodborne", "the witcher 3", "red dead redemption 2", "cyberpunk 2077", "assassin's creed valhalla", "ghost of tsushima", "resident evil village", "final fantasy vii remake", "persona 5 royal", "the legend of zelda: breath of the wild", "super mario odyssey", "animal crossing: new horizons", "splatoon 2", "mario kart 8 deluxe", "super smash bros. ultimate"]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
#sugestão de jogo de computador pra jogar
@bot.command()
async def jogo(ctx):
    await ctx.send(f'Que tal jogar {random.choice(jogos)}?')

@bot.command()
async def bolochocolate(ctx):
    await ctx.send(receitas_bolo[0])

@bot.command()
async def bolocenoura(ctx):
    await ctx.send(receitas_bolo[1])

@bot.command()
async def bolobanana(ctx):
    await ctx.send(receitas_bolo[2])

@bot.command()
async def bolofuba(ctx):
    await ctx.send(receitas_bolo[3])

@bot.command()
async def clear(ctx, quantidade: int):

    cargo_permitido = "$Clear"

    if any(role.name == cargo_permitido for role in ctx.author.roles):

        await ctx.channel.purge(limit=quantidade)
        await ctx.send(f"{quantidade} mensagens apagadas.", delete_after=3)

    else:
        await ctx.send("Você não tem o cargo necessário", delete_after=3)
#comando para novos membros conhecerem o servidor
@bot.event
async def on_member_join(member):

    canal = member.guild.system_channel

    if canal:
        await canal.send(f"Bem-vindo ao servidor, {member.mention}! clique na aba #rules para ter ciência das regras do server e entre em contato com o adm kodl para mais informações")



bot.run("meu_token")
