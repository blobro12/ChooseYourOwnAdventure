from fasthtml.common import *
import json

app, rt = fast_app()

# Story/Decision Tree Structure with Requirements and Items
STORY_NODES = {
    "start": {
        "title":
        "The Nexus Gate",
        "content":
        """You awaken in a room with smooth, obsidian walls. A glowing triangular portal hovers before you. A voice whispers:

    'You may enter one of three paths. Each leads to a world of choice and consequence.'""",
        "choices": [{
            "text": "🐉  Enter The Shattered Kingdom (Fantasy)",
            "next": "fantasy_start",
            "choice_id": "fantasy_start"
        }, {
            "text": "🚀 Step into Echoes of Andromeda (Sci-Fi)",
            "next": "scifi_start",
            "choice_id": "scifi_start"
        }, {
            "text": "🕵️‍♀️ Walk through The Vanishing Hour (Mystery)",
            "next": "mystery_start",
            "choice_id": "mystery_start"
        },
            {"text": "𖣐 Become the Nexus Gate Walker",
                    "next": "nexusgatewalker",
                    "choice_id":"nexusgatewalker",
             "requirements":{"completed_routes": ["dragongem", "accuse", "dreams"]},
            },
    ]
    },
    "fantasy_start": {
        "title":
        "The Shattered Kingdom",
        "content":
        """ You step into a ruined kingdom where dragons once ruled, now fractured by civil war and dark magic. Your Role: A supposedly lost heir to a royal family that was deposed 17 years ago by the Jakeobins. You bewield a secret power that could shape the future of the entire Kingdom. There are myths of a Dragon's Heart which if obtained would allow the user to transform into a dragon temporarily. However, the people grow restless of the new regime. What do you do?""",
        "choices": [{
            "text": "A. Seek the Dragon’s Heart (legendary gem of power)",
            "next": "dragons_heart",
            "choice_id": "heart"
        }, {
            "text": "B. Rally the Loyal Knights",
            "next": "rallyloyals",
            "choice_id": "rebel"
        }, {
            "text": "C. Spy on the Jakeobin's Plans",
            "next": "spyplans",
            "choice_id": "spy"
        }]
    },
    "dragons_heart": {
        "title":
        "The Dragon's Heart",
        "content":
        """You journey through the Cursed Woods of the East, the rumored location of the Dragon's Heart. After a multi-day journey, you begin to doubt these rumors. Suddenly, you spot a tucked away cave that might just host what you are looking for. You walk in cautiously. This seems almost too easy. There it sits. However, not in the form you expected. A dying dragon, clearly past its prime stares before you. 'Human.... I have not much left to offer Take my heart and follow in my footsteps.' There it lies. What do you do?""",
        "choices": [
            {
                "text": "Accept the Gem from the Dragon",
                "next": "dragongem",
                "choice_id": "dragongem",
                "gives_items": ["dragongem"]
            },
            {
                "text": "Refuse and destroy the Gem",
                "next": "nodragongem",
                "choice_id": "nodragongem"
            },
        ]
    },
    "rallyloyals": {
        "title":
        "Rallying the Loyalists",
        "content":
        """ You approach the Loyalists. Their presentation is underwhelming, situated in the back of a tavern. However, they promise there are hundreds of groups ready to strike at their command. However, the Head of the Jakeobins has began putting out vast wealth prizes for people who defect and give away intelligence. The Head Knight who appears to be dressed in gold armor speaks up from the back of table, looking ominously towards you, 'We recently discovered a rat within our own guild. As the heir, we trust you will be just in his punishment. What shall it be?' """,
        "choices": [
            {
                "text": "Execute him as an example of what we do to traitors!",
                "next": "executed",
                "choice_id": "executed"
            },
            {
                "text":
                "Although he is a rat, maybe he can give us some intel on the Jakeobins...",
                "next": "noexecuted",
                "choice_id": "noexecuted"
            },
            {    "text": "He would be the perfect test subject for the Dragon Gem.",
            "next": "dragonraid",
            "choice_id": "dragonraid",
             "requirements":{"items": ["dragongem"]},
            
            },
        ]
    },
    "spyplans": {
        "title":
        "Spying on the Jakeobins",
        "content":
        """You are approached by a man appearing to be dressed in all black. 'Your the heir they spoke of, right?' Intel has it they're staging a big operation to shut down the Loyalist coup and by extension your ticket to power. We have two ideas for getting in: A big distraction or a more... stealthy approach. What do you think? """,
        "choices": [
            {
                "text": "Go big or go home, right?",
                "next": "loud",
                "choice_id": "loud"
            },
            {
                "text": "If we want to outsmart them, we must be meticulous.",
                "next": "stealthy",
                "choice_id": "stealthy",
            },
             {   "text": "They are more likely to trust a member of their team than any of us.",
                "next": "ratspy",
                "choice_id": "ratspy",
                "requirements":{"completed_routes": ["noexecuted"]},
            },
        ]
    },

    "scifi_start": {
        "title":
        "Echoes of Andromeda",
        "content":
        """'Lieutenant, We've recieved some messages from an unknown outpost roughly 2 light-years away. We believe that they might be useful to tracking down the secret civilization we've been looking for. However, as of right now, only me and you know about the message. What should we do?'""",
        "choices": [{
            "text": "Let's keep it underwraps, and see where it leads.",
            "next": "echodiver",
            "choice_id": "echodiver"
        }, {
            "text":
            "We need to inform high command ASAP! This might get us promoted!",
            "next": "highcommand",
            "choice_id": "highcommand"
        }, {
            "text": "Why would they contact us? You must be hearing things.",
            "next": "doubt",
            "choice_id": "doubt"
        }]
    },
    "echodiver": {
        "title":
        "What do we have here?",
        "content":
        """After weeks of studying the message undercover for weeks, there seems to be some technology this civilization is hiding from you. The message states that they have a way to 'See while they are asleep.'You believe this might be a hint to dream technology and might be the best way to learn more about them through hijacking and monitoring their dreams. The only question now: How do we get in? """,
        "choices": [
            {
                "text": "Let's to hack into it using a message with a trojan horse.",
                "next": "trojanhorse",
                "choice_id": "trojanhorse"
            },
            {
                "text": "Let's just ask 'em. No harm no foul, right?'",
                "next": "diplo",
                "choice_id": "diplo"
            },
             {   "text": "We know about the Rilo System. Let us see the dreams and we can help you.",
            "next": "dreams",
            "choice_id": "dreams",
            "requirements":{"completed_routes": ["falsefame"]}
            },    
        ]
    },
    "highcommand": {
        "title":
        "Alpha Delta High Command Center...",
        "content":
        """'Sir, We've picked up some messages from 2 light-years away. I believe this would be our best way in finding out more about this civilization' 'Send me the message. I'll run in through our analyist team; get back to you. If you're right, this could warrant some serious headway. Now about the aliens, what do you think we should do with them once we contact them? """,
        "choices": [
            {
                "text": "If they are just as advanced as we are, it would be best for us to make an alliance with them.",
                "next": "peace",
                "choice_id": "peace"
            },
            {
                "text": "If they are as advanced as we are, they need to be conquered before they become a threat.",
                "next": "conquer",
                "choice_id": "conquer"
            },
        ]
    },
    "doubt": {
        "title":
        "That can't be right.",
        "content":
        """'With all due respect, why would they want to reach out to us if we're the ones hunting them?' 
        'I don't know, sir. Maybe, they want to be found?' 
        'I'm sorry. I'm just not buying it. If it submit this; it's wrong. I could be in some serious trouble. I just can't take the risk. The intern walks off while leaving the drive with the message on your desk. This presents an opportunity.... """,
        "choices": [
            {
                "text": "Take the drive and pass it off as your own findings.",
                "next": "falsefame",
                "choice_id": "falsefame"
            },
            {
                "text": "Throw out the drive.",
                "next": "trash",
                "choice_id": "trash"
            },
        ]
    },
    "mystery_start": {
        "title":
        "The Vanishing Hour",
        "content":
        """Rain drips down your window. These murders, more recently named the Half-Moon Murders, all seem the same. The victims all recieve a letter with four letters: ISYS. We're not sure what these letters mean yet, but we have gotten some leads. One of the foot officers claim that some folks around town could help us. Specifically, the docks, the hotel, and in the slums. Where should we start?""",
        "choices": [{
            "text": "The docks. The last case took place at the docks.",
            "next": "docks",
            "choice_id": "docks"
        }, {
            "text":
            "The hotel. If our killer would be anywhere, that's where he'd be.",
            "next": "hotel",
            "choice_id": "hotel"
        }, {
            "text": "The slums. They're our best chance of tracking him down.",
            "next": "slums",
            "choice_id": "slums",
            "requirements":{"items": ["halfmoonintel"]},
        }]
    },
    "docks": {
        "title":
        "Hartweather Docks; 11:48 PM",
        "content":
        """You arrive at the docks. The place seems like it's out of an old photograph where everything around you is a shade of gray. The owner of the docks comes out to greet you. 'You're here 'bout those murders, right? Here's everything I know. The victim was a lady who was not a frequent customer, but she did mention something 'bout a letter she got. I don't even think she owns a boat. That's why I was puzzled when I heard of the news of her drowning out on the lake. I still don't think something's right 'bout that.... """,
        "choices": [{
            "text": "Investigate around the lake where the body was found.",
            "next": "lakeinv",
            "choice_id": "lakeinv",
            "gives_items": ["docknote"]
        }, {
            "text": "Further press the dock owner.",
            "next": "dockowner",
            "choice_id": "dockowner",
            "requirements":{"items": ["docknote"]},
        },
            {"text": "I bet you planned this to cover up your alibi. I saw your name on that poster...",
            "next": "accuse",
            "choice_id": "accuse",
             "requirements":{"items": ["hierachyofsociety"]},
                    }]
    },
    "hotel": {
        "title":
        "Madame Luvre Hotel, 10:14 PM",
        "content":
        """'Welcome in, Detective. How may I help you?', said the clerk as you walked in. 
        'I'm here on a lead about the Half-Moon Murders. I believe that if the culprit were to hide anywhere, it'd be here.' 
        'Here. This is a master-key of the hotel. If he's in a room, you'll be able to get in.' A choice becomes obvious. How to find him?""",
        "choices": [{
            "text": "See if he was dumb enough to leave a name in the check-in book.",
            "next": "checkinbook",
            "choice_id": "checkinbook",
            "gives_items": ["halfmoonintel"]
        }, {
            "text": "We'll have to check every room.",
            "next": "everyroom",
            "choice_id": "everyroom",
            "gives_items": ["hierachyofsociety"]
        }]
    },
    "slums": {
        "title":
        "Corner of Southside and 5th Street. 1:13 PM",
        "content":
        """You get out of your car to find yourself standing on the corner of 5th and Southside. As rundown as this place looks, you do not feel threathened. Stay focused, how to get to Big Johnny? """,
        "choices": [{
            "text": "We'll setup a raid and force it out of him.",
            "next": "raided",
            "choice_id": "raided"
        }, {
            "text": "Let's reach out and see if he'll hand it over peacefully",
            "next": "appease",
            "choice_id": "appease"
        }]
    },
}

