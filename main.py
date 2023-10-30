basic.show_icon(IconNames.HAPPY)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 150)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 150)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
basic.pause(1000)
maqueen.motor_stop(maqueen.Motors.ALL)
basic.pause(1000)

def on_forever():
    pass
basic.forever(on_forever)
