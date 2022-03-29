import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count=0
    while(n != 1):
        count=count+1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
                      # the last print is 1
    return count
def drawLineGraph(upperBound):
  window=turtle.Screen()
  window.setworldcoordinates(0,0,10,10)
  turtleMaxData=turtle.Turtle()
  turtleDraw=turtle.Turtle()
  turtleDraw.speed(0)
  turtleDraw.up()
  turtleMaxData.up()
  turtleDraw.goto(0,0)
  turtleDraw.down()
  max_so_far=0
  for i in range(1,upperBound):
    result=seq3np1(i)
    if(result>max_so_far):
      max_so_far=result
      turtleMaxData.clear()
      turtleMaxData.goto(0,max_so_far)
      str="Maximum so far: {}, {}".format(i,max_so_far)
      turtleMaxData.write(str)
    turtleDraw.goto(i,result)
    window.setworldcoordinates(0,0,i+10,max_so_far+10)
  window.exitonclick()
def main():
  value = int(input("Enter an upper bound..."))
  if(value<=0):
    return
  for i in range(1,value):
    print(i)
    print(seq3np1(i))
  drawLineGraph(value)
main()
