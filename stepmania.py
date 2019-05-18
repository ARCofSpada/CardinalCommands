import aiohttp
import discord
from discord.ext import commands
import json
import subprocess
from bs4 import BeautifulSoup

class StepMania:
	def __init__(self, bot):
		with open("data/LuaDocumentation.xml") as file_read:
			soup = BeautifulSoup(file_read.read(), features="xml")
			self.smFunctions = soup.find_all("Function")
			
		self.bot = bot
		
	@commands.command()
	async def smfunction(self, arg):
		#soup.Documentation.GlobalFunctions
		for func in self.smFunctions:
			if func['name'] == arg:
				msg= func['return'] + " " + func['name'] + "("+func['arguments']+")\n"
				msg += "".join(str(item) for item in func.contents).strip().replace("<code>","`").replace("</code>","`")
				await self.bot.say(msg)
				return
		await self.bot.say("Couldn't find that function.")

def setup(bot):
	bot.add_cog(StepMania(bot))
