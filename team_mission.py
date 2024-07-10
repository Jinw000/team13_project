class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(
            f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}")


members = []
posts = []
members_id = []

# 터미널에서 유저를 추가하는 기능


def plus_user():
    while True:
        name = input("이름을 입력해주세요: ").strip()
        username = input("ID를 입력해주세요: ").strip()
        if username in members_id:
            print("해당 ID는 사용중입니다. 다른 ID를 사용해주세요.")
            continue
        password = input("패스워드를 입력해주세요: ").strip()

        members.append(Member(name, username, password))
        members_id.append(username)

        if input("회원을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
            print()
            continue
        else:
            break
    print()

# 터미널에서 게시글을 입력하는 기능


def plus_post():
    while True:
        title = input("게시글 제목을 입력해주세요: ").strip()
        content = input("게시글 내용을 입력해주세요: ").strip()
        author = input("게시글 작성자를 입력해주세요: ").strip()

        if author in members_username:
            posts.append(post(title, content, author))
        else:
            print("해당 ID를 가진 회원이 존재하지 않습니다. ID를 다시 확인해주세요.")
            continue

        if input("게시물을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
            print()
            continue
        else:
            break
    print()


# 회원 이름 출력
print("All Members:")
for member in members:
    print(member.name)


# 회원이 작성한 게시글 제목 출력
def find_post():
    user_name = input('누구의 게시글을 찾을까요?')
    print(f"{user_name}'s Posts:")
    for post in posts:
        if post.author == user_name:
            print(post.title)

# 특정 단어가 포함된 게시글 제목 출력


def find_post_key():
    keyword = input("어떤 키워드를 검색하시겠습니까?")
    print(f"\nPosts containing '{keyword}' in content:")
    for post in posts:
        if keyword in post.content:
            print(post.title)
