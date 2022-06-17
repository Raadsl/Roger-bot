print('starting')
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import asyncio
from discord.utils import get
keep_alive()
os.system('clear')

tokend = os.environ['BOTTOKEN']
invitelink = 'https://discord.com/api/oauth2/authorize?client_id=983443133092225075&permissions=8&scope=bot%20applications.commands'
verbanwoord = ['@everyone', '@here', 'gay']
bot = commands.Bot(command_prefix='!')

#---------------------------------------------------------------EVENTS-------------------
#starten en status
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="Jou")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)  
    print("Bot is gestart")
    statuskan1 = bot.get_channel(984528725783748608)
    await statuskan1.send(':green_circle: De echte Roger is weer wakker')

#cooldown
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):  
        return await ctx.send('De command **{}** heeft nog een cooldown voor {:.2f} seconden'.format(ctx.command.name, error.retry_after))



#-----------------------commands-----------------------------
#ping cmd
@bot.command()
async def ping(ctx):
  """Pong"""
  await ctx.send(f'Pong! `{round (bot.latency * 1000)}` ms')
#say cmd


@bot.command()
async def guilds(ctx):
  for guild in bot.guilds:
    await ctx.send(guild.name)
@bot.command()
async def say(ctx, *, message):
  """Zeg iets wijs """
  if verbanwoord in message:
    await ctx.send("Goed geprobeerd" + ctx.message.author + 'dit bericht bevat iets verboden :)')
  else:
    try:
        await ctx.message.delete()
        await ctx.send(message)
        print(f'Ik zei {message}\nDoor {ctx.message.author}\n')
        f = open("rogertext.txt", "a")
        f.write(f"Door {ctx.message.author}, zei ik: '{message}'.\n")
        f.close()
    except:
        await ctx.send("Geef een bericht wat ik moet zeggen nerd")
#sudo
@bot.command()
async def sudo(ctx, member: discord.Member, *, message=None):
  """sudo jobbe"""
  await ctx.message.delete()
  webhooks = await ctx.channel.webhooks()
  for webhook in webhooks:
      await webhook.delete()
  webhook = await ctx.channel.create_webhook(name=member.name)
  await webhook.send(str(message),
                     username=member.name,
                     avatar_url=member.avatar_url)

#prenk
@bot.command()
async def sey(ctx, *, message):
  """random shit """
  try:
      await ctx.send('ROGER LUISTERD NAAR NIEMAND MUHAHAHAHHA')
  except:
      await ctx.send("Geef een bericht wat ik moet zeggen nerd")

#invite link
@bot.command()
async def invite(ctx):
  """Krijg de invite link voor deze alpha male """
  try:
      await ctx.send('De invite link voor roger de alpha male is')
      await ctx.send(invitelink)
  except:
      await ctx.send("Error")
      print('error met invite command')
@bot.command()
async def verwijder(ctx):
  """Daar doet Roger niet aan"""
  await ctx.send('ROGER VERWIJDERD GEEN BERICHTEN')
  await ctx.send('STOP ER NU MEE')
#dmplus
@bot.command()
@commands.is_owner()
@commands.cooldown(1, 60, commands.BucketType.user)
async def dmplus(ctx, user: discord.User, *, message=None):
  
  """DM een gebruiker als admin zonder dat er bij komt te staan wie hem heeft gestuurd """
  try:
      message = message or "Dit bericht is naar de DM gestuurt"
      await user.send(message) 
      await ctx.send('Ik heb hem gebamboozled')
  except:
     await ctx.send('er is een error. Gebruik !DM @user bericht')
     await ctx.send('Als dit nogsteeds niet werkt, DM Raadsel#9398')

#dm
@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def dm(ctx, user: discord.User, *, message=None):
  
  """DM een gebruiker """
  try:
      message = message or "Dit bericht is naar de DM gestuurt"
      await user.send(message) 
      await user.send(f'Gestuurd door: {ctx.message.author}') 
      await ctx.send('Ik heb hem gebamboozled')
  except:
     await ctx.send('er is een error. Gebruik !DM @user bericht')
     await ctx.send('Als dit nogsteeds niet werkt, DM Raadsel#9398')

#roger god
@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)  #of guild ipv user
async def roger(ctx):
  """Roger de alpha male"""
  await ctx.message.delete()
  await ctx.send('https://tenor.com/view/fight-gif-22871285')
  await ctx.send('Roger is voor niemand bang')
  await ctx.send('||En Je spreekt het uit als Rodjer. Niet rooger Maar Rodjer.||')

#owner cmds----------------------------
  #zet bot off
@bot.command()
@commands.is_owner()
async def slaap(ctx):
  """zet de bot uit """
  await ctx.send('Dankjewel Raadsel. Ik ga nu slapen. Joejoe')
  statuskan2 = bot.get_channel(983805261535916032)
  await statuskan2.send(':red_circle: Roger gaat een dutje doen')
  await ctx.bot.logout()
# test cooldown
@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def test(ctx, command=None):
  """ test command """
  if command is None:
      await ctx.send('a')  
  elif command.lower() == '2':
      await ctx.send('b')

#snipe command
snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command(name = 'snipe')
async def snipe(ctx):
  """Laat het laatst verwijderde bericht in een kanaal zien"""
  channel = ctx.channel
  try: 
      em = discord.Embed(name = f"Laatste verwijderde bericht in #{channel.name}", description = snipe_message_content[channel.id])
      em.set_footer(text = f"Dit bericht was verstuurd door {snipe_message_author[channel.id]}")
      await ctx.send(embed = em)
  except KeyError: 
      await ctx.send(f"Er zijn geen recent verwijderde berichten in #{channel.name} Joepie!")

#@bot.event
#async def on_message(message):
#    msg = message
#    with open("alle berichten.txt", "a") as n:
#      n.write("\n" + "Tijd: " + str(msg.created_at) + "| " + str(msg.author.id) #+ " | <" + str(msg.author) + "> : \n" + msg.content)
#      n.close()
#
  
bot.run(tokend)
