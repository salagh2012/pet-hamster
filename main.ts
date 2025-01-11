input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
})
basic.showIcon(IconNames.Tortoise)
