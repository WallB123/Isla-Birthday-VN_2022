# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c_nvl = Character("Coleknight", kind=nvl)
define c_adv = Character("Coleknight", what_color="#000000")
define c_all_adv = Character("Coleknights", what_color="#000000")
define n = Character("???", what_color="#000000")
define i = Character("Isla", what_color="#000000")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, what_color="#000000")
define k = Character ("Barista K.", what_color="#000000")
define c_1 = Character("Coleknight 1", what_color="#000000")
define c_2 = Character("Coleknight 2", what_color="#000000")
define c_3 = Character("Coleknight 3", what_color="#000000")

image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

#OUTSIDE CAFE WITH CLOUD
image cafe_cloud:
    contains:
        subpixel True
        xalign 0.0
        yalign 0.0
        "blue"
    contains:
        "cloudsanim"
    contains:
        "cafe"

image cloudsanim:
    contains:
        subpixel True
        xalign 0.0
        HBox(   "clouds",
                "clouds")
        linear 200.0 xpos -1.0
        repeat


# NVL window transition
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    hardPause = True

# Shake Effect
init:
    python:

        import math
        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)


# Game Intro
label splashscreen:
    $ renpy.block_rollback()
    $ quick_menu = False
    scene black
    with Pause(1)
    $ renpy.music.set_volume(0.3, delay=0, channel='movie')
    $ renpy.movie_cutscene('video/logo.webm')
    with Pause(1)
    scene black
    $ renpy.block_rollback()
    show text "{color=#ffffff}{size=+4}Coleknights Present...{/color}{/size}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    scene black
    with dissolve
    $ _game_menu_screen = 'save'
    $ renpy.block_rollback()
    return
define config.end_splash_transition = dissolve

label before_main_menu:
    stop sound
    queue music "audio/Game_title_by_Charzu.ogg" noloop volume 0.4
    queue music "audio/10c.ogg" loop volume 0.05
return

# <------------------------------------------GAME START------------------------------------------>

