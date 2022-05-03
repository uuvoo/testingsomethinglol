credits="""
  _           _       _              
 | |         | |     | |             
 | |__   __ _| | ___ | |_ __ _ _ __  
 | '_ \ / _` | |/ _ \| __/ _` | '_ \ 
 | | | | (_| | | (_) | || (_| | | | |
 |_| |_|\__,_|_|\___/ \__\__,_|_| |_|
                                     
                                      
Top Bot
Made by 0halotan#4400
"""







#ACCOUNT FILE NAMES NEED TO BE LOWERCASED
print(credits)
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot Running!")
@bot.command() # Stock command
async def stock(ctx):
    stockmenu = discord.Embed(title="Cuentas en stock",description="") # Define the embed
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: # Open every file in the accounts folder
            ammount = len(f.read().splitlines()) # Get the ammount of lines
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") #Make the name look nice
            stockmenu.description += f"*{name}* - {ammount}\n" # Add to the embed
    await ctx.send(embed=stockmenu) # Send the embed



@bot.command() #Gen command
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("especifica que cuenta quieres") # Say error if no name specified
    else:
        name = name.lower()+".txt" #Add the .txt ext
        if name not in os.listdir("Accounts"): # If the name not in the directory
            await ctx.send(f"Que carajos intentas? `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() #Read the lines in the file
            if len(lines) == 0: # If the file is empty
                await ctx.send("Se acabo el stock de este generador") #Send error if lines = 0
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines) # Get a random line
                try: #Try to send the account to the sender
                    await ctx.author.send(f"`{str(account)}`\n\nHecho por 0halotan#4400",delete_after=delete)
                except: # If it failed send a message in the chat
                    await ctx.send("Error al inviar la cuenta (Activate para recibir mensajes directos)")
                else: # If it sent the account, say so then remove the account from the file
                    await ctx.send("Cuenta enviada a tu dm")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") #Clear the file
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: #Add the lines back
                            if line != account: #Dont add the account back to the file
                                file.write(line+"\n") # Add other lines to file
bot.run(token)