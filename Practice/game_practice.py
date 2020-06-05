#模拟简单的王者荣耀游戏
import random

print('*'*30,'亲爱的召唤师，欢迎来到王者荣耀','*'*30)
role = input('请选择英雄：（1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.亚瑟 7.兰陵王 8.安琪拉 9.铠 10.程咬金）\n')
weapon_list = []
coins = 1000
print('亲爱的{1}，当前的金币是{0}'.format(coins,role))

while True:
    choice = input('请选择：\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n')
    # 购买武器
    if choice == '1.购买武器':
        print('欢迎来到武器库：')
        weapons = [['枪', 480], ['扇子', 500], ['打野刀', 650], ['剑', 500]]
        for weapon in weapons:
            print(weapon[0], weapon[1])
            # 提示输入要购买的武器
        weaponname = input('请输入要购买的武器名称：\n')
        # 1.原来有没有买过武器，2.输入的武器名是否存在于武器库
        if weaponname not in weapon_list:
            for weapon in weapons:
                if weaponname == weapon[0]:
                    # 购买武器
                    if coins >= weapon[1]:
                        # 减去武器所需金币
                        coins -= weapon[1]
                        # 将武器添加到武器列表
                        weapon_list.append(weapon[0])
                        print('{}的武器{}购买成功！当前金币余额是{}'.format(role, weaponname, coins))
                        break
                    else:
                        print('金币不足，赶快打仗挣金币')
                        break
            else:
                print('输入武器名称错误，请重新输入\n')
        else:
            print('您已经拥有该武器，不用重复购买')
    # 打仗
    elif choice == '2.打仗':
        print('进入战场····')
        # 判断是否拥有武器
        if len(weapon_list) > 0:
            # 选择武器
            print('{}拥有的武器有：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('请选择要使用的武器名称：\n')
                if weaponname in weapon_list:
                    # 进入战争状态，默认与系统对战
                    ran1 = random.randint(1,20)
                    ran2 = random.randint(1,20)
                    if ran1 > ran2:
                        print('此局对战：系统胜利！！！')
                    elif ran1 < ran2:
                        coins += 200
                        print('此局对战：{}胜利，剩余金币是{}！！！'.format(role,coins))
                    else:
                        print('此局平局')
                        # if answer == 'y':
                        #     continue
                    break
                else:
                    print('选择的武器不存在，请重新选择\n')
        else:
            print('{}还没有武器，请购买'.format(role))
    # 删除武器
    elif choice == '3.删除武器':
        if len(weapon_list) > 0:
            print('{}拥有的武器有：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('请选择要删除的武器名称：\n')
                if weaponname in weapon_list:
                    # 删除武器 remove(obj)  pop(index)  clear del weapon_list(index)
                    weapon_list.remove(weaponname)
                    # 退还金币
                    weapons = [['枪', 480], ['扇子', 500], ['打野刀', 650], ['剑', 500]]
                    for weapon in weapons:
                        if weaponname == weapon[0]:
                            coins += weapon[1]
                            print('{}删除成功，当前金币是{}'.format(weaponname, coins))
                            break
                    break
                else:
                    print('输入武器名称错误，请重新输入\n')
                    break
        else:
            print('{}还没有武器，请购买'.format(role))
    # 4.查看武器
    elif choice == '4.查看武器':
        if len(weapon_list) > 0:
            print('{}拥有的武器有：'.format(role))
            for weapon in weapon_list:
                print(weapon)
        else:
            print('{}还没有武器，请购买'.format(role))
    elif choice == '5.退出游戏':
        answer = input('确认退出游戏吗(y/n)?\n')
        if answer == 'y':
            print('game over')
            break
    else:
        print('输入错误，请重新输入\n')