label start:
    $ quick_menu = False
    $ _game_menu_screen = None
    scene blackbg
    with dissolve
    pause 2
    $ quick_menu = False
    $ _game_menu_screen = None
    scene disclaimer_and_controls
    with dissolve
    pause
    $ quick_menu = True
    window auto
    stop sound
    $ renpy.block_rollback()
    $ quick_menu = True
    $ _game_menu_screen = 'save'
    scene coleknight_bedroom
    with fade
    play music "audio/sound/room_幸せをかぞえて.ogg" loop volume 0.08
    pause 3

    # These display lines of dialogue.
    narrator_nvl "—November 18, Coleknight’s room—{p=1}{nw}"




    narrator_nvl "November 18th… Isla-sama’s birthday!"
    narrator_nvl "For a change of pace, I actually woke up pretty early."
    narrator_nvl "…Wait, it’s Isla’s birthday. It’s... it’s already Friday?"
    narrator_nvl "I thought today was Thursday! I still haven’t gotten her anything!"
    narrator_nvl "Okay, okay, calm down. I still have some time."
    narrator_nvl "I could just get her something today, no biggie."
    narrator_nvl "I’ll just have to walk quickly, yup, mm hmm."
    nvl clear
    with dissolve
    narrator_nvl "I think the store’s close by… Perhaps there’s something there that I can get."
    narrator_nvl "Yes… something… incredible. Something super-duper!"
    narrator_nvl "Something that will make her feel like-"
    narrator_nvl "{color=#a9e0eb}“Omigosh Coleknight, you’ve thought about me for a week? That’s so sweet~”{/color}"
    narrator_nvl "…I totally wasn’t thinking about work or gacha games instead of Isla, not at all."
    window hide
    nvl clear
    with dissolve
    show c_think
    with dissolve
    c_adv "I wonder… which store would have things that Isla would like?"
    hide c_think
    show c_neutral
    c_adv "Hmmm… oh, maybe-"
    #=====
    #sound here
    #=====
    queue sound "audio/sound/ringtone_chama_sneeze.mp3" volume 0.20 fadein 2
    narrator_adv"{p=1}{nw}"
    c_adv "Gwak!? Oh, my friend just texted me. Jeez…"
    c_adv "Okay, I think I’m back to reality now. I’ll just… go out and buy her a gift. Easy."
    hide c_neutral
    with dissolve
    narrator_adv "I finish my morning routine, and head to the station."

    scene blackbg
    with dissolve
    stop music fadeout 1.0
    pause 3
    with dissolve
    play sound "audio/sound/train_door.ogg" noloop volume 0.11
    play music "audio/sound/train_noise.ogg" loop volume 0.11
    scene train
    with dissolve
    window show
    narrator_nvl "—In front of the station—{p=1}{nw}"
    narrator_nvl "Stepping out of the station, I was assaulted by the myriad sounds coming from the various visitors in the city."
    narrator_nvl "There were parents shopping with their children, students hanging out with their friends, there were even foodies enjoying the local cuisine, as well as vendors advertising their shops."
    narrator_nvl "The streets were bustling with activity despite it being early in the morning. A cool sea breeze was blowing through from the nearby port."
    window hide
    nvl clear
    with dissolve
    show c_neutral
    with dissolve
    c_adv "Well, here I am, and I… still don’t know what to get her."
    hide c_neutral
    show c_think
    c_adv "New headphones? No, that’s out of my price range, she wouldn’t replace her earbuds anyway."
    c_adv "Is there any Nino merch she doesn’t have? I doubt it."
    c_adv "Aaaahhhhhh!! I don’t know what to do!"
    stop music fadeout 0.5
    n "Huh? Coleknight?"
    hide c_think
    show c_sad
    c_adv "That voice… it can’t be…"
    narrator_adv "I quickly turn around"
    hide c_sad
    with dissolve
    play music "audio/sound/train_カラフルハート.ogg" loop fadein 0.5  volume 0.08
    scene isla_2
    with dissolve
    narrator_adv "As I saw a girl with golden hair and sparkling blue eyes standing before me, my fears were confirmed."
    narrator_adv "It really is her- my oshi, Isla Coleman!"
    narrator_adv "…why’d I phrase that like a generic anime character?"
    narrator_adv "Normally I’d be ecstatic to see her, but today… right now… I feel only fear."
    c_adv "H-hey, Isla-sama! H-happy birthday!"
    i "Oh, thanks!"
    c_adv "So, what are you doing out here, if you don’t mind me asking."
    i "Ah, I’m just doing a little shopping. I take it you’re out here doing the same?"
    c_adv "Yup!"
    scene train
    with dissolve
    show isla_happyneutral
    with dissolve
    i  "You looked a little panicked when you saw me… you aren’t hiding something, are you? Like maybe, doing some last minute shopping for my present..?"
    narrator_adv "Oh god…"
    c_adv "What?! No, that’s crazy! I’m just uh… Well I wasn’t expecting to run into you is all!"
    hide isla_happyneutral
    show isla_angry
    i "Hmmm…"
    hide isla_angry
    show isla_happyneutral
    i "Well, since you’re here anyway, maybe you could accompany me while I do some shopping."
    i "You’ll carry my bags for me!"
    c_adv "..."
    hide isla_happyneutral
    show isla_angry
    i "I-I’ll give you 16 Minecraft snowballs!"
    hide isla_angry
    show c_sad
    with dissolve
    narrator_adv "Why is she trying to pay me?! I don’t even play Minecraft!"
    narrator_adv "If I join her, I won’t be able to get her a gift. But, looking at her, she doesn’t seem to be in a good mood for some reason…"
    hide c_sad
    show c_happy
    c_adv "Ahh… Sure, I can accompany you."
    hide c_happy
    show isla_happyneutral
    with dissolve
    i "Great! Let’s get started then."
    stop music fadeout 0.5
    scene blackbg
    with dissolve
    pause 3
    play music "audio/sound/street_Sweet_Pea_Home.ogg" loop volume 0.08
    scene street
    with dissolve
    window show
    narrator_nvl "Isla started dragging me around the city with her."
    narrator_nvl "Although she said that I was there to help carry her bags, we spent most of the time just chatting and window shopping."
    narrator_nvl "After a while, I started noticing a pattern in some of the shops we went by."
    narrator_nvl "Greeting cards, balloons, party supplies, a bakery with charmingly decorated birthday cakes in the window…"
    narrator_nvl "With each one we passed, she looked more and more frustrated. Why could that be?"
    nvl clear
    with dissolve
    window hide
    scene store
    with dissolve
    show isla_happyneutral
    with dissolve
    narrator_adv "We were walking past a convenience store when Isla suddenly stopped."
    i "Hey, can we take a bit of a break? I’m starting to get thirsty."
    c_adv "Oh, sure. I was starting to get thirsty as well."
    narrator_adv "We entered the store, and moved toward the drink coolers."
    narrator_adv "Isla silently grabbed a green tea, with a despondent expression on her face."
    narrator_adv "While I was looking for a drink, she finally said something."
    hide isla_happyneutral
    show isla_sad
    i "Coleknight… today is my birthday, right?"
    c_adv "Hm? Of course it is."
    i "Then… how come you’re the only one that seemed to remember?"
    narrator_adv "I froze for a moment and began to think about what she said."
    c_adv "Huh? You mean to say that no one else wished you a happy birthday?"
    i "Well… you’re the only Coleknight that did. My morning tweet barely got any interaction too..."
    narrator_adv "Come to think of it, when she tweeted this morning I only liked it, and I didn’t really check if anyone else liked or even replied."
    i "Did… did everyone forget…?"
    narrator_adv "Before I could reply, Isla gloomily walked to the register with her green tea."
    hide isla_sad
    show c_sad
    with dissolve
    narrator_adv "This isn’t good… I pulled out my phone and told the other Coleknights to take a break to at least wish her happy birthday on Twitter."
    narrator_adv "Maybe that’ll help her mood, but I feel like I should get her a little gift to try and cheer her up more…"
    hide c_sad
    show c_think
    narrator_adv "But, what can I get her?"
    window hide
