def on_gesture_logo_up():
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_logo_pressed():
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.show_icon(IconNames.TORTOISE)