# Enhanced user session structure
user_sessions = {}

def get_user_session(session_id="default"):
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "current_node": "start",
            "choices_made": [],
            "story_path": ["start"],
            "items_collected": [],
            "completed_routes": [],  # Track completed ending paths
            "playthrough_count": 0
        }
    return user_sessions[session_id]

def update_user_session(session_id, node_id, choice_made):
    session = get_user_session(session_id)
    session["current_node"] = node_id
    session["choices_made"].append(choice_made)
    session["story_path"].append(node_id)

    # Add items if the choice gives any
    if "gives_items" in choice_made:
        for item in choice_made["gives_items"]:
            if item not in session["items_collected"]:
                session["items_collected"].append(item)

    return session

def check_choice_requirements(choice, session):
    """Check if a choice's requirements are met"""
    if "requirements" not in choice:
        return True, ""

    reqs = choice["requirements"]

    # Check item requirements
    if "items" in reqs:
        for required_item in reqs["items"]:
            if required_item not in session["items_collected"]:
                return False, choice.get("locked_text", "Requirements not met")

    # Check completed route requirements
    if "completed_routes" in reqs:
        for required_route in reqs["completed_routes"]:
            if required_route not in session["completed_routes"]:
                return False, choice.get("locked_text", "You must complete certain paths first")

    return True, ""

