from instabot import Bot
from cuenta import dic
# from shutil import rmtree
# borrar la carpeta config
# rmtree("config")
mi_bot = Bot()
lista = []
lista2 = []
# print(dic['username'])
# print(dic)
mi_bot.login(username=dic['email'], password=dic['password'])
followers = mi_bot.get_user_followers(dic['username'])
followings = mi_bot.get_user_following(dic['username'])
# print(f"seguidores is {len(followers)}")
# print(f"seguidos is {len(followings)}")
# print(dir(mi_bot))
# print(followers)
# print('---------------')
# print(followings)
# user_id = '32719091660' 
# username = mi_bot.get_username_from_user_id(user_id)
# print(f"Welcome {username} your userid is {user_id}")

# print (len(seguidores))
# print (len(seguidos))
#for id_seguidos in seguidos:
#    if not id_seguidos in seguidores:
        # lista.append(id_seguidos)
        # username = mi_bot.get_username_from_user_id(id_seguidos)
        # lista2.append(username)
#        mi_bot.unfollow(id_seguidos)
# print(len(lista))
# print(lista)
# print(len(lista2))
# print(lista2)

for id_seguidos in followings:
    if not id_seguidos in followers:
        # lista.append(id_seguidos)
        # username = mi_bot.get_username_from_user_id(id_seguidos)
        # lista2.append(username)
        mi_bot.unfollow(id_seguidos)