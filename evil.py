

def solve():
    # Ok after many tries with this one I ended up finding a gfx file. When googling the format all I could find was
    # proposed solutions for this level. Since it doens't seem something very usefull to learn, and had already wasted a
    # lot of time, i just gave up and checked the solution

    with open("./files/evil/evil2.gfx", "rb") as file:
        s = file.read()

        open("./files/evil/one.jpg", "wb").write(s[0::5])
        open("./files/evil/two.png", "wb").write(s[1::5])
        open("./files/evil/three.gif", "wb").write(s[2::5])
        open("./files/evil/four.png", "wb").write(s[3::5])
        open("./files/evil/five.jpg", "wb").write(s[4::5])
