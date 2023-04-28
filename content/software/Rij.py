import tkinter as tk

bSd=32
bS = 32
w, h = 1280, 640

main = tk.Tk()

main.title("R x i x j")
main.geometry(f"{w}x{h}")

canvas=tk.Canvas(main, width=w, height=h)
canvas.pack()

for x in range(int(w/bS)):
    canvas.create_line(bS*(x+1),0,bS*(x+1),h, fill="gray", width=1)

for y in range(int(h/bS)):
    canvas.create_line(0,bS*(y+1),w,bS*(y+1), fill="gray", width=1)

canvas.create_line(w/2,0,w/2,h, fill="black", width=3)
canvas.create_line(0,h/2,w,h/2, fill="black", width=3)

X,Y,Z = int(w/(bS*2)),int(h/bS),8

for a in range(X):
    for b in range(bS*Y*int(32/bS)):
        m = a **2 - ((h/2*int(32/bS)-b)/bSd) **2
        n = 2 *a * ((h/2*int(32/bS)-b)/bSd)
        canvas.create_oval(w/2+bS*m-1, h/2+bS*n-1, w/2+bS*m+1, h/2+bS*n+1, fill="blue", width=0)

for a in range(X):
    for b in range(bS*Y):
        m = a **2 + ((h/2-b)/bS) **2
        n = 2 *a *((h/2-b)/bS)
        canvas.create_oval(w/2+bS*m-1, h/2+bS*n-1, w/2+bS*m+1, h/2+bS*n+1, fill="green", width=0)


tk.mainloop()