default menuset = set()
# <------------------------------------------JUMP CHOICES------------------------------------------>
# <------------------------------------------------------------------------------------------------>
# <------------------------------------------------------------------------------------------------>
menu choice_gift:

    set menuset
    narrator_adv "What can I get her?"

    "Cup Noodles":
        jump cup_noodles

    "Sanrio Keychain":
        jump sanrio_keychain

    "Can of air":
        jump can_air

    "???":
        jump something_1
# <------------------------------------------------------------------------------------------------>
# <------------------------------------------------------------------------------------------------>
# <------------------------------------------JUMP CHOICES------------------------------------------>



# <------------------------------------------CHOICES------------------------------------------>
# <------------------------------------------------------------------------------------------->
# <------------------------------------------------------------------------------------------->

#=====
#Cup Noodles
#=====
label cup_noodles:

    hide c_think
    with dissolve
    scene store_noods
    with dissolve
    window show
    narrator_nvl "Isla likes food, but what could I get at a convenience store…?"
    narrator_nvl "I check the counter to see if they have anything in the hot case… nothing."
    narrator_nvl "I don’t think she’d like any of the bentos in the cooler either…"
    narrator_nvl "I start scanning the aisles desperately, but there’s really nothing special here."
    narrator_nvl "… I’ll have to go with ol’ reliable."
    nvl clear
    with dissolve
    window hide
    scene store
    with dissolve
    show isla_happyneutral
    with dissolve
    i "That took a while, did they not have what you were looking for?"
    c_adv "Something like that."
    i "Ah, we can go to a different store if you want."
    c_adv "No no, that’s fine. I was trying to find a little something for you since you were feeling down, but…"
    hide isla_happyneutral
    show isla_o
    narrator_adv "I hold out the Cup Noodle."
    i "… Cup Noodle?"
    c_adv "Uh, y-yeah…"
    i "…"
    hide isla_o
    show isla_eyesclosed
    i "Ahahahahaha!"
    narrator_adv "This is pretty embarrassing…"
    i "Sorry, sorry. I appreciate the thought behind it, I just wasn’t expecting Cup Noodle of all things."
    i "Thank you, really."
    narrator_adv "I’m still pretty embarrassed… but at least she’s okay with it."
    jump cont
