import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/rlandhr._.o/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "고예원")
write("description", "효성중 3학년")
write("button", "인스타그램")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "mbti": "istp",
  "학교": '대구 효성중",
  "좋아하는 것": "고양이",
  "좋아하는 과목": "과학"
}
information(informations)
