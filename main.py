from fasthtml.common import *
import json
from datetime import datetime
from starlette.responses import HTMLResponse  # Adjust this import as per your requirement
# Then, in your function, replace Raw with HTMLResponse


app, rt = fast_app()

# Story/Decision Tree Structure
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
        """Rain drips down your window. These murders, more recently named the Half-Moon Murders, are seem the same. The victims all recieve a letter with four letters: ISYS. We're not sure what these letters mean yet, but we have gotten some leads. One of the foot officers claim that some folks around town could help us. Specifically, the docks, the hotel, and in the slums. Where should we start?""",
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
            "choice_id": "loud"
        }, {
            "text": "Further press the dock owner.",
            "next": "dockowner",
            "choice_id": "dockowner"
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
    },
}
def story_page():
    return HTMLResponse(f'<p style="line-height: 1.6; margin-bottom: 30px; white-space: pre-line;">{story_content}</p>')
user_sessions = {}

def get_user_session(session_id="default"):
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "current_node": "start",
            "choices_made": [],
            "story_path": ["start"]
        }
    return user_sessions[session_id]

def update_user_session(session_id, node_id, choice_made):
    session = get_user_session(session_id)
    session["current_node"] = node_id
    session["choices_made"].append(choice_made)
    session["story_path"].append(node_id)
    return session
SECRET_CODE_FRAGMENTS = {
    "fragment_1": {
        "code_piece": "shadow",
        "location": "dragons_heart", 
        "trigger_word": "journey",  # Word in dragons_heart story text
        "discovery_text": "The ancient runes on the cave wall glow briefly, revealing the word: 'SHADOW'",
        "hint": "You sense this word is part of something larger...",
        "sound": "mystical_chime"
    },
    "fragment_2": {
        "code_piece": "nexus", 
        "location": "echodiver",
        "trigger_word": "asleep",  # Word in echodiver story text
        "discovery_text": "The dream technology panel flickers and displays a cryptic message: 'NEXUS'",
        "hint": "This seems like a key piece of a puzzle...",
        "sound": "electronic_beep"
    },
    "fragment_3": {
        "code_piece": "gate",
        "location": "docks",
        "trigger_word": "letter",  # Word in docks story text
        "discovery_text": "You examine the victim's letter more closely and notice faint writing on the back: 'GATE'",
        "hint": "Three words... but how many more are there?",
        "sound": "discovery_bell"
    },
    "fragment_4": {
        "code_piece": "walker",
        "location": "noexecuted", 
        "trigger_word": "Debtors",  # Word in noexecuted ending text
        "discovery_text": "Hidden in the traitor's confession, you discover a coded message: 'WALKER'",
        "hint": "Four words now... try combining them to form a secret path!",
        "sound": "treasure_chime"
    }
}

def make_words_clickable(text, node_id, session_id, session):
    """Convert trigger words in story text to clickable elements"""
    # Find if this node has any secret fragments
    available_fragments = []
    for frag_id, frag_data in SECRET_CODE_FRAGMENTS.items():
        if (frag_data["location"] == node_id and 
            frag_id not in session["code_fragments"]):
            available_fragments.append((frag_id, frag_data))

    if not available_fragments:
        return text

    # Process each fragment
    for frag_id, frag_data in available_fragments:
        trigger_word = frag_data["trigger_word"]

        # Create clickable span for the trigger word (case insensitive)
        import re
        pattern = r'\b(' + re.escape(trigger_word) + r')\b'

        def replace_word(match):
            word = match.group(1)
            return f'<span class="secret-word" data-fragment="{frag_id}" data-session="{session_id}" data-node="{node_id}" data-sound="{frag_data["sound"]}" onclick="discoverSecretFragment(this)">{word}</span>'

        text = re.sub(pattern, replace_word, text, flags=re.IGNORECASE)

    return text

# User state tracking (in production, use a database)
user_sessions = {}

def get_user_session(session_id="default"):
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "current_node": "start",
            "choices_made": [],
            "story_path": ["start"],
            "code_fragments": [],  # Track found code pieces
            "secret_attempts": 0   # Track how many times they've tried
        }
    return user_sessions[session_id]

def update_user_session(session_id, node_id, choice_made):
    session = get_user_session(session_id)
    session["current_node"] = node_id
    session["choices_made"].append(choice_made)
    session["story_path"].append(node_id)
    return session

