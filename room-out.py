def on_received_number(receivedNumber):
    if receivedNumber == 1:
        servos.P0.set_angle(180)
        basic.pause(1000)
        servos.P0.set_angle(0)
radio.on_received_number(on_received_number)

servos.P0.set_angle(0)
radio.set_group(20)

def on_forever():
    pass
basic.forever(on_forever)
