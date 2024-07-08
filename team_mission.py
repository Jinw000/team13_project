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


member1 = Member("", "", "")
member2 = Member("", "", "")
member3 = Member("", "", "")

members = []
members.append(member1)
members.append(member2)
members.append(member3)

# 회원 이름 출력
print("All Members:")
for member in members:
    print(member.name)

# 게시글 작성
post1 = Post("", member1.username)
post2 = Post("", member1.username)
post3 = Post("", member1.username)

post4 = Post("", member2.username)
post5 = Post("", member2.username)
post6 = Post("",
             "", member2.username)

post7 = Post("",
             "", member3.username)
post8 = Post("", "",
             member3.username)
post9 = Post("",
             "", member3.username)

# posts 리스트에 게시물 추가
posts = []
posts.extend([post1, post2, post3, post4, post5, post6, post7, post8, post9])

# 각 회원이 작성한 게시글 제목 출력
print("\nPosts by each Member:")
for member in members:
    print(f"{member.name}'s Posts:")
    for post in posts:
        if post.author == member.username:
            print(post.title)

# 특정 단어가 포함된 게시글 제목 출력
keyword = ""
print(f"\nPosts containing '{keyword}' in content:")
for post in posts:
    if keyword in post.content:
        print(post.title)