@rt("/")
def get():
    return RedirectResponse("/story")

@rt("/story")
def story_page(node: str = "start", session_id: str = "default"):
    session = get_user_session(session_id)
    current_node = STORY_NODES.get(node, STORY_NODES["start"])

    # Create choice buttons
    choice_buttons = []
    for choice in current_node["choices"]:
        is_available, lock_reason = check_choice_requirements(choice, session)

        if is_available:
            # Available choice - normal button
            choice_buttons.append(
                Button(
                    choice["text"],
                    type="submit",
                    name="choice",
                    value=choice["choice_id"],
                    style="display: block; width: 100%; margin: 10px 0; padding: 15px; text-align: left; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;"
                )
            )
        else:
            # Locked choice - disabled button with explanation
            choice_buttons.append(
                Div(
                    Button(
                        choice["text"],
                        disabled=True,
                        style="display: block; width: 100%; margin: 10px 0; padding: 15px; text-align: left; background: #7f8c8d; color: #bdc3c7; border: none; border-radius: 5px; cursor: not-allowed; font-size: 16px;"
                    ),
                    P(f"🔒 {lock_reason}", style="color: #e74c3c; font-size: 14px; margin: 5px 0 0 0; font-style: italic;")
                )
            )

    # Items display
    items_display = ""
    if session["items_collected"]:
        items_display = Div(
            H4("🎒 Your Items:"),
            P(", ".join([item.replace("_", " ").title() for item in session["items_collected"]])),
            style="margin-top: 20px; padding: 15px; background: #e8f5e8; border-radius: 5px; border-left: 4px solid #27ae60;"
        )

    return Titled(current_node["title"],
        Div(
            H2(current_node["title"], style="color: #34495e; margin-bottom: 20px;"),
            P(current_node["content"], style="line-height: 1.6; margin-bottom: 30px; white-space: pre-line;"),
            items_display,
            Form(
                *choice_buttons,
                Input(type="hidden", name="current_node", value=node),
                Input(type="hidden", name="session_id", value=session_id),
                action="/make_choice",
                method="post"
            ),
            style="max-width: 800px; margin: 0 auto; padding: 20px;"
        ),
        # Story progress indicator
        Div(
            H4("Your Journey:"),
            P(" → ".join([STORY_NODES[n]["title"] for n in session["story_path"] if n in STORY_NODES])),
            style="margin-top: 40px; padding: 20px; background: #ecf0f1; border-radius: 5px;"
        ) if len(session["story_path"]) > 1 else "",
        # Navigation
        Div(
            A("Start Over", href="/restart", style="margin-right: 20px;"),
            A("Story Map", href="/map"),
            style="margin-top: 20px; text-align: center;"
        )
    )

