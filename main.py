from fasthtml.common import *
import json
from datetime import datetime

app, rt = fast_app(
    hdrs=[
        Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"),
        Script(src="https://unpkg.com/htmx.org@1.9.10"),
    ]
)

# Story/Decision Tree Structure
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
        "content": """You step into a ruined kingdom where dragons once ruled, now fractured by civil war and dark magic. Your Role: A supposedly lost heir to a royal family that was deposed 17 years ago by the Jakeobins. You bewield a secret power that could shape the future of the entire Kingdom. There are myths of a Dragon's Heart which if obtained would allow the user to transform into a dragon temporarily. However, the people grow restless of the new regime. What do you do?""",
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
        }]
    },
    "dragons_heart": {
        "title": "The Dragon's Heart",
        "content": """You journey through the Cursed Woods of the East, the rumored location of the Dragon's Heart. After a multi-day journey, you begin to doubt these rumors. Suddenly, you spot a tucked away cave that might just host what you are looking for. You walk in cautiously. This seems almost too easy. There it sits. However, not in the form you expected. A dying dragon, clearly past its prime stares before you. 'Human.... I have not much left to offer Take my heart and follow in my footsteps.' There it lies. What do you do?""",
        "choices": [{
            "text": "Accept the Gem from the Dragon",
            "next": "dragongem",
            "choice_id": "dragongem"
        }, {
            "text": "Refuse and destroy the Gem",
            "next": "nodragongem",
            "choice_id": "nodragongem"
        }]
    },
    "rallyloyals": {
        "title": "Rallying the Loyalists",
        "content": """You approach the Loyalists. Their presentation is underwhelming, situated in the back of a tavern. However, they promise there are hundreds of groups ready to strike at their command. However, the Head of the Jakeobins has began putting out vast wealth prizes for people who defect and give away intelligence. The Head Knight who appears to be dressed in gold armor speaks up from the back of table, looking ominously towards you, 'We recently discovered a rat within our own guild. As the heir, we trust you will be just in his punishment. What shall it be?'""",
        "choices": [{
            "text": "Execute him as an example of what we do to traitors!",
            "next": "executed",
            "choice_id": "executed"
        }, {
            "text": "Although he is a rat, maybe he can give us some intel on the Jakeobins...",
            "next": "noexecuted",
            "choice_id": "noexecuted"
        }]
    },
    "spyplans": {
        "title": "Spying on the Jakeobins",
        "content": """You are approached by a man appearing to be dressed in all black. 'Your the heir they spoke of, right?' Intel has it they're staging a big operation to shut down the Loyalist coup and by extension your ticket to power. We have two ideas for getting in: A big distraction or a more... stealthy approach. What do you think?""",
        "choices": [{
            "text": "Go big or go home, right?",
            "next": "loud",
            "choice_id": "loud"
        }, {
            "text": "If we want to outsmart them, we must be meticulous.",
            "next": "stealthy",
            "choice_id": "stealthy"
        }]
    },
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
        }]
    },
    "mystery_start": {
        "title": "The Vanishing Hour",
        "content": """Rain drips down your window. These murders, more recently named the Half-Moon Murders, are seem the same. The victims all recieve a letter with four letters: ISYS. We're not sure what these letters mean yet, but we have gotten some leads. One of the foot officers claim that some folks around town could help us. Specifically, the docks, the hotel, and in the slums. Where should we start?""",
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
        }]
    },
    "noexecuted": {
        "title": "The Traitor's Confession",
        "content": """After hours of careful interrogation, the traitor finally breaks down and reveals crucial information about the Jakeobin operations. His confession mentions several key infiltration points and even reveals a coded message about 'Debtors' who owe allegiance to the cause. This intelligence proves invaluable to the Loyalist cause.""",
        "choices": [{
            "text": "Use this information to strike immediately",
            "next": "strike_now",
            "choice_id": "strike"
        }, {
            "text": "Gather more intelligence first",
            "next": "more_intel",
            "choice_id": "intel"
        }]
    }
}

