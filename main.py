from fasthtml.common import *
import json

app, rt = fast_app()

# Story/Decision Tree Structure with Requirements and Items
STORY_NODES = {
    "start": {
        "title": "The Nexus Gate",
        "content": """You awaken in a room with smooth, obsidian walls. A glowing triangular portal hovers before you. A voice whispers:

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
        "title": "The Shattered Kingdom",
        "content": """ You step into a ruined kingdom where dragons once ruled, now fractured by civil war and dark magic. Your Role: A supposedly lost heir to a royal family that was deposed 17 years ago by the Jakeobins. You bewield a secret power that could shape the future of the entire Kingdom. There are myths of a Dragon's Heart which if obtained would allow the user to transform into a dragon temporarily. However, the people grow restless of the new regime. What do you do?""",
        "choices": [{
            "text": "A. Seek the Dragon's Heart (legendary gem of power)",
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
        }, {
            "text": "🔒 D. Use Ancient Royal Magic (Requires Royal Seal)",
            "next": "royal_magic",
            "choice_id": "royal_magic",
            "requirements": {"items": ["royal_seal"]},
            "locked_text": "You need the Royal Seal to access ancient magic"
        }]
    },
    "dragons_heart": {
        "title": "The Dragon's Heart",
        "content": """You journey through the Cursed Woods of the East, the rumored location of the Dragon's Heart. After a multi-day journey, you begin to doubt these rumors. Suddenly, you spot a tucked away cave that might just host what you are looking for. You walk in cautiously. This seems almost too easy. There it sits. However, not in the form you expected. A dying dragon, clearly past its prime stares before you. 'Human.... I have not much left to offer Take my heart and follow in my footsteps.' There it lies. What do you do?""",
        "choices": [
            {
                "text": "Accept the Gem from the Dragon",
                "next": "dragongem",
                "choice_id": "dragongem",
                "gives_items": ["dragon_heart"]
            },
            {
                "text": "Refuse and destroy the Gem",
                "next": "nodragongem",
                "choice_id": "nodragongem",
                "gives_items": ["dragon_peace"]
            },
            {
                "text": "🔒 Attempt to heal the Dragon (Requires Dragon Peace from previous playthrough)",
                "next": "heal_dragon",
                "choice_id": "heal_dragon",
                "requirements": {"completed_routes": ["nodragongem"]},
                "locked_text": "You must have chosen peace with dragons before to unlock this path",
                "gives_items": ["dragon_ally"]
            }
        ]
    },
    "rallyloyals": {
        "title": "Rallying the Loyalists",
        "content": """ You approach the Loyalists. Their presentation is underwhelming, situated in the back of a tavern. However, they promise there are hundreds of groups ready to strike at their command. However, the Head of the Jakeobins has began putting out vast wealth prizes for people who defect and give away intelligence. The Head Knight who appears to be dressed in gold armor speaks up from the back of table, looking ominously towards you, 'We recently discovered a rat within our own guild. As the heir, we trust you will be just in his punishment. What shall it be?' """,
        "choices": [
            {
                "text": "Execute him as an example of what we do to traitors!",
                "next": "executed",
                "choice_id": "executed"
            },
            {
                "text": "Although he is a rat, maybe he can give us some intel on the Jakeobins...",
                "next": "noexecuted",
                "choice_id": "noexecuted",
                "gives_items": ["spy_intel"]
            },
            {
                "text": "🔒 Offer him a chance at redemption (Requires Dragon Heart power)",
                "next": "redemption_path",
                "choice_id": "redemption",
                "requirements": {"items": ["dragon_heart"]},
                "locked_text": "You need the Dragon's power to sense his true intentions"
            }
        ]
    },
    "spyplans": {
        "title": "Spying on the Jakeobins",
        "content": """You are approached by a man appearing to be dressed in all black. 'Your the heir they spoke of, right?' Intel has it they're staging a big operation to shut down the Loyalist coup and by extension your ticket to power. We have two ideas for getting in: A big distraction or a more... stealthy approach. What do you think? """,
        "choices": [
            {
                "text": "Go big or go home, right?",
                "next": "loud",
                "choice_id": "loud",
                "gives_items": ["explosive_knowledge"]
            },
            {
                "text": "If we want to outsmart them, we must be meticulous.",
                "next": "stealthy",
                "choice_id": "stealthy",
                "gives_items": ["stealth_training"]
            },
            {
                "text": "🔒 Use the spy intel to infiltrate perfectly (Requires Intel)",
                "next": "perfect_infiltration",
                "choice_id": "perfect_infiltration",
                "requirements": {"items": ["spy_intel"]},
                "locked_text": "You need intelligence from interrogating the traitor",
                "gives_items": ["royal_seal"]
            }
        ]
    },
    # New nodes for locked content
    "royal_magic": {
        "title": "Ancient Royal Magic",
        "content": """With the Royal Seal glowing in your hand, you feel the ancient magic of your bloodline coursing through your veins. The seal reveals hidden passages and forgotten spells that your ancestors once wielded. You can sense the true loyalties of everyone around you and command respect through divine right.""",
        "choices": [
            {
                "text": "Use the magic to unite all factions peacefully",
                "next": "magical_unity",
                "choice_id": "magical_unity"
            },
            {
                "text": "Combine royal magic with dragon power (if you have it)",
                "next": "ultimate_power",
                "choice_id": "ultimate_power",
                "requirements": {"items": ["dragon_heart"]},
                "locked_text": "You need both Royal Seal and Dragon Heart for ultimate power"
            }
        ]
    },
    "heal_dragon": {
        "title": "The Dragon's Redemption",
        "content": """Having learned compassion from your previous journey, you approach the dying dragon differently. You place your hands on its ancient scales and channel healing energy. The dragon's eyes brighten as life returns to its massive form. 'You... you have changed since we last met across the threads of fate. I am in your debt, young heir.'""",
        "choices": [
            {
                "text": "Ask the dragon to be your ally",
                "next": "dragon_alliance",
                "choice_id": "dragon_alliance"
            },
            {
                "text": "Request the dragon teach you ancient wisdom",
                "next": "dragon_wisdom",
                "choice_id": "dragon_wisdom"
            }
        ]
    },
    "redemption_path": {
        "title": "The Power of Redemption",
        "content": """The Dragon Heart's power allows you to see into the traitor's soul. You discover he was being blackmailed - the Jakeobins threatened his family. With your newfound power, you help him rescue his loved ones and turn him into your most loyal ally.""",
        "choices": [
            {
                "text": "Lead a perfectly informed rebellion",
                "next": "perfect_rebellion",
                "choice_id": "perfect_rebellion"
            }
        ]
    },
    "perfect_infiltration": {
        "title": "The Master Spy",
        "content": """Using the detailed intelligence from your interrogation, you walk directly into the Jakeobin stronghold disguised as one of their own agents. You're not just sneaking around - you're attending their strategy meetings and sabotaging their plans from within. You discover the location of the lost Royal Seal.""",
        "choices": [
            {
                "text": "Retrieve the Royal Seal and expose their plans",
                "next": "seal_retrieved",
                "choice_id": "seal_retrieved"
            }
        ]
    },

    # Continue with existing sci-fi and mystery content...
    "scifi_start": {
        "title": "Echoes of Andromeda",
        "content": """'Captain, We've recieved some messages from an unknown outpost roughly 2 light-years away. We believe that they might be useful to tracking down the secret civilization we've been looking for. However, as of right now, only me and you know about the message. What should we do?'""",
        "choices": [{
            "text": "Let's keep it underwraps, and see where it leads.",
            "next": "echodiver",
            "choice_id": "echodiver"
        }, {
            "text": "We need to inform high command ASAP! This might get us promoted!",
            "next": "highcommand",
            "choice_id": "highcommand"
        }, {
            "text": "Why would they contact us? You must be hearing things.",
            "next": "doubt",
            "choice_id": "doubt"
        }, {
            "text": "🔒 Use stealth training to investigate secretly (Requires Stealth Training)",
            "next": "stealth_investigation",
            "choice_id": "stealth_investigation",
            "requirements": {"items": ["stealth_training"]},
            "locked_text": "You need stealth training from a previous adventure"
        }]
    },
    "mystery_start": {
        "title": "The Vanishing Hour",
        "content": """Rain drips down your window. These murders, more recently named the Half-Moon Murders, all seem the same. The victims all recieve a letter with four letters: ISYS. We're not sure what these letters mean yet, but we have gotten some leads. One of the foot officers claim that some folks around town could help us. Specifically, the docks, the hotel, and in the slums. Where should we start?""",
        "choices": [{
            "text": "The docks. The last case took place at the docks.",
            "next": "docks",
            "choice_id": "docks"
        }, {
            "text": "The hotel. If our killer would be anywhere, that's where he'd be.",
            "next": "hotel",
            "choice_id": "hotel"
        }, {
            "text": "The slums. They're our best chance of tracking him down.",
            "next": "slums",
            "choice_id": "slums"
        }, {
            "text": "🔒 Use explosive knowledge to force answers (Requires Explosive Knowledge)",
            "next": "explosive_interrogation",
            "choice_id": "explosive_interrogation",
            "requirements": {"items": ["explosive_knowledge"]},
            "locked_text": "You need knowledge of explosives from a previous adventure"
        }]
    },

    # Continue with existing content but add some cross-story requirements...
    "docks": {
        "title": "Hartweather Docks; 11:48 PM",
        "content": """You arrive at the docks. The place seems like it's out of an old photograph where everything around you is a shade of gray. The owner of the docks comes out to greet you. 'You're here 'bout those murders, right? Here's everything I know. The victim was a lady who was not a frequent customer, but she did mention something 'bout a letter she got. I don't even think she owns a boat. That's why I was puzzled when I heard of the news of her drowning out on the lake. I still don't think something's right 'bout that.... """,
        "choices": [{
            "text": "Investigate around the lake where the body was found.",
            "next": "lakeinv",
            "choice_id": "lakeinv"
        }, {
            "text": "Further press the dock owner.",
            "next": "dockowner",
            "choice_id": "dockowner"
        }, {
            "text": "🔒 Use dragon wisdom to sense deception (Requires Dragon Ally)",
            "next": "truth_sensing",
            "choice_id": "truth_sensing",
            "requirements": {"items": ["dragon_ally"]},
            "locked_text": "You need the wisdom of dragons to see through lies"
        }]
    },

    # Add more existing nodes with some modifications for items...
    # (I'll include key ones to show the pattern)
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