#=====
# Sanrio Keychain
#=====
label sanrio_keychain:

    hide c_think
    with dissolve
    scene store_chain
    with dissolve
    window show
    narrator_nvl "Is that a display of Sanrio merch? Perfect!"
    narrator_nvl "I head over to the display. Looks like they’re selling keychains, phone charms, and other small items."
    narrator_nvl "This is good, I’ll just get a Cinnamoroll keychain and… where is he?"
    narrator_nvl "Oh, this empty spot must have been where he was…"
    narrator_nvl "Well, I already decided on this. But which character should I get?"
    narrator_nvl "No, I can’t overthink this too much."
    narrator_nvl "I remember her saying she likes Kuromi, and there are still a couple keychains in stock, so I grab one and quickly head to the register to pay."
    nvl clear
    with dissolve
    window hide
    scene store
    with dissolve
    show isla_happyneutral
    with dissolve
    i "Did you get what you need?"
    c_adv "Yeah, it’s actually a little gift for you."
    i "A gift?"
    narrator_adv "I give her the Kuromi keychain."
    c_adv "Sorry, I know it isn’t much, and there wasn’t any Cinnamoroll, but I know you like Kuromi too so…"
    hide isla_happyneutral
    show isla_eyesclosed
    narrator_adv "Isla smiles warmly."
    i "This is really cute! Thank you… I luvey it."
    narrator_adv "For the first time since we ran into each other, she looks genuinely happy."
    jump cont

# Canned Air
label can_air:
    hide c_think
    with dissolve
    scene store_can
    with dissolve
    window show
    narrator_nvl "Wait, I know Isla likes practical merch, maybe she’d like a practical gift, too."
    narrator_nvl "But what would be here that’s practical…"
    narrator_nvl "Multivitamins? Lotion? Toothpaste?"
    narrator_nvl "Wait, is that a can of air? Perfect!"
    narrator_nvl "She’s been needing to clean her computer out for 2 years now."
    narrator_nvl "I grab the can and go to check out."
    nvl clear
    with dissolve
    window hide
    scene store
    with dissolve
    show isla_happyneutral
    with dissolve
    c_adv "Sorry to keep you waiting."
    i "Oh, it’s no problem. Did you have trouble finding a drink?"
    c_adv "No, I actually just wanted to buy a little something for you, since it’s your birthday and all."
    narrator_adv "I give her the can of air."
    hide isla_happyneutral
    show isla_o
    i "… What is it?"
    c_adv "A can of compressed air, of course!"
    i "Compressed air?"
    c_adv "Yeah! You just pull the trigger and it shoots out air from the nozzle."
    narrator_adv "She follows my instructions, and when the air shoots out her eyes widen in wonder."
    hide isla_o
    show isla_amazed
    narrator_adv "She keeps spraying the air, laughing every time."
    i "This is so cool! Ahahaha!"
    hide isla_amazed
    show isla_eyesclosed
    narrator_adv "I didn’t expect this to get such a reaction out of her, but if it cheered her up then I’m glad."
    jump cont

# ???/Bad End
label something_1:
    hide c_think
    with dissolve
    scene store_rrat
    with dissolve
    window show
    narrator_nvl "My mind is completely blank! I can’t think of something on the spot like this!"
    narrator_nvl "I look around quickly, eyes darting back and forth trying to find something, anything!"
    narrator_nvl "Wait, I saw something out of the corner of my eye, is that a…"
    narrator_nvl "…"
    narrator_nvl "…"
    narrator_nvl "I grab it and hurry out of the store."
    nvl clear
    with dissolve
    window hide
    scene store
    with dissolve
    show isla_happyneutral
    with dissolve
    i "Ah, there you are. You look kind of… off, is something wrong?"
    c_adv "Oh, it’s just that you seemed to be troubled so… here."
    stop music
    narrator_adv "I hand her a rat."
    hide isla_happyneutral
    show isla_shockedbw
    with dissolve
    pause 2
    narrator_adv "She looks at it blankly, then at me."
    narrator_adv "I give her a thumbs up"
    scene blackbg
    with dissolve
# Bad End
    play movie "video/rrat.webm" loop
    show movie with dissolve

    narrator_adv "-Bad End- \n
    Why did you think giving her a rat from the convenience store would be a good idea?"
    with dissolve
    $ _game_menu_screen = None
    jump splashscreen


# <------------------------------------------------------------------------------------------->
# <------------------------------------------------------------------------------------------->
# <------------------------------------------CHOICES------------------------------------------>

