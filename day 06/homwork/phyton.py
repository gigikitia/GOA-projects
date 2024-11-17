
x *= 2  # იგივეა რაც x = x * 2
x += 5  # იგივეა რაც x = x + 5
x /= 4  # იგივეა რაც x = x / 4


Debugging დებაგინგიგამოსწორებს პროგრამაში არსებულ შეცდომებს (ბაგებს) და ახდენს მისი შესრულების პრობლემების პოვნასა და გადაჭრას


x = 0


x = x + 3  


x = x * 2  

x = x - 1  


x = x / 5  

x = x + 10  


print(x)



import turtle


t = turtle.Turtle()


for _ in range(3):  
    t.forward(100)  
    t.left(120)    


turtle.done()
