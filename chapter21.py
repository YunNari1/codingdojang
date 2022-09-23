import turtle as t

a, b = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(a):
    t.forward(b)
    t.right((360 / a)*2)
    t.forward(b)
    t.left(360/a)

