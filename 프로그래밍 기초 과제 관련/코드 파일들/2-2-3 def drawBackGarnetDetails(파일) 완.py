import turtle as t

#2-2-3
def drawBackGarnetDetails(t,colorList):
    t.rt(60)
    t.fd(10)
    t.fillcolor(colorList[2])
    t.begin_fill()
    t.rt(120)
    t.fd(10)
    t.rt(120)
    t.fd(2.8)
    t.rt(76)
    t.fd(8.7)
    t.end_fill()
    t.lt(135)
    t.fd(9.9)

    t.rt(60)
    t.fd(10)
    t.begin_fill()
    t.lt(121)
    t.fd(10)
    t.lt(120)
    t.fd(2.8)
    t.lt(76)
    t.fd(8.8)
    t.end_fill()

    t.fillcolor(colorList[1])
    t.begin_fill()
    t.rt(136)
    t.fd(2.8)
    t.lt(77)
    t.fd(9.3)
    t.lt(163)
    t.fd(10.2)
    t.end_fill()
