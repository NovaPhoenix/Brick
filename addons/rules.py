#!/usr/bin/env python3.6

import discord
from discord.ext import commands

class Rules:
    """
    Follow teh rules
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    @commands.command(hidden=True)
    async def r1(self, ctx):
        return await ctx.send("Rule 1: Being an asshole is okay, but know when to stop.")

    @commands.command(hidden=True)
    async def r2(self, ctx):
        return await ctx.send("Rule 2: No doxing or harassment, either of these will result in an immediate ban.")

    @commands.command(hidden=True)
    async def r3(self, ctx):
        return await ctx.send("Rule 3: Spamming is only allowed in the dedicated spam channel, <#355713947548123137>, however, automation of the aforementioned spam is not allowed.")

    @commands.command(hidden=True)
    async def r4(self, ctx):
        return await ctx.send("Rule 4: Keep NSFW content to #nsfw. You can gain access to it by using the command `.togglechannel nsfw`")

    @commands.command(hidden=True)
    async def r5(self, ctx):
        return await ctx.send("Rule 5: Ask a staff member before posting invite links to things like servers on Discord, Skype groups, etc.")

    @commands.command(hidden=True)
    async def r6(self, ctx):
        return await ctx.send("Rule 6: Content pertaining to discussion in the voice channels and excessive or random bot commands should be kept to #voice-and-bot-cmds")

    @commands.command(hidden=True)
    async def r7(self, ctx):
        return await ctx.send("Rule 7: Alternate accounts are only allowed with the explicit permission of a staff member.")

    @commands.command(hidden=True)
    async def r8(self, ctx):
        return await ctx.send("Rule 8: Trying to evade, look for loopholes, or stay borderline within the rules will be treated as breaking them.")

        


def setup(bot):
    bot.add_cog(Rules(bot))