label cont:
    hide isla_eyesclosed
    show isla_smug
    i "Hey, wanna grab something to eat? Of course, you’ll be paying, it’s MY birthday after all."
    c_adv "Oh, sure. Was there anywhere you wanted to go to?"
    hide isla_smug
    show isla_eyesclosed
    i "Yeah! It’s a cafe called Le Fishe au Chocolat."
    narrator_adv "That is… quite the name for a cafe. But she seems really excited to go there."
    hide isla_eyesclosed
    show c_happy
    with dissolve
    c_adv "Sounds good, lead the way."
    hide c_happy
    with dissolve
    narrator_adv "Isla happily starts walking while I follow. It seems like she’s back to her usual self."
    narrator_adv "I’m glad that my little gift was able to help cheer her up so much."
    scene blackbg
    with dissolve
    pause 2
    scene street
    with dissolve
    narrator_adv "We talk about random topics as we walk."
    show isla_happyneutral
    with dissolve
    i "So Coleknight, do you have an heirloom yet?"
    c_adv "No, not yet."
    hide isla_happyneutra
    show isla_smug
    i "Heeeh? Still no heirloom? Even I got one!"
    c_adv "Through pity."
    i "Still counts! Buuut, if you buy some more packs then maybe you’ll get one. Don’t count on it though~"
    hide isla_smug
    show isla_eyesclosed
    narrator_adv "She laughs happily."
    narrator_adv "Even if it’s at my expense, it’s good to see her so cheerful again."
    #=====#
    #bell sound and change to cafe bgm
    #=====#
    stop music fadeout 1.0
    scene blackbg
    with dissolve
    pause 3
    play music "audio/sound/cafe_outside.ogg" loop volume 0.75
    scene cafe_cloud
    with dissolve
    pause 3
    window show
    narrator_nvl "…"
    narrator_nvl "Sure enough, it’s really called Le Fishe au Chocolat."
    narrator_nvl "The cafe owner's refined taste is obvious from the outside. The simple wooden exterior reminds me of a Japanese inn."
    narrator_nvl "I wouldn't be surprised if an onsen happened to be hiding in the back somewhere."
    narrator_nvl "My eyes slowly relax as they trace a path along the wood. A menu on the wall is closely guarded on both sides by colorful origami, folded into the appearance of strawberries and blueberries."
    nvl clear
    with dissolve
    #cafe inside
    play sound "audio/sound/sliding_door.mp3" fadein 0.6 volume 0.1
    scene blackbg
    with dissolve
    pause 2
    #=====
    #bell ring
    #=====
    play music "audio/sound/cafe_bossa_nova.ogg" loop volume 0.1
    scene cafeinside_day
    with dissolve
    narrator_nvl "We walked through the narrow door into a room full of bright people enjoying their meals."
    narrator_nvl "We saw someone eating thin powdered crepes with berries and cream, and another was eating vanilla ice cream with nuts and fudge."
    narrator_nvl "We even saw mushroom and swiss, pesto chicken, as well as an open-faced sandwich topped with fish and onion."
    narrator_nvl "A loner in the corner was taking a small bite out of a bagel that was toasted on both sides."
    narrator_nvl "The barista flashes us a warm smile. This place is busy for the early afternoon."
    nvl clear
    with dissolve
    window hide
    #=====#
    #koshita voice (if ever he sends one)
    #=====#
    k "Welcome!"
    show isla_happyneutral
    with dissolve
    narrator_adv "We both order coffee, Isla also orders a parfait for herself."
    hide isla_happyneutral
    show isla_sad
    narrator_adv "While waiting, Isla repeatedly checks her phone. Why could that be? "
    narrator_adv "She has been checking her phone all day, so I thought nothing of it, but now that she’s doing it more frantically, I’m becoming more curious and worried."
    narrator_adv "I have to ask…"
    hide isla_sad
    show c_neutral
    with dissolve
    c_adv "Is everything okay, Isla?"
    hide c_neutral
    show isla_happyneutral
    with dissolve
    i "Huh? Oh, it’s just…"
    #=====
    #windows scene
    #=====
    scene windows
    with dissolve
    narrator_adv "She tilts her head and looks to the side, like she’s trying to find the right words to say."
    i "I guess… the day is gonna be over soon, and you’re the only one who’s really done anything for me."
    i "I got some more birthday wishes, but…"
    i "I was kind of hoping for something more…"
    narrator_adv "Her voice is wavering…"
    i "Oh! I don’t mean to devalue what you’ve done so far, I know it wasn’t planned, but I really appreciate you spending time with me today, and for the little gift you gave me."
    i "I just…{p=0.3}{nw}"
    $ renpy.music.set_pause(True, channel="music")
    scene cafeinside_no_nino
    show coleguard
    #Shake effect
    with Shake((0, 0, 0, 0), 0.5, dist=7)
    narrator_adv "The waitress comes to the table with our order, somewhat breaking up the tense atmosphere."
    hide coleguard
    show isla_sad
    with dissolve
    i "Sorry, I think I need to go for an idol meeting real quick…"
    c_adv "O-oh, sure. Go ahead."
    hide isla_sad
    with dissolve
    window show
    narrator_nvl "She gets up and leaves the table."
    narrator_nvl "This is worse than I thought… Is there anything more I can do?"
    narrator_nvl "…"
    narrator_nvl "No, for the time being, I don’t think there’s much I can do."
    narrator_nvl " I could probably try texting the other Coleknights again, see if I can get more of them to wish her a happy birthday or something…"
    nvl clear
    narrator_nvl "Before I can act, Isla returns to the table."
    narrator_nvl "Guess all I can do now is just talk to her, and hopefully get her mind off of things."
    $ renpy.music.set_pause(False, channel="music")
    scene cafeinside_dusk
    with dissolve
    narrator_nvl "I started talking to her about random topics, like how the plural of octopus can be octopi and not just octopuses, and how air fryers are the peak of human inventions; anything to keep her mind off of the lack of Coleknights."
    narrator_nvl "I’m not sure whether it’s working, or that she caught on to what I was doing and is trying to keep me from worrying, but she does seem to be happier now."
    narrator_nvl "We sat there talking for a long time. So long, in fact, that the sky turned orange as the sun began to set."
    nvl clear
    window hide
    with dissolve
    pause 2
    stop music fadeout 1.0
    play sound "audio/sound/sliding_door.mp3" fadein 0.6 volume 0.1
    scene blackbg
    with dissolve
    pause 3
    play music "audio/sound/cafe_outside.ogg" loop volume 0.75
    scene cafe_dusk
    with dissolve
    show isla_happyneutral
    with dissolve
    narrator_adv "We leave the restaurant and are immediately hit by the cool autumn air."
    narrator_adv "Isla does a little stretch, then looks toward me."
    i "It’s starting to get pretty late… was there anywhere you wanted to go before the day’s over, Coleknight?"
    hide isla_happyneutral
    show c_think
    with dissolve
    c_adv "Oh, yeah, there actually is a place I wanted to go…"

