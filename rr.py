from turtle import *

# Setup screen
title("RR Decor Logo")
bgcolor("black")
pencolor("white")
hideturtle()

# Write main logo text
penup()
goto(-150,50)
pendown()
write("Rrdecor", font=("Brush Script MT", 72, "bold"))

# Write tagline
penup()
goto(-180,-50)
pendown()
write("COUNTER DECORATOR AND A CATERER", font=("Arial", 14, "bold"))

done()
