#user_count 참여자 수 입력

class User:
    def user_count(self):
        c = int(input("사용자 수 입력해주세요 : "))
        return c
game_count= User()
user_count= game_count.user_count()

print(user_count)
