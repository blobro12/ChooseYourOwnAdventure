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
            "choice_id": "raided",
            "requirements": {"items": ["hierachyofsociety", "docknote"],},
        }, {
            "text": "Let's reach out and see if he'll hand it over peacefully",
            "next": "appease",
            "choice_id": "appease"
        }]
    },
}