@rt("/make_choice")
def post(choice: str, current_node: str, session_id: str = "default"):
    # Find the next node based on choice
    node_data = STORY_NODES.get(current_node)
    if not node_data:
        return RedirectResponse("/story")

    next_node = None
    choice_data = None

    for choice_option in node_data["choices"]:
        if choice_option["choice_id"] == choice:
            choice_data = choice_option
            next_node = choice_option["next"]
            break

    if choice_data and next_node and next_node in STORY_NODES:
        # Update session with choice data (including items)
        session = update_user_session(session_id, next_node, choice_data)
        
        # Debug: Print items for verification
        print(f"Items collected: {session['items_collected']}")
        
        return RedirectResponse(
            f"/story?node={next_node}&session_id={session_id}")
    else:
        # Handle ending or invalid choice
        session = get_user_session(session_id)
        
        # Check if this choice gives items before ending
        for choice_option in node_data["choices"]:
            if choice_option["choice_id"] == choice and "gives_items" in choice_option:
                for item in choice_option["gives_items"]:
                    if item not in session["items_collected"]:
                        session["items_collected"].append(item)
        
        if choice not in session["completed_routes"]:
            session["completed_routes"].append(choice)
        session["playthrough_count"] += 1

        return RedirectResponse(
            f"/ending?choice={choice}&session_id={session_id}")

