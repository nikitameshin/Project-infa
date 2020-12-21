class Tag:
    # поля
    tag_str = ""
    content = ""
    # конструктор
    def __init__(self, list = [], attributes="", styles=""):
        s = ""
        for tag in list:
            s += str(tag) #объединяет элементы списка
        if styles != "":
            styles = "style=\"" + styles + "\""
        self.content = "<" + self.tag_str +" " + attributes + styles + ">" + s + "</" + self.tag_str + ">"
        pass
    # преобразование к строке
    def __str__(self):
        return self.content

class Html(Tag):
    tag_str = "html"

class Body(Tag):
    tag_str = "body"

class I(Tag):
    tag_str = "i"

class P(Tag):
    tag_str = "p"

class H1(Tag):
    tag_str = "h1"

class Br(Tag):
    tag_str = "br"
#выделяет текст , тег em
class Em(Tag):
    tag_str = "em"

class Img(Tag):
    tag_str = "img"

class A(Tag):
    tag_str = "a"

class Mark(Tag):
    tag_str = "mark"

link_adress = "https://ru.wikipedia.org/wiki/Заглавная_страница"
img_path = "https://chance4traveller.com/wp-content/uploads/2019/11/e13b2d18528e89af9ac922eb691e31e2631be96dr1-1200-800v2_hq.jpg"
page = Html([Body([H1("Привет красотка "), P(["Ты моя первая  ", Br(), I(["страница"], styles="color: black;"),Br(),  Em("Не судите сторого ")], styles = "color: red; text-align: center"),
A("Wikipedia", attributes="href=\" "+ link_adress + "\""), Br(), Img(attributes="src=\" "+ img_path + "\"")])])
page = str(page)

#помогает сохранить все в файле html
with open("web.html", 'w') as f:
    f.write(page)

#вывод в консоль просто так
print(page)
