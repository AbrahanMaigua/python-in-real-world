import time

def pomodoro(work:   int  =25,
            Break:   int  =5,
             cont:   int  =0,  
             mesg:   list =('Red', 'Yellow', 'Green')):

  while True:
    cont +=1 
    if cont == 1:
      print(mesg[cont-1 ])
      # como la funcion sleep aceta el tiempo en 
      # segundos hay que realizar una conversion
      # de segundos a minutos 
      # t = mins X 60 seg
      # t = 35 mins X 60seg = 2.100
      time.sleep(work * 60)

    if cont == 2:
      print(mesg[cont-1 ])
      time.sleep(Break - 3 * 60)

    if cont == 3:
      print(mesg[cont-1 ])
      time.sleep(Break* 60)
      break

pomodoro(mesg=('Work 25 min', 'end in 5','Break 5 min' ))