def create_progress_hints(session):
    """Create helpful hints based on progress"""
    fragment_count = len(session["code_fragments"])

    if fragment_count == 0:
        return P("🔍 Hint: Look for words that seem to shimmer with hidden meaning as you explore...", 
                style="font-style: italic; color: #9b59b6; font-size: 14px;")
    elif fragment_count == 1:
        return P("🧩 You've found your first piece! Keep exploring different story paths to find more fragments.", 
                style="font-style: italic; color: #27ae60; font-size: 14px;")
    elif fragment_count == 2:
        return P("🔗 Two fragments collected! Try combining them: /fragment1-fragment2-...", 
                style="font-style: italic; color: #f39c12; font-size: 14px;")
    elif fragment_count == 3:
        return P("⚡ Almost there! One more fragment to unlock the secret path!", 
                style="font-style: italic; color: #e74c3c; font-size: 14px;")
    else:
        return P("🚪 All fragments found! Navigate to: /shadow-nexus-gate-walker", 
                style="font-weight: bold; color: #8e44ad; font-size: 16px;")

# Modified story page with enhanced secret system
@rt("/story")
def story_page(node: str = "start", session_id: str = "default"):
    session = get_user_session(session_id)
    current_node = STORY_NODES.get(node, STORY_NODES["start"])

    # Process story content to make trigger words clickable
    story_content = make_words_clickable(current_node["content"], node, session_id, session)

    # Create choice buttons
    choice_buttons = []
    for choice in current_node["choices"]:
        choice_buttons.append(
            Button(
                choice["text"],
                type="submit",
                name="choice", 
                value=choice["choice_id"],
                style="display: block; width: 100%; margin: 10px 0; padding: 15px; text-align: left; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;"
            )
        )

    # Code fragments display
    fragments_display = ""
    if session["code_fragments"]:
        fragment_codes = [SECRET_CODE_FRAGMENTS[frag_id]["code_piece"].upper() 
                         for frag_id in session["code_fragments"]]

        fragments_display = Div(
            H4("🔍 Code Fragments Found:"),
            Div(
                *[Span(code, style="background: #34495e; color: white; padding: 5px 10px; margin: 0 5px; border-radius: 3px; font-family: monospace;") 
                  for code in fragment_codes]
            ),
            P(f"{len(session['code_fragments'])}/4 fragments discovered"),
            P("💡 Try combining these words to form a secret path: /word1-word2-word3-word4", 
              style="font-style: italic; color: #7f8c8d; font-size: 14px;") if len(session['code_fragments']) >= 2 else "",
            P("🚪 Enter the complete path in your browser's address bar!", 
              style="font-weight: bold; color: #e74c3c;") if len(session['code_fragments']) >= 3 else "",
            style="margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #9b59b6;"
        )

    return Titled(current_node["title"],
        # Enhanced CSS with sound and animation effects
        Style("""
            .secret-word {
                position: relative;
                cursor: pointer;
                transition: all 0.3s ease;
                color: #8e44ad;
                font-weight: bold;
                border-bottom: 2px dotted #9b59b6;
                padding: 2px 4px;
                border-radius: 3px;
            }

            .secret-word:hover {
                background: rgba(155, 89, 182, 0.1);
                color: #663399;
                text-shadow: 0 0 8px rgba(155, 89, 182, 0.6);
                transform: scale(1.05);
                box-shadow: 0 0 15px rgba(155, 89, 182, 0.3);
            }

            .secret-word.clicked {
                animation: secretReveal 0.8s ease-out;
                background: linear-gradient(45deg, #9b59b6, #8e44ad);
                color: white;
                border: none;
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
                padding: 2px 6px;
                border-radius: 3px;
                font-weight: bold;
            }

            .discovery-popup {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                z-index: 1000;
                max-width: 500px;
                text-align: center;
                border: 3px solid #9b59b6;
            }

            .discovery-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.7);
                z-index: 999;
            }
        """),

        # JavaScript for handling clicks and sound
        Script("""
            function discoverSecretFragment(element) {
                // Add clicked animation
                element.classList.add('clicked');

                // Create discovery popup
                showDiscoveryPopup(element);

                // Make AJAX call to register discovery
                const fragment = element.dataset.fragment;
                const sessionId = element.dataset.session;
                const node = element.dataset.node;

                fetch(`/discover_fragment_ajax?fragment=${fragment}&session_id=${sessionId}&node=${node}`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            // Remove clickability after discovery
                            element.onclick = null;
                            element.style.cursor = 'default';
                            element.title = 'Fragment already discovered';
                        }
                    })
                    .catch(error => console.error('Error:', error));
            }

            function showDiscoveryPopup(element) {
                const fragment = element.dataset.fragment;
                const fragmentData = {
                    'fragment_1': {
                        code: 'SHADOW',
                        text: 'The ancient runes on the cave wall glow briefly, revealing the word: SHADOW',
                        hint: 'You sense this word is part of something larger...'
                    },
                    'fragment_2': {
                        code: 'NEXUS',
                        text: 'The dream technology panel flickers and displays a cryptic message: NEXUS',
                        hint: 'This seems like a key piece of a puzzle...'
                    },
                    'fragment_3': {
                        code: 'GATE',
                        text: 'You examine the victim\\'s letter more closely and notice faint writing on the back: GATE',
                        hint: 'Three words... but how many more are there?'
                    },
                    'fragment_4': {
                        code: 'WALKER',
                        text: 'Hidden in the traitor\\'s confession, you discover a coded message: WALKER',
                        hint: 'Four words now... try combining them to form a secret path!'
                    }
                };

                const data = fragmentData[fragment];
                if (!data) return;

                // Create overlay
                const overlay = document.createElement('div');
                overlay.className = 'discovery-overlay';

                // Create popup
                const popup = document.createElement('div');
                popup.className = 'discovery-popup';
                popup.innerHTML = `
                    <h2 style="color: #9b59b6; margin-bottom: 20px;">🔍 Secret Fragment Discovered!</h2>
                    <p style="font-size: 16px; margin-bottom: 15px;">${data.text}</p>
                    <p style="margin-bottom: 10px;">Code Fragment: <span class="code-fragment">${data.code}</span></p>
                    <p style="font-style: italic; color: #7f8c8d; margin-bottom: 20px;">${data.hint}</p>
                    <button onclick="closeDiscoveryPopup()" style="background: #9b59b6; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">Continue Exploring</button>
                `;

                document.body.appendChild(overlay);
                document.body.appendChild(popup);

                // Auto-close after 5 seconds
                setTimeout(() => {
                    closeDiscoveryPopup();
                }, 5000);
            }

            function closeDiscoveryPopup() {
                const overlay = document.querySelector('.discovery-overlay');
                const popup = document.querySelector('.discovery-popup');
                if (overlay) overlay.remove();
                if (popup) popup.remove();

                // Refresh the page to update fragment display
                location.reload();
            }
        """),

        Div(
            H2(current_node["title"], style="color: #34495e; margin-bottom: 20px;"),

            # Story content with clickable words
            Div(
                # Use raw HTML for the processed content
                HTML(f'<p style="line-height: 1.6; margin-bottom: 30px; white-space: pre-line;">{story_content}</p>'),
                id="story-content"
            ),

            # Code fragments display
            fragments_display,

            # Choices form
            Form(
                *choice_buttons,
                Input(type="hidden", name="current_node", value=node),
                Input(type="hidden", name="session_id", value=session_id),
                action="/make_choice",
                method="post"
            ),

            # Hint for secret words
            P("👁️ Some words seem to shimmer with hidden meaning...", 
              style="font-style: italic; color: #9b59b6; font-size: 14px; margin-top: 20px;") if any(
                  frag["location"] == node and frag_id not in session["code_fragments"] 
                  for frag_id, frag in SECRET_CODE_FRAGMENTS.items()
              ) else "",

            style="max-width: 800px; margin: 0 auto; padding: 20px;"
        ),

        # Progress indicator
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

# AJAX endpoint for fragment discovery
@rt("/discover_fragment_ajax")
def discover_fragment_ajax(fragment: str, session_id: str, node: str):
    session = get_user_session(session_id)

    if fragment in SECRET_CODE_FRAGMENTS and fragment not in session["code_fragments"]:
        session["code_fragments"].append(fragment)
        return {"success": True, "fragments_found": len(session["code_fragments"])}

    return {"success": False}

# The secret ending route (players must navigate here manually)
@rt("/shadow-nexus-gate-walker")
def secret_ending():
    return Titled("The Hidden Path Revealed",
        Style("""
            .secret-success {
                background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
        """),
        Div(
            H1("🌟 CONGRATULATIONS! 🌟", style="font-size: 3em; margin-bottom: 20px;"),
            H2("You've discovered the Shadow Nexus Gate Walker!", style="margin-bottom: 30px;"),
            P("""You are one of the few who has uncovered the deepest secret of the Nexus. 

By piecing together the fragments scattered across dimensions, you've proven yourself worthy of the title: Shadow Nexus Gate Walker.

You now stand at the convergence of all realities, wielding the power to traverse between worlds at will. The portals are no longer barriers - they are doorways you command.

This ending is reserved for the truly dedicated explorers who look beyond the surface and piece together the hidden truths.""", 
              style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;"),

            H3("🏆 Achievement Unlocked: Master Detective"),
            P("You've completed the secret ARG (Alternate Reality Game) layer!"),

            Div(
                A("🔄 Start a New Journey", href="/restart", 
                  style="background: rgba(255,255,255,0.2); color: white; padding: 15px 30px; text-decoration: none; border-radius: 25px; margin: 10px; display: inline-block; backdrop-filter: blur(10px);"),
                A("📖 View Your Achievement", href="/achievement",
                  style="background: rgba(255,255,255,0.2); color: white; padding: 15px 30px; text-decoration: none; border-radius: 25px; margin: 10px; display: inline-block; backdrop-filter: blur(10px);"),
                style="margin-top: 30px;"
            ),

            class_="secret-success"
        )
    )

# Route to show achievement/certificate
@rt("/achievement")
def achievement():
    return Titled("Achievement Certificate",
        Style("""
            .certificate {
                background: white;
                border: 10px solid gold;
                padding: 40px;
                margin: 20px auto;
                max-width: 600px;
                text-align: center;
                box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
            }
        """),
        Div(
            H1("🏆 CERTIFICATE OF ACHIEVEMENT 🏆"),
            Hr(style="border: 2px solid gold; margin: 20px 0;"),
            H2("Shadow Nexus Gate Walker"),
            P("This certifies that the bearer has successfully:"),
            Ul(
                Li("Discovered all 4 hidden code fragments"),
                Li("Solved the secret path puzzle"), 
                Li("Navigated to the hidden ending manually"),
                Li("Demonstrated exceptional detective skills"),
                style="text-align: left; display: inline-block;"
            ),
            P(f"Completed on: {datetime.now().strftime('%B %d, %Y')}", 
              style="margin-top: 30px; font-style: italic;"),
            P("🌟 You are among the elite few who have mastered the Nexus! 🌟", 
              style="color: gold; font-weight: bold;"),
            class_="certificate"
        )
    )
@rt("/")
def get():
    return RedirectResponse("/story")

@rt("/make_choice")
def post(choice: str, current_node: str, session_id: str = "default"):
    # Find the next node based on choice
    node_data = STORY_NODES.get(current_node)
    if not node_data:
        return RedirectResponse("/story")

    next_node = None
    choice_text = ""

    for choice_option in node_data["choices"]:
        if choice_option["choice_id"] == choice:
            next_node = choice_option["next"]
            choice_text = choice_option["text"]
            break

    if next_node and next_node in STORY_NODES:
        # Update session
        update_user_session(
            session_id, next_node, {
                "choice_id": choice,
                "choice_text": choice_text,
                "from_node": current_node
            })
        return RedirectResponse(
            f"/story?node={next_node}&session_id={session_id}")
    else:
        # Handle ending or invalid choice
        return RedirectResponse(
            f"/ending?choice={choice}&session_id={session_id}")


@rt("/ending")
def ending_page(choice: str, session_id: str = "default"):
    session = get_user_session(session_id)

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
        
    }

    ending_text = endings.get(choice, "The End.")

    return Titled(
        "Actions always have Consequences...",
        Div(H2("The End.", style="color: #e74c3c;"),
            P(ending_text,
              style="font-size: 18px; line-height: 1.6; margin: 30px 0;"),
            H3("Your Choices:"),
            Ul(*[
                Li(f"{choice['from_node']} → {choice['choice_text']}")
                for choice in session["choices_made"]
            ]),
            Div(A(
                "Start New Adventure",
                href="/restart",
                style=
                "background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 10px;"
            ),
                A("View Story Map",
                  href="/map",
                  style=
                  "background: #95a5a6; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 10px;"
                  ),
                style="text-align: center; margin-top: 40px;"),
            style=
            "max-width: 800px; margin: 0 auto; padding: 20px; text-align: center;"
            ))


@rt("/restart")
def restart():
    # Clear session and start over
    return RedirectResponse("/story?session_id=new_" +
                            str(hash("restart"))[:8])


@rt("/map")
def story_map():
    # Visual representation of the story structure
    nodes_html = []
    for node_id, node_data in STORY_NODES.items():
        choices_list = [Li(choice["text"]) for choice in node_data["choices"]]
        nodes_html.append(
            Div(H4(f"{node_id}: {node_data['title']}"),
                P(node_data["content"][:100] +
                  ("..." if len(node_data["content"]) > 100 else "")),
                Ul(*choices_list),
                style=
                "border: 1px solid #bdc3c7; margin: 10px; padding: 15px; border-radius: 5px;"
                ))

    return Titled(
        "Story Map",
        Div(H2("Story Structure"),
            *nodes_html,
            A("Back to Story",
              href="/story",
              style="display: block; text-align: center; margin-top: 20px;"),
            style="max-width: 1200px; margin: 0 auto; padding: 20px;"))


serve()
