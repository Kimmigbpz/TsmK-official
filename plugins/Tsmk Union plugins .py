# -*- coding: utf-8 -*-
# made by GBPZkimmi
# v1.4 2022/8/2
PLUGIN_METADATA = {
    'id': 'GB Union plugins',
    'version': '0.1.3',
    'name': 'GB Union plugins',
    'link': 'https://github.com/Kimmigbpz/Union-plugins'
}
    
def on_info(server,info):
    
    if info.is_player:
        if info.content.split == '!!dim':
            server.say('!!dim true 开启服务器超线程优化\n!!dim false 关闭服务器超线程优化')
        elif info.content.split == '!!dim true':
            server.execute('gamerule dimthread_active true')
            server.say('多线程优化已开启')
        elif info.content.split == '!!dim false':
            server.execute('gamerule dimthread_active false')
            server.say('多线程优化已关闭')
        elif info.content == '!!ban':
            server.say('NAN')
        elif info.content == '!!pardon':
            server.say('NAN')
        elif info.content == '!!mcdr lvl':
            server.say("玩家：" + info.player + "您的MCDR等级是" + str(server.get_permission_level(info.player)))
            if server.get_permission_level(info.player) == 0:
                server.say("等级0为guest，属服务器参观者，可以进行所有基本操作，但无法进行任何特殊操作")
            elif server.get_permission_level(info.player) == 1:
                server.say("等级1为player，属服务器成员，可以进行所有基本操作，以及一些特殊操作")    
            elif server.get_permission_level(info.player) == 2:
                server.say("等级2为helper，属服务器重要成员，可以进行一些关键指令操作")
            elif server.get_permission_level(info.player) == 3:
                server.say("等级3为admin，属服务器管理员，可以进行所有插件与指令操作，但不会破坏游戏平衡")
            elif server.get_permission_level(info.player) == 4:
                server.say("等级4为owner，属服务器所有者，可以进行所有插件与指令操作与调试，但不会破坏游戏平衡")
        elif info.content.startswith('!!head'):
                name = info.content.split()
                server.execute('give ' + info.player +' minecraft:player_head{SkullOwner:"' + info.player + '"}')
                

    


