import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")

    def check_password(self, password):
        return self.password == self.hash_password(password)


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


def add_user():
    while True:
        name = input("이름을 입력해주세요: ").strip()
        username = input("ID를 입력해주세요: ").strip()
        if username in members_id:
            print("해당 ID는 사용중입니다. 다른 ID를 사용해주세요.")
            continue
        password = input("패스워드를 입력해주세요: ").strip()

        members.append(Member(name, username, password))
        members_id.append(username)

        if input("회원을 계속 추가하시겠습니까? (y/n): ").lower() != "y":
            break
        print()
    print()

# 터미널에서 게시글을 입력하는 기능


def add_post():
    while True:
        title = input("게시글 제목을 입력해주세요: ").strip()
        content = input("게시글 내용을 입력해주세요: ").strip()
        author = input("게시글 작성자를 입력해주세요: ").strip()

        if author in members_id:
            posts.append(Post(title, content, author))
        else:
            print("해당 ID를 가진 회원이 존재하지 않습니다. ID를 다시 확인해주세요.")
            continue

        if input("게시물을 계속 추가하시겠습니까? (y/n): ").lower() != "y":
            break
        print()
    print()

# 모든 회원의 이름 출력


def display_all_members():
    print("All Members:")
    for member in members:
        print(member.name)

# 특정 회원이 작성한 게시글 제목 출력


def find_post_by_user():
    username = input('누구의 게시글을 찾을까요? ').strip()
    print(f"{username}'s Posts:")
    for post in posts:
        if post.author == username:
            print(post.title)

# 특정 단어가 포함된 게시글 제목 출력


def find_post_by_keyword():
    keyword = input("어떤 키워드를 검색하시겠습니까? ").strip()
    print(f"\nPosts containing '{keyword}' in content:")
    for post in posts:
        if keyword in post.content:
            print(post.title)


# 실행
if __name__ == "__main__":
    while True:
        print("옵션을 선택하세요:\n1. 회원 추가\n2. 게시글 추가\n3. 회원 목록 보기\n4. 회원 게시글 찾기\n5. 키워드로 게시글 찾기\n6. 종료")
        choice = input("선택: ").strip()

        if choice == '1':
            add_user()
        elif choice == '2':
            add_post()
        elif choice == '3':
            display_all_members()
        elif choice == '4':
            find_post_by_user()
        elif choice == '5':
            find_post_by_keyword()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")
