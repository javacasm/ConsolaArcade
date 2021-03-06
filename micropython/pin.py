from pyb import Pin  #引入引脚类


"""
A6 - UP
A7 - LEFT
A5 - DOWN
B2 - RIGHT
B9 - A
C3 - B
LED_GREEN
LED_RED
BUZZ

"""

help(Pin.board)  #在MU中使用REPL敲如下指令查看喵比特所有引脚定义

p_out = Pin('A1', Pin.OUT_PP)       #将A2设置为推挽式驱动输出模式
p_out.high()        #引脚输出高电平
p_out.low()         #引脚输出低电平

p_in = Pin('A2', Pin.IN, Pin.PULL_UP)  #将A2设置为输入模式，且设置上拉
p_in.value()      #获取I0的电平，0或者1

