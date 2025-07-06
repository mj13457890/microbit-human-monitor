n = 0
OLED.init(128, 64)
radio.set_group(20)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 0:
        n = 3
        OLED.clear()
        OLED.write_string_new_line("If you don't turn back within 3 seconds, the water will shoot out and the egg will break.")
        for index in range(3):
            OLED.write_num(n)
            n -= 1
            basic.pause(1000)
        if pins.digital_read_pin(DigitalPin.P0) == 0:
            OLED.write_string_new_line("fire")
            radio.send_number(1)
            music.play(music.string_playable("A B A B A B A B ", 333),
                music.PlaybackMode.UNTIL_DONE)
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(3000)
        pins.digital_write_pin(DigitalPin.P2, 0)
    else:
        basic.show_leds("""
            . # # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)
