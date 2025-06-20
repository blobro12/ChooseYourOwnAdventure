from fasthtml.common import *
from story_data import STORY_NODES
from ending_data import endings

app, rt = fast_app()
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
#Actual Map Page including Requirements and Items
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
    #Story Map Layout
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