default menuset2 = set()
# <------------------------------------------JUMP CHOICES 2---------------------------------------->
# <------------------------------------------------------------------------------------------------>
# <------------------------------------------------------------------------------------------------>
menu choice_place:
    set menuset

    narrator_adv "The place I wanted to go…"

    "The park":
        jump park

    "Olympus":
        jump abex
# <------------------------------------------JUMP CHOICES 2---------------------------------------->
# <------------------------------------------------------------------------------------------------>
# <------------------------------------------------------------------------------------------------>

#BAD END
label abex:
    play music "audio/sound/abex_choice_Maru_Maru_Animals.ogg" loop volume 0.11 fadein 1.0
    hide c_think
    show c_happy
    c_adv "… We should go play some APEX!"
    hide c_happy
    show isla_amazed
    with dissolve
    narrator_adv "Isla’s eyes light up like a fire."
    i "Yeah! Let’s go!"
    scene blackbg
    with dissolve
    window show
    with dissolve
    narrator_nvl "We went to the local net cafe. Thankfully for us, the computers all have Apex already installed."
    narrator_nvl "We queue up. Isla constantly flaunts her heirloom, but it unfortunately doesn’t improve her game sense."
    narrator_nvl "We had many losses, but a few champions too."
    narrator_nvl "Regardless, the two of us had fun closing out the night with some Apex."
    nvl clear
    with dissolve
    stop music fadeout 5
    window hide
    pause 2
    narrator_adv "I feel like there was something I had to do… Well, it’s too late for that. I’m just gonna keep playing Apex."
    narrator_adv "Bad End (depending on how you look at it)"
    with dissolve
    $ _game_menu_screen = None
    jump splashscreen

