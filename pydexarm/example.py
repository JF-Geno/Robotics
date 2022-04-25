from pydexarm import Dexarm
import time

'''windows'''
dexarm = Dexarm(port="COM6")
'''mac & linux'''
# device = Dexarm(port="/dev/tty.usbmodem3086337A34381")


#star up 
dexarm.go_home()
#pick up object on table 
dexarm.move_to(0, 320, 0)
dexarm.move_to(0, 320, 60)
dexarm.move_to(-80, 370, 60)
dexarm.move_to(-80, 370, 0)
dexarm.air_picker_pick()
#put object aside on table 
dexarm.move_to(280, 290, 60)
dexarm.move_to(280, 290, -15)
dexarm.air_picker_place()

#move to pick up clean eras
dexarm.move_to(240, 160, 0)
dexarm.move_to(240, 160, -50)
dexarm.air_picker_pick()

#starts cleaning table  
dexarm.move_to(200, 200, 50)
dexarm.move_to(-100, 400, 50)
dexarm.move_to(-100, 400, 3)
dexarm.move_to(-100, 175, 3)
dexarm.move_to(-20, 195, 3)
dexarm.move_to(-20, 400, 3)
dexarm.move_to(80, 175, 3)
dexarm.move_to(80, 400, 3)
dexarm.move_to(80, 400, 50)
dexarm.move_to(240, 160, 0)
dexarm.move_to(240, 160, -30)
#stops cleaning table 

#put clean eras back 
dexarm.air_picker_place()

dexarm.move_to(200, 200, 50)
dexarm.move_to(240, 300, 60)

dexarm.move_to(280, 290, -50)
#put object back on table
dexarm.air_picker_pick()
dexarm.move_to(240, 300, 60)
dexarm.move_to(-80, 370, 60)
dexarm.move_to(-80, 370, 15)
dexarm.air_picker_place()
time.sleep (3)
dexarm.air_picker_stop()
dexarm.move_to(-73, 348, 60)
dexarm.go_home()
dexarm.close()

#The end, code by (JF Geno Obonde)