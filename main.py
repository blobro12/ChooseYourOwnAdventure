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
        }]
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
                "choice_id": "dragongem"
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
                "choice_id": "stealthy"
            },
        ]
    },

    "scifi_start": {
        "title":
        "Echoes of Andromeda",
        "content":
        """'Captain, We've recieved some messages from an unknown outpost roughly 2 light-years away. We believe that they might be useful to tracking down the secret civilization we've been looking for. However, as of right now, only me and you know about the message. What should we do?'""",
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
                "text": "We know about the..."
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
            "choice_id": "slums"
            "requirements": "halfmoonintel"
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
            "choice_id": "lakeinv"
            gives_items: ["docknote"]
        }, {
            "text": "Further press the dock owner.",
            "next": "dockowner",
            "choice_id": "dockowner"
            "requirements": "docknote"
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
            "choice_id": "checkinbook"
            gives_items: ["halfmoonintel"]
        }, {
            "text": "We'll have to check every room.",
            "next": "everyroom",
            "choice_id": "everyroom"
            gives_items: ["hierachyofsociety"]
        }]
    },
    "slums": {
        "title":
        "Corner of Southside and 5th Street. 1:13 PM",
        "content":
        """You get out of your car to find yourself standing on the corner of 5th and Southside. As rundown as this place looks, you do not feel threathened. You see a woman walking along the sidewalk. 'Ma'am I'm looking for the murderer of one of the people around this area. What could you tell me about his where-abouts?'
        'I don't know anything, but I bet Big Johnny would... for a price.' You can't pass up on the lead of a lifetime. How to get to Big Johnny? """,
        "choices": [{
            "text": "We'll setup a raid a force it out of him.",
            "next": "raided",
            "choice_id": "raided"
        }, {
            "text": "Catching the Half-Moon Murderer is worth the price.",
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
        update_user_session(
            session_id, next_node, choice_data)
        return RedirectResponse(
            f"/story?node={next_node}&session_id={session_id}")
    else:
        # Handle ending or invalid choice
        session = get_user_session(session_id)
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
        "dragongem": "You take the Dragon's heart and grip it tightly. The Gem begins to shine brightly and the Power seems to flow right into your veins. You march to the gates of the Jakeobins and transform. Destroying everything once there. You take throne as the new King, the new power showing through your new grip on the Kingdom. This is what the Loyalists wanted, right? I'm just reclaiming my throne. Ending: Tyrant of Flame🔥",
        "nodragongem": "You took the dragon's heart and threw it on the ground. It shattered into million of pieces. 'Thank you, I am finally free from the cycle that has plagued us for centuries...' the dragon utters to you, as it passes. The Kingdom may still be in shambles but Peace may not be so far away. Ending: The Final Peacekeeper. 🌿",
        "magical_unity": "With the Royal Seal's power and the wisdom gained from your journey, you unite all factions under a new banner of hope. The kingdom enters a golden age of peace and prosperity. Ending: The True King/Queen 👑",
        "dragon_alliance": "The ancient dragon becomes your closest ally, helping you rule with wisdom and strength. Together, you usher in an age where humans and dragons live in harmony. Ending: Dragon Bond 🐲",
        # Add more endings...
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