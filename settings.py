from pygame import locals
# TODO: Video Diver
# TODO: Joystick
# TODO: Aesthetics

settings = {
    'VSync': (True, 'Sync frame rate with monitor refresh rate'),
    'Target FPS': (69, 'How many frames to be displayed per second'),
    'Fullscreen': (True, ''),
    'Resizeable': (False, 'Allows for screen resizing'),
    'Borderless': (False, 'Removes controls and border from screen'),
    'Controls': ({
        'Move Left': (locals.K_a, ''),
        'Move Up': (locals.K_w, ''),
        'Move Right': (locals.K_d, ''),
        'Move Down': (locals.K_s, '')
    }, ''),
    'MAXSCREENSIZE': ((3840, 2160), ''),
    'MINSCREENSIZE': ((800, 600), '')
}