@rt("/ending")
def ending_page(choice: str, session_id: str = "default"):
    session = get_user_session(session_id)

    # Your existing endings dictionary here...
    endings = {
        "dragongem":
            "You take the Dragon's heart and grip it tightly. The Gem begins to shine brightly and the Power seems to flow right into your veins. You march to the gates of the Jakeobins and transform. Destroying everything once there. You take throne as the new King, the new power showing through your new grip on the Kingdom. This is what the Loyalists wanted, right? I'm just reclaiming my throne. Ending: Tyrant of Flame🔥",
            "nodragongem":
            "You took the dragon's heart and threw it on the ground. It shattered into million of pieces. 'Thank you, I am finally free from the cycle that has plagued us for centuries...' the dragon utters to you, as it passes. The Kingdom may still be in shambles but Peace may not be so far away. Ending: The Final Peacekeeper. 🌿 ",
            "executed":
            "You didn't just execute him. You made sure anyone you tried to defect again would be scared too. This is what must be done to ensure the victory of the Loyalists. Later that year, the siege of the castle was successful with many losses. The wheels of history turn by blood alone. Ending: Blade of Justice.⚔️",
            "noexecuted":
            """After just a few minutes of interrogation, the rat exposes a major weakness in the Jakeobin ranks. Within a few weeks, the Loyalists were able to secure a majority and coup their leader. Reclaiming your throne once and for all. Ending: The Rat Repays Its Debtors🐀""",
            "loud":
            "'That's what I'm talking about!', the mysterious figure cheers, taking you aback as you now question what you signed up for. 'The Plan is simple: I have 'acquired' some explosives that would be a perfect distraction to allow someone like yourself sneak in, grab info, and get out. With that, he was off. You followed him far behind and found him prepping. 'Now, This, this is the fun part', he said as he pushed the lever. The expolsions rattled you but with all the pursuing chaos. You were able to enter without a hitch. After returning from the Jakeobin base, the intel you gathered allowed the Loyalists to make quick work of the weakened Jakeobins. 'It's good to be back' Ending: 007 Tomorrow Never Dies.🔫",
            "stealthy":
            """The man sighs. 'Fair enough...' You sneak up to the castle, looking for a way in. 'Hey! What are you doing over there?', you hear a voice shout at you. 'Oi, mate! I'm new and I left my keys at home. Can you get me in? I have a meeting in 5 minutes!' 'Sure, Someone has to take care of the new hires.' Perfect, I just got a free ticket.'What did you say your name was?'
            'Jim Milton, they just transfered me from the base up in New Dalesville.'
            'Huh, I didn't even know they had a base in New Dalesville.'
            'It's a newer facility for sure.'
            You thank the man for escorting you and walk into a poorly lit room where there are countless papers strowed all around the walls and floor with circles and threaded lines that look like a madman's work. You walk in and gather as much as you can from the room, leaving it as fast as you entered in. Returning to the man, he thanks you greatly for gathering the intel and disturbing the Jakeobin progress on cracking down the Loyalists. 'Victory shall be ours soon.', he says before disappearing as quickly as he arrived. Ending: The Invisible Man 🙈 """,
        "ratspy": " You send in the rat with not very high hopes. After a few days, he returns much worse than he arrived. 'There's only one thing they gave me and you could probably guess what it was.... However, I did manage to overhear some plans. He says almost begging, realizing what the failed operation might mean for him. 'They plan on building a new base up in New Dalesville, to increase their influence in the area as well as cracking down on the revoultion brewing in the city. That's how we'll find out what they're planning. Ending: The Rat's Tale🐀",
            "trojanhorse":"""It was hard to craft a message that would be real enought for the civilization to believe it was a real message while also dodging high command intervention. After sending the message, you waited. Was this worth it? What if you got caught? Then it came, a notification on your computer. Access Granted. Let's see what these dreams are all about. You load up one of the more recent recordings of the dreams and are met with some of the most beautiful visions you've ever seen. Something about them seemed so surreal; you could not even begin to desribe it to your coworkers without looking like a nut. Maybe, there was a reason that civilization was hidden. Ending: Trapped in a False Paradise🌴""",
            "diplo":"""You send back a friendly message, albiet a weak one given the limited access you're given. After a few weeks, the aliens respond; they declined the request for the dream access. They seem glad that their message has reached someone, but informed you not to go any further. They fear with the technology you possess that they may be overthrown by the humans. Fair enough you suppose. You almost wish there was something more you could've done to win their trust. Ending: Lost to Wonder🔮""",
            "dreams":"You send the response message. Days go by before another message returns...'Given you know about our situation, you must help us. If you want the dreams, take them.' You open the attached dream file and are met with some dreams filled with wonder and beautiful visions unlike anything you've ever seen which makes the nightmares all the more terrifying. It makes you question whether the pursuit to find this civilization was worth it. Ending: Behind the Curtains of the Xialo""",
            "peace": """High Command would send out a message the following week. Making sure to be as sure as possible to have a good connection to the aliens. They would not respond for 6 months. Suddenly, a unfamiliar ship would dock into one of the ports of your station. Panicked at first, High Command would eventually stand down to the aliens upon realizing they were here about the message. They stated they would like to be peaceful towards you, but do not seek an alliance due to fear of drawing attention to someone. They did not say who though. Who is this man? We may not want to know. Ending: The Casted Shadow over Andromeda👤""",    
            "conquer":""" High Command seemed to agree almost immeadiately and quickly sent an ultimatum out to the aliens. High Command seemed to be ready for war since the beginning. Was this their plan? The aliens responded by saying they were worried this would happen. They said if a fight is wanted, to come and get it. High Command seemed amused by this threat. The war was not pretty. Luckily, you were not one of the men that had to slaughter these creatures. In the end, you sit with a statue on the planet and eternal fame. Was it all worth it though? This fame in exchange for a once unknown species' extinction. Ending: The Dark Forest🌲""",
         "falsefame":"""This is my chance to cement myself in the history books. I snatched the drive off the desk and calm as one could be, walked toward the Alpha Delta High Command Center. You walk in, cool and collected as you could. '2nd Lt., What are you doing in here?', says the man behind the first desk. My boss. 'Sir, you are going to want to see this. I have discovered a message that the aliens sent.'
         'Well, let's see this.' He plugs it into the computer and it begans to play. You lean in as you become quite intrigued on what it will say.
         'We hope this finds you quickly. We are the Xialo Civilization. We have lived on the planet of Urailo for nearly 7000 years. As threathening as that may sound, we truly wish for no relations with the humans. For our safety, We believe there is a bigger threat that looms over us from the Rilo System. And, that our secrecy has kept us from being discovered. This message may also be our last. Rest now knowing your search was successful.'
         'Well, that might be the most poetic thing I've ever heard.', said the boss. 'I believe that'll wrap all this up. We appreciate you commitment to the people; for that you are now promoted to Captain.' He salutes and you return it. After the momentary pride, the seriousness of the message looms over you. What if that message is the only memoir that will exist of them? Ending: Memoir of a Fallen Civilization📕""",
            "trash":" You break the drive in half and toss it in the nearby recipticle. There's a since of relief. You feel as though you did what you were supposed to. That message was probably nothing, you think. There's a lot that starts to bear down on you. That could have been it. The ticket. Over the next few weeks, you watch as the search continues to nothing. You return home to your family thinking of what that message could have been about. Atleast, you are safe and you got promoted to 1st Lt. for serving on the voyage. Security is nice. Ending: Connection Terminated🖥️",
            "lakeinv":
            "You board onto a small dingie docked in the port. You push off the shore and use the small motor to pull out to the body. Luckily, there was a small sandbar that allowed you to park the boat. Upon exiting the boat, you notice a small note on the ground, covered in blood. It reads: 'The Moon shines bright tonight, Detective.' You are left with a sense of dread. He knows you're on his tail but you must find him. What does that mean though? You think for a second before sticking it in your pocket. You return to the docks with the plan to take the note for forensic testing. A hit. The prints return a Owen Abbins. He gets busted and taken in, yet something feels off. Maybe, he is just one small part of the conspriacy. Ending: The Moon Shines Bright Tonight.🌙",
            "dockowner":"""'Walk with me if you will Mr. Benns. What were you doing the night that woman was killed?'
            'Well, I was sitting behind the register. Closing up for the night, putting bills in the register, the usual.'
            'You have cameras, Mr. Benns. It would be very difficult to secure an alibi for you if you did not.'
            'My cameras broke two weeks ago; Some hoodlums came in and ransacked the place while I was out, taking care of the lake.' 
            'What did they look like?'
            'They were all dressed in these big yellow jackets with yellow masks with only eye holes. Definetly a planned attack, yet I don't know who I set off.
            Upon further investigation, you found out that the jackets and masks belong to the Society of the Waking Moon. A recent society that has popped up and been causing trouble. Maybe, this cult-like society is behind the murders. You end up finding a member and getting him to talk about the society. However, he was a relatively low ranked member and a few days later, he was found dead in his apartment. Ending: The New Moon🌑""",
        "accuse": "'Nice try', you say smirking, 'You set up the raid on your dock to cover up the alibi and to make you seem like a victim rather than a murder. You're the person who killed that woman. You have a lot of explaining to do. Upon reaching the station, the dock owner spills that he worked with some of the quarter moons to set the whole thing up, but that he wasn't the one pulling the strings. 'Keep looking Detective. I'm just a Cog in the machine. Ending: The Waning Crescent🌒""",
            "checkinbook": """ You check the names and find a name interest: 'John Ebbens Room 301' You bust in his room to find an empty room. However, it looks like he left in a hurry as there's a few things of interst left. Namely, a poster on the wall showing a hierachy of sorts. At the top there is one man with a full moon above him followed by 4 3 quarter moons and 12 new moons under split up among the quarter moons. You take the poster back to the station. 'This is our Society. Now we just have to bust them.' The next day, you are able to corner the man initially in that apartment. He says that the best way to get to the leader is through the slums. He is holed up there under the protection of Big Johnny. As for me, I served my purpose for the Moon. Ending: The Half Moon🌓""",
           "everyroom": "We can't let him get away. We begin busting through every room in the hotel, but he's already gone. The only thing we found of use is in Room 301. A note on the ground reads, 'To Shine you must find the Light.' This note feels like it's missing something. We weren't able to gather much else about the society. This feel like just a small piece to the puzzle. Ending: The Waning Moon🌘",
            "raided": "The team busts in and captures Big Johnny with relative ease. After a long, interrogation, he breaks. 'The leader of the Society of the Waking Moon is a man that goes by 'The Moon'. He is currently out in the woods performing his final ritual to ascend to Moonhood.' You are your team rush out into the middle of the Wakeborrow Woods and track down the man. He quickly notices you and begins to run. You and your team quickly encircle him. 'I see you found Big Johnny. Shame. I was beginning to like him. It seems the Moon does shine bright after all.' You arrest him and take him back to the station. You feel proud to bring the Half-Moon Murders to a close. For now. Ending: The Full Moon🌕",
            "appease": "You arrange for the money to be sent to Big Johnny in return for the location of the leader of the Society of the Waking Moon. He sends you the location of the leader. You and your team rush out into the middle of the Wakeborrow Woods and attempt to track him down. However, he is nowhere to be seen. You are left with a sense of anger. You were so close to capturing him just to be outsmarted at the very end. 'This is over.', you mutter as you walk back to your car. 'This is only the beginning.'Ending: Waxing Gibbous🌔",
    }

    ending_text = endings.get(choice, "The End.")

    # Show unlocked content message if this is a repeat playthrough
    unlock_message = ""
    if session["playthrough_count"] > 1:
        unlock_message = Div(
            H3("🔓 New Paths Unlocked!", style="color: #27ae60;"),
            P("Your previous choices have opened new possibilities in future playthroughs!"),
            style="background: #d5f4e6; padding: 15px; border-radius: 5px; margin: 20px 0;"
        )

    return Titled(
        "Actions always have Consequences...",
        Div(
            H2("The End.", style="color: #e74c3c;"),
            P(ending_text, style="font-size: 18px; line-height: 1.6; margin: 30px 0;"),
            unlock_message,
            H3("Your Items Collected:"),
            P(", ".join([item.replace("_", " ").title() for item in session["items_collected"]]) if session["items_collected"] else "None"),
            H3("Your Choices:"),
            Ul(*[Li(f"{choice.get('from_node', 'Unknown')} → {choice.get('text', choice.get('choice_text', 'Unknown choice'))}")
                 for choice in session["choices_made"]]),
            Div(
                A("Start New Adventure", href="/restart", 
                  style="background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 10px;"),
                A("Continue with Items", href=f"/story?session_id={session_id}", 
                  style="background: #e67e22; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 10px;"),
                A("View Story Map", href="/map", 
                  style="background: #95a5a6; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 10px;"),
                style="text-align: center; margin-top: 40px;"
            ),
            style="max-width: 800px; margin: 0 auto; padding: 20px; text-align: center;"
        )
    )