#GOOD END
label park:
    hide c_think
    show c_neutral
    c_adv "There’s a nice park nearby, I think taking a little walk would be good."
    hide c_neutral
    show isla_happyneutral
    with dissolve
    i "Umu, sounds good to me."
    scene blackbg
    with dissolve
    pause 2
    play music "audio/sound/dusk.ogg" loop fadein 1 volume 0.3
    scene park
    with dissolve
    show isla_happyneutral
    with dissolve
    narrator_adv "The sun continues to set with each step we take. Darkness started to engulf our surroundings."
    hide isla_happyneutral
    show isla_sad
    narrator_adv "I looked to my right and noticed that Isla was tensing up."
    hide isla_sad
    show c_sad
    with dissolve
    c_adv "Is something wrong, Isla-sama?"
    hide c_sad
    show isla_sad
    with dissolve
    i "Oh, it’s just… It’s getting a little bit creepier the darker it gets…"
    narrator_adv "As I look around, I begin to see why she’s scared. This park is definitely creepy at night."
    narrator_adv "There’s a giant snail… it’s a slide with giant cartoon eyes and a shell pattern, and as we move it seems to be following us."
    narrator_adv "There is a giant spider… no, it’s actually a round jungle gym."
    narrator_adv "Why does this park have to be bug themed!? I start walking a bit faster."
    hide isla_sad
    show c_neutral
    with dissolve
    c_adv "I see. Well, we’re almost out of the park, and luckily it’s close to the station."
    hide c_neutral
    show isla_sad
    with dissolve
    i "Okay…"
    narrator_adv "As we approach the last grassy open area of the park, we start seeing some bright lights, but these weren’t the normal blue lights of the streetlamps."
    hide isla_sad
    show isla_shocked
    with dissolve
    narrator_adv "Isla starts looking confused, but I smile knowing what that means."
    stop music
    scene party
    #screen shake
    with Shake((0, 0, 0, 0), 0.5, dist=7)
    c_all_adv "Happy birthday Isla-sama!!"
    show isla_shocked
    i "Uweeh?!"
    play music "audio/sound/bday_Lucria.ogg" loop volume 0.11 fadein 1.0
    narrator_adv "She looks completely shocked."
    i "…"
    i "…"
    hide isla_shocked
    show isla_cry
    i "Y-you idiots!"
    narrator_adv "Eh?"
    i "Even if you were going to throw me a surprise party, you should’ve wished me a happy birthday earlier!"
    narrator_adv "It sounds like she’s trying to fight back tears. But she’s right, that’s the least we could’ve done…"
    narrator_adv "The Coleknights all apologize to her."
    hide isla_cry
    with dissolve
    c_1 "We’re really sorry Isla-sama, it took us the whole day to prepare all this stuff! And we didn’t want to ruin the surprise!"
    c_2 "Yeah! Who knew baking a cake would be so hard… we even failed many times on the icing alone!"
    c_3 "Shut up, you weren’t even helping! You were just tasting the icing as we put it on! We didn’t even notice until halfway!"
    narrator_adv "The other Coleknights laugh."
    narrator_adv "I look towards Isla-sama."
    show c_neutral
    with dissolve
    c_adv "Again, we’re really sorry for making it look like everyone forgot about your birthday, Isla-sama."
    hide c_neutral
    show c_happy
    c_adv "But we do hope you’d like what we prepared for you."
    hide c_happy
    show isla_eyesclosed
    with dissolve
    i "Well… I do appreciate this. No point in being upset now, so let’s party!"
    scene final_cg
    with dissolve
    pause 1
    i "Thank you, Coleknights."
    stop music fadeout 5.0
    pause 5










    # This ends the game.
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    play movie "video/credits.webm" volume 0.6
    $ renpy.pause(15, hard=True)
    pause 94.5
    jump splashscreen
