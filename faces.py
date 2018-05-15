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

    

    messages = ['Hey You, Kid! Hey!',
                'There\'s a snake next door!',
                'You look tough, think you could kill it?',
                'I\'ll give you some gold!']
    messages2 = ['Have you killed the snake yet?',
                 'Well come back when you have!']
    messages3 = ['Hey thanks for killing that snake!']


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


class shopkeeper():
    face = [('''
             $$$$$$$$$
            $$$$$$$$$$$
           $| ... ... |$
           C|  O   O  |D
           $|.    |  .|$
          $$|..  -  ..|$$
             \\......./
    ___________________________
    '''),
    ('''
             $$$$$$$$$
            $$$$$$$$$$$
           $| ... ... |$
           C|  -   -  |D
           $|.    |  .|$
          $$|..  -  ..|$$
             \\......./
    ___________________________
    ''')]

    messages = ['Hey there traveller!', 'What can I do for you?']

#