@rt("/restart")
def restart():
    # Clear session and start over
    return RedirectResponse("/story?session_id=new_" + str(hash("restart"))[:8])

@rt("/map")
def story_map():
    # Enhanced story map showing requirements
    nodes_html = []
    for node_id, node_data in STORY_NODES.items():
        choices_list = []
        for choice in node_data["choices"]:
            choice_text = choice["text"]
            if "requirements" in choice:
                choice_text += " (LOCKED)"
            if "gives_items" in choice:
                choice_text += f" [Gives: {', '.join(choice['gives_items'])}]"
            choices_list.append(Li(choice_text))

        nodes_html.append(
            Div(
                H4(f"{node_id}: {node_data['title']}"),
                P(node_data["content"][:100] + ("..." if len(node_data["content"]) > 100 else "")),
                Ul(*choices_list),
                style="border: 1px solid #bdc3c7; margin: 10px; padding: 15px; border-radius: 5px;"
            )
        )

    return Titled(
        "Story Map",
        Div(
            H2("Story Structure"),
            P("🔒 = Locked choices | [Gives: item] = Grants items", style="font-style: italic; margin-bottom: 20px;"),
            *nodes_html,
            A("Back to Story", href="/story", style="display: block; text-align: center; margin-top: 20px;"),
            style="max-width: 1200px; margin: 0 auto; padding: 20px;"
        )
    )

serve()