# Secret code fragments hidden in story content
SECRET_CODE_FRAGMENTS = {
    "fragment_1": {
        "code_piece": "SHADOW",
        "location": "dragons_heart",
        "trigger_word": "shadows",
        "replacement": '<span class="secret-word" hx-get="/discover-fragment/fragment_1" hx-target="#secret-response" hx-swap="innerHTML" data-fragment="fragment_1">shadows</span>',
        "discovery_text": "The ancient runes on the cave wall glow briefly, revealing the word: SHADOW"
    },
    "fragment_2": {
        "code_piece": "NEXUS", 
        "location": "echodiver",
        "trigger_word": "technology",
        "replacement": '<span class="secret-word" hx-get="/discover-fragment/fragment_2" hx-target="#secret-response" hx-swap="innerHTML" data-fragment="fragment_2">technology</span>',
        "discovery_text": "The dream technology panel flickers and displays a cryptic message: NEXUS"
    },
    "fragment_3": {
        "code_piece": "GATE",
        "location": "mystery_start", 
        "trigger_word": "letter",
        "replacement": '<span class="secret-word" hx-get="/discover-fragment/fragment_3" hx-target="#secret-response" hx-swap="innerHTML" data-fragment="fragment_3">letter</span>',
        "discovery_text": "You examine the victim's letter more closely and notice faint writing on the back: GATE"
    },
    "fragment_4": {
        "code_piece": "WALKER",
        "location": "noexecuted",
        "trigger_word": "Debtors",
        "replacement": '<span class="secret-word" hx-get="/discover-fragment/fragment_4" hx-target="#secret-response" hx-swap="innerHTML" data-fragment="fragment_4">Debtors</span>',
        "discovery_text": "Hidden in the traitor's confession, you discover a coded message: WALKER"
    }
}

# User state tracking
user_sessions = {}

def get_user_session(session_id="default"):
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "current_node": "start",
            "choices_made": [],
            "story_path": ["start"],
            "code_fragments": [],
            "secret_attempts": 0
        }
    return user_sessions[session_id]

def update_user_session(session_id, node_id, choice_made):
    session = get_user_session(session_id)
    session["current_node"] = node_id
    session["choices_made"].append(choice_made)
    session["story_path"].append(node_id)
    return session

def make_words_clickable(content, current_node, session):
    """Replace trigger words with clickable HTMX elements"""
    processed_content = content

    for frag_id, fragment in SECRET_CODE_FRAGMENTS.items():
        if (fragment["location"] == current_node and 
            frag_id not in session["code_fragments"] and
            fragment["trigger_word"] in content):
            processed_content = processed_content.replace(
                fragment["trigger_word"], 
                fragment["replacement"]
            )

    return processed_content

# Main story page
@rt("/")
def get():
    return story_page()

@rt("/story")
def story_page(node: str = "start", session_id: str = "default"):
    session = get_user_session(session_id)
    current_node = STORY_NODES.get(node, STORY_NODES["start"])

    # Process story content to make trigger words clickable
    story_content = make_words_clickable(current_node["content"], node, session)

    # Create choice buttons with HTMX
    choice_buttons = []
    for choice in current_node["choices"]:
        choice_buttons.append(
            Button(
                choice["text"],
                hx_post="/make-choice",
                hx_vals=json.dumps({
                    "choice": choice["choice_id"],
                    "current_node": node,
                    "session_id": session_id
                }),
                hx_target="#game-container",
                hx_swap="innerHTML",
                style="display: block; width: 100%; margin: 10px 0; padding: 15px; text-align: left; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; transition: all 0.3s ease;",
                _="on mouseenter add .hover-effect to me on mouseleave remove .hover-effect from me"
            )
        )

    # Code fragments display
    fragments_display = create_fragments_display(session)

    return Titled("The Nexus Gate Adventures"),
        # Enhanced CSS
Style("""
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
            }

            .game-container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                max-width: 900px;
                margin: 0 auto;
                padding: 40px;
            }

            .secret-word {
                position: relative;
                cursor: pointer;
                transition: all 0.3s ease;
                color: #8e44ad;
                font-weight: bold;
                border-bottom: 2px dotted #9b59b6;
                padding: 2px 6px;
                border-radius: 4px;
                background: rgba(155, 89, 182, 0.1);
            }

            .secret-word:hover {
                background: rgba(155, 89, 182, 0.2);
                color: #663399;
                text-shadow: 0 0 8px rgba(155, 89, 182, 0.6);
                transform: scale(1.05);
                box-shadow: 0 0 15px rgba(155, 89, 182, 0.3);
            }

            .secret-word.discovered {
                animation: secretReveal 0.8s ease-out;
                background: linear-gradient(45deg, #9b59b6, #8e44ad);
                color: white;
                border: none;
                cursor: default;
            }

            @keyframes secretReveal {
                0% { transform: scale(1); }
                50% { transform: scale(1.2); box-shadow: 0 0 20px rgba(155, 89, 182, 0.8); }
                100% { transform: scale(1); }
            }

            .code-fragment {
                font-family: 'Courier New', monospace;
                background: #2c3e50;
                color: #ecf0f1;
                padding: 4px 8px;
                border-radius: 4px;
                font-weight: bold;
                margin: 0 4px;
                display: inline-block;
            }

            .fragments-container {
                background: linear-gradient(135deg, #f8f9fa, #e9ecef);
                border: 2px solid #9b59b6;
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }

            .hover-effect {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }

            .story-content {
                line-height: 1.8;
                font-size: 16px;
                margin-bottom: 30px;
                white-space: pre-line;
                color: #2c3e50;
            }

            .secret-response {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                text-align: center;
                font-weight: bold;
                animation: fadeIn 0.5s ease-in;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .progress-indicator {
                background: #ecf0f1;
                padding: 20px;
                border-radius: 8px;
                margin-top: 30px;
                border-left: 4px solid #3498db;
            }
        """),

        # Include hyperscript for enhanced interactions
Script(src="https://unpkg.com/hyperscript.org@0.9.12"),

Div(
            H1("🌟 The Nexus Gate Adventures"), 
               style="text-align: center; color: #2c3e50; margin-bottom: 30px;"),

Div(id="game-container",
                H2(current_node["title"], style="color: #34495e; margin-bottom: 20px;"),

                # Story content with clickable words
                Div(
                    H2(current_node["title"], style="color: #34495e; margin-bottom: 20px;"),
                    # Story content with clickable words
                    Div(
                        Raw(story_content), 
                        class_="story-content"
                    ),
                    # Secret response area
                    Div(id="secret-response", style="min-height: 20px;"),
                    # Code fragments display
                    fragments_display,
                    # Choice buttons
                    Div(
                        *choice_buttons,  # Unpacked positional arguments first
                        style="margin: 30px 0;"  # Keyword arguments after
                    ),
                    # Progress indicator
                    create_progress_indicator(session),
                    id="game-container",
                    class_="game-container"
                ),

            # Navigation
                  Div(
                      *[
                          Button(
                              "🔄 Start Over",
                              hx_get="/restart",
                              hx_target="#game-container",
                              hx_swap="innerHTML",
                              style="background: #e74c3c; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; margin: 10px;",
                          ),
                          Button(
                              "🗺️ Story Map",
                              hx_get="/map",
                              hx_target="#game-container",
                              hx_swap="innerHTML",
                              style="background: #95a5a6; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; margin: 10px;",
                          ),
                      ],
                      style="text-align: center; margin-top: 20px;"
                  )
   )

def create_fragments_display(session):
    """Create the fragments display section"""
    if not session["code_fragments"]:
        return Div()

    fragment_codes = [SECRET_CODE_FRAGMENTS[frag_id]["code_piece"] 
                     for frag_id in session["code_fragments"]]

    return Div(
        H4("🔍 Code Fragments Discovered:", style="color: #9b59b6; margin-bottom: 15px;"),
        Div(
            *[Span(code, class_="code-fragment") for code in fragment_codes],
            style="margin-bottom: 15px;"
        ),
        P(f"Progress: {len(session['code_fragments'])}/4 fragments found"),
        P("💡 Combine all fragments to form the secret path: /word1-word2-word3-word4", 
          style="font-style: italic; color: #7f8c8d;") if len(session['code_fragments']) >= 2 else "",
        P("🚪 Navigate to: /shadow-nexus-gate-walker when you have all 4!", 
          style="font-weight: bold; color: #e74c3c;") if len(session['code_fragments']) >= 3 else "",
        class_="fragments-container"
    )

def create_progress_indicator(session):
    """Create progress indicator"""
    if len(session["story_path"]) <= 1:
        return Div()

    return Div(
        H4("Your Journey:"),
        P(" → ".join([STORY_NODES.get(n, {"title": "Unknown"})["title"] 
                     for n in session["story_path"] if n in STORY_NODES])),
        class_="progress-indicator"
    )

# HTMX endpoint for making choices
@rt("/make-choice")
def make_choice(choice: str, current_node: str, session_id: str = "default"):
    # Find the next node based on choice
    node_data = STORY_NODES.get(current_node)
    if not node_data:
        return story_content_only("start", session_id)

    next_node = None
    choice_text = ""

    for choice_option in node_data["choices"]:
        if choice_option["choice_id"] == choice:
            next_node = choice_option["next"]
            choice_text = choice_option["text"]
            break

    if next_node and next_node in STORY_NODES:
        # Update session
        update_user_session(session_id, next_node, {
            "choice_id": choice,
            "choice_text": choice_text,
            "from_node": current_node
        })
        return story_content_only(next_node, session_id)
    else:
        # Handle ending
        return ending_content(choice, session_id)

def story_content_only(node, session_id):
    """Return just the story content for HTMX updates"""
    session = get_user_session(session_id)
    current_node = STORY_NODES.get(node, STORY_NODES["start"])

    story_content = make_words_clickable(current_node["content"], node, session)

    choice_buttons = []
    for choice in current_node["choices"]:
        choice_buttons.append(
            Button(
                choice["text"],
                hx_post="/make-choice",
                hx_vals=json.dumps({
                    "choice": choice["choice_id"],
                    "current_node": node,
                    "session_id": session_id
                }),
                hx_target="#game-container",
                hx_swap="innerHTML",
                style="display: block; width: 100%; margin: 10px 0; padding: 15px; text-align: left; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; transition: all 0.3s ease;",
                _="on mouseenter add .hover-effect to me on mouseleave remove .hover-effect from me"
            )
        )

    return Div(
        H2(current_node["title"], style="color: #34495e; margin-bottom: 20px;"),
        Div(Raw(story_content), class_="story-content"),
        Div(id="secret-response", style="min-height: 20px;"),
        create_fragments_display(session),
        Div(*choice_buttons, style="margin: 30px 0;"),
        create_progress_indicator(session)
    )

# HTMX endpoint for discovering fragments
@rt("/discover-fragment/{fragment_id}")
def discover_fragment(fragment_id: str, session_id: str = "default"):
    session = get_user_session(session_id)

    if (fragment_id in SECRET_CODE_FRAGMENTS and 
        fragment_id not in session["code_fragments"]):

        session["code_fragments"].append(fragment_id)
        fragment = SECRET_CODE_FRAGMENTS[fragment_id]

        return Div(
            f"🎉 {fragment['discovery_text']}",
            Br(),
            f"Code Fragment: ",
            Span(fragment['code_piece'], class_="code-fragment"),
            Br(),
            f"Progress: {len(session['code_fragments'])}/4 fragments found",
            class_="secret-response",
            hx_get=f"/update-fragments/{session_id}",
            hx_target=".fragments-container",
            hx_swap="outerHTML",
            hx_trigger="load delay:2s"
        )

    return Div("Already discovered!", class_="secret-response")

# Update fragments display
@rt("/update-fragments/{session_id}")
def update_fragments(session_id: str):
    session = get_user_session(session_id)
    return create_fragments_display(session)

# Restart functionality
@rt("/restart") 
def restart():
    new_session_id = f"new_{hash('restart')}_{datetime.now().timestamp()}"[:16]
    return story_content_only("start", new_session_id)

# Secret ending
@rt("/shadow-nexus-gate-walker")
def secret_ending():
    return Titled("🌟 SECRET ENDING UNLOCKED! 🌟",
        Style("""
            .secret-ending {
                background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 60px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                margin: 40px auto;
                max-width: 800px;
                animation: secretGlow 2s ease-in-out infinite alternate;
            }

            @keyframes secretGlow {
                from { box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
                to { box-shadow: 0 20px 60px rgba(155, 89, 182, 0.4); }
            }
        """),

        Div(
            H1("🎊 CONGRATULATIONS! 🎊", style="font-size: 3.5em; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);"),
            H2("Shadow Nexus Gate Walker", style="margin-bottom: 40px; font-size: 2.2em;"),
            P("""You have successfully uncovered the deepest secret of the Nexus! 

By discovering all four code fragments hidden throughout the multiverse, you've proven yourself worthy of the ultimate title: Shadow Nexus Gate Walker.

You now possess the power to traverse between all realities at will. The portals bend to your command, and the very fabric of the multiverse recognizes your mastery.

This secret ending is reserved for the most dedicated explorers who look beyond the surface narrative and piece together the hidden mysteries.""", 
              style="font-size: 18px; line-height: 2; margin-bottom: 40px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);"),

            H3("🏆 Achievement Unlocked: Master of the Nexus", style="color: gold; font-size: 1.8em; margin: 30px 0;"),
            P("You've completed the secret ARG layer!", style="font-size: 16px; margin-bottom: 40px;"),

            Div(
                A("🔄 Begin New Adventure", href="/", 
                  style="background: rgba(255,255,255,0.2); color: white; padding: 20px 40px; text-decoration: none; border-radius: 30px; margin: 15px; display: inline-block; backdrop-filter: blur(10px); font-size: 18px; transition: all 0.3s ease;"),
                A("🏅 View Certificate", href="/certificate",
                  style="background: rgba(255,255,255,0.2); color: white; padding: 20px 40px; text-decoration: none; border-radius: 30px; margin: 15px; display: inline-block; backdrop-filter: blur(10px); font-size: 18px; transition: all 0.3s ease;"),
                style="margin-top: 40px;"
            ),

            class_="secret-ending"
        )
    )

def ending_content(choice, session_id):
    """Generate ending content"""
    session = get_user_session(session_id)

    endings = {
        "dragongem": "You take the Dragon's heart and grip it tightly. The power flows through your veins as you transform and reclaim your throne. Ending: Tyrant of Flame 🔥",
        "nodragongem": "You shatter the dragon's heart, breaking the cycle of violence. Peace may finally be possible. Ending: The Final Peacekeeper 🌿",
        "executed": "Your harsh justice instills fear but ensures victory. History turns by blood alone. Ending: Blade of Justice ⚔️",
        "noexecuted": "The traitor's intel leads to victory without unnecessary bloodshed. Ending: The Rat Repays Its Debtors 🐀"
    }

    ending_text = endings.get(choice, "The End.")

    return Div(
        H2("The End", style="color: #e74c3c; font-size: 2.5em; text-align: center; margin-bottom: 30px;"),
        P(ending_text, style="font-size: 20px; line-height: 1.8; margin: 40px 0; text-align: center;"),

        H3("Your Journey:", style="color: #34495e; margin: 30px 0 20px 0;"),
        Ul(*[Li(f"{choice['from_node']} → {choice['choice_text']}")
             for choice in session["choices_made"]], 
           style="font-size: 16px; line-height: 1.6;"),

        Div(
            Button("🔄 New Adventure", 
                   hx_get="/restart",
                   hx_target="#game-container",
                   hx_swap="innerHTML",
                   style="background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 8px; cursor: pointer; font-size: 18px; margin: 20px 10px;"),
            style="text-align: center; margin-top: 40px;"
        )
    )

serve()