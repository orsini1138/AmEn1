# faces.py - put all the faces for the dialogue sections of the game here

class girl():
    face = [('''
            $$$&$$
           $$||||$$
           $ .  . $
           $   `  $
            \\  = /
             |--|
          __/    \\__
    ___________________________
    '''),

    ('''
            $$$&$$
           $$||||$$
           $ _  _ $
           $   `  $
            \\  = /
             |--|
          __/    \\__
    ___________________________
    ''')]

    

    messages = ['Ooh Honey, look at you- you\'re filthy!',
                'I\'m sure I could have you cleaned up in no time-',
                'Hey, wait, you\'re that punk from next door, aren\'t you?',
                'Get the hell outta here before I call the police!']


class man():
    face = [('''
            |^^^^^^^^^|
            | ... ... |
            |  O   O  |
            |.   B   .|
            |..  >  ..|
            |.........|
    ___________________________
    '''),
    ('''
            |^^^^^^^^^|
            | ... ... |
            |  -   -  |
            |.   B   .|
            |..  >  ..|
            |.........|
    ___________________________
    ''')

            ]

    messages = ['Look, I\'m gonna be honest kid...',
                'You\'ve gotta cut it out with this shit.',
                'Everyone is getting REAL sick of your "adventures"',
                'Now go bother someone else! Bakka!']
    

class oven():
    face = [('''
            ^   ^  ^  ^
         |-------------|
         |.     .  .  .|
         |  ..      .  |
         |.  _______   |
         |  /       \\  |
         |..|       |. |
         |_____________|
    ___________________________
    '''),
    ('''
          ^ ^     ^   ^
         |-------------|
         |.     .  .  .|
         |  ..      .  |
         |.  _______   |
         |  /       \\  |
         |..|       |. |
         |_____________|
    ___________________________
    ''')]

    

    messages = ['It\'s an oven!',
                'You can access this to reset your HP to 10 if it\'s lower!',
                'Here\'s your HP you bum!']


class snakeMan():
    face = [('''
            ________
           /    ^   \\
          |^  ^    O \\
          |     _____/```
          | ^^    |
          | ^   ^ |
    ___________________________
    '''),
    ('''
            ________
           /    ^   \\
          |^  ^    - \\
          |     _____/`^`
          | ^^    |
          | ^   ^ |
    ___________________________
    ''')]

    messages = ['You fool! You\'ve come to the Viper!',
                'Prepare to die in Combat!',
                'HISSSSSSSSS']
