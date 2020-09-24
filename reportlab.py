from reportlab.pdfgen import canvas

def hello(c):
    c.drawString(100, 100, "Hello Nattapong")

c = canvas.Canvas("hello.pdf")
hello(c)
c.ShowPage()
c.save()