bearing = 0

def on_forever():
    global bearing
    bearing = input.compass_heading()
    if bearing < 45 or bearing > 315:
        basic.show_string("N")
    else:
        basic.show_string(" ")
basic.forever(on_forever)
