from p5 import *

def setup():
  global x
  createCanvas(500,500)
  x = 150
  global spin
  spin = 0 


def draw():
  global x
  global spin
  global y
  y= random(350,450)
  background("skyblue")
  #drawTickAxes()

  
  #circle
  fill("yellow")
  noStroke()
  circle(0,500,200)
  #rectangle/ground
  #rect(x,y,w,h)
  fill("green")
  stroke("lightgreen")
  strokeWeight(4)
  rect(0,0,500,35)
  #cloud/oval
  #ellipse(x,y,w,h)
  fill("white")
  noStroke()
  ellipse(x,y,100,50)
  x=x+1

  #ellipse/ alien head
  fill("magenta")
  noStroke()
  ellipse(250, 300, 50,100)
  
  #ellipse/ alien body
  fill("lightgreen")
  noStroke()
  ellipse(250, 175, 75,150)

  #ellipse/ alien eye
  eyeX = 250
  eyeY = 310
  eyeLength = 45
  eyeWidth = 20
  fill("white")
  noStroke()
  ellipse(eyeX, eyeY, eyeLength,eyeWidth) 

  xRatio = (mouseX-eyeX)/eyeX
  yRatio = (mouseY-eyeY)/eyeY

  pupilX = eyeX + xRatio * eyeLength/2
  pupilY = eyeY + yRatio * eyeWidth/2
  
  #ellipse/ alien pupil
  fill("blue")
  noStroke()
  circle(pupilX, pupilY, 15) #circle(x,y,diameter)
  #circle(eyeX, eyeY, 15) #circle(x,y,diameter)

  #line/ alien smile
   #arc(x,y,w,h,startangle,stopangle)
  stroke("black")
  noFill()
  strokeWeight(3)
  arc(250,285,25,25,180,360)

  translate(250,75)
  spin = spin + 10
  rotate(spin)
  
  #drawTickAxes()

  #ellipse/ alien feet
  fill("orange")
  noStroke()
  ellipse(0,0, 75,50)
