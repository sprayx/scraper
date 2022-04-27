import discum, time 
token = "" #token da conta 
guild_id = '' # id do servidor
channel_id = '' #id do canal
bot = discum.Client(token= token, log=True)
bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()
bot.gateway.run()
def __get_badges(flags) -> list[str]:
    
        BADGES = {
            1 << 1:  'Dono de Servidor Partner',
            1 << 2:  'HypeSquad Events',
            1 << 3:  'Bug Hunter Level 1',
            1 << 9:  'Apoiador Inicial',
            1 << 10: 'Team User',
            1 << 12: 'System',
            1 << 14: 'Bug Hunter Level 2',
            1 << 17: 'Developer',
            1 << 18: 'Moderador do Discord'
        }
        badges = []
        for badge_flag, badge_name in BADGES.items():
            if flags & badge_flag == badge_flag:
                badges.append(badge_name)
        return badges
with open('results.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badges(temp)
            if len(z) != 0:
                badges = ', '.join(z)
                print(f'discord.com/users/{id} | {username} | {badges}')
                file.write(f'{id}\n')
