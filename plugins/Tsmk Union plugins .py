# -*- coding: utf-8 -*-
# made by GBPZkimmi
#插件信息
PLUGIN_METADATA = {
    'id': 'Tsmk Union plugins',
    'version': '0.1.7',
    'name': 'Tsmk Union plugins',
    'link': 'https://github.com/Kimmigbpz/TsmK-official'
}
#加载注册
def on_load(server, old_module):
    server.register_help_message('!!dim', 'true开启/false关闭 服务器多线程')
    server.register_help_message('!!mcdr lvl', '查看您的MCDR权限等级')
    global op
    op = 'false'
    global dim
    dim = 'true'
#进入游戏时加载
def on_player_joined(server, player):
    server.execute("deop @a")
#标准响应
def on_info(server,info):
    if 'a server operator' in info.content and 'no longer a server operator' not in info.content and op == 'false':
        server.execute("deop @a")
        server.say("请勿试图获取管理员,默认设置为:阻止false")
        server.say("管理权限已被夺回")
    elif 'a server operator' in info.content and 'no longer a server operator' not in info.content and op == 'ture':
        server.say("已获取管理员,权限控制设置为:允许true")
#用户响应
def on_user_info(server,info):
        #dim项
        if info.content == '!!dim':
            server.say('!!dim true 开启服务器超线程优化\n!!dim false 关闭服务器超线程优化')
            if dim == 'true':
                server.say('dim:true')
            else:
                server.say('dim:false')
        elif info.content == '!!dim true' and server.get_permission_level(info.player) >=3:
            server.execute('gamerule dimthread_active true')
            dim = 'true'
            server.say('多线程优化已开启')
        elif info.content == '!!dim false' and server.get_permission_level(info.player) >=3:
            server.execute('gamerule dimthread_active false')
            dim = 'false'
            server.say('多线程优化已关闭')
        #ban项
        elif info.content == '!!ban':
            server.say('NAN')
        #pardon项
        elif info.content == '!!pardon':
            server.say('NAN')
        #mcdr lvl项
        elif info.content == '!!mcdr lvl':
            server.say("玩家：" + info.player + "您的MCDR等级是" + str(server.get_permission_level(info.player)))
            if server.get_permission_level(info.player) == 0:
                server.say("等级0为guest,属服务器参观者,可以进行所有基本操作,但无法进行任何特殊操作")
            elif server.get_permission_level(info.player) == 1:
                server.say("等级1为player,属服务器成员,可以进行所有基本操作,以及一些特殊操作")    
            elif server.get_permission_level(info.player) == 2:
                server.say("等级2为helper,属服务器重要成员,可以进行一些关键指令操作")
            elif server.get_permission_level(info.player) == 3:
                server.say("等级3为admin,属服务器管理员,可以进行所有插件与指令操作,但不会破坏游戏平衡")
            elif server.get_permission_level(info.player) == 4:
                server.say("等级4为owner,属服务器所有者,可以进行所有插件与指令操作与调试,但不会破坏游戏平衡")
        #head项
        elif info.content.startswith('!!head'):
                server.execute('give ' + info.player +' minecraft:player_head{SkullOwner:"' + info.player + '"}')
        elif info.content == '!!op true' and server.get_permission_level(info.player)==4:
            op = 'true'
            server.say("op控制设置为 允许true")
        elif info.content == '!!op false' and server.get_permission_level(info.player)==4:
            op = 'false'
            server.say("op控制设置为 阻止false")
