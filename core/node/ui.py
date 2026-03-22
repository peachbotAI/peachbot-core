from colorama import Fore, Style, init

init(autoreset=True)


# ==============================
# SECTION HELPERS
# ==============================

def print_section(title):
    print(Fore.CYAN + Style.BRIGHT + f"\n=== {title} ===")


def print_divider():
    print(Fore.BLUE + "-" * 50)


# ==============================
# STATE DISPLAY
# ==============================

def print_state(state):
    print_section("CLINICAL STATE")

    symptoms = state.get("symptoms", [])
    severity = state.get("severity", "unknown")

    print(Fore.WHITE + f"Symptoms : {', '.join(symptoms) if symptoms else 'None'}")
    print(Fore.WHITE + f"Severity : {severity}")


# ==============================
# SAFETY ALERT
# ==============================

def print_alert(alert):
    print_section("SAFETY EVALUATION")

    level = alert.get("level", "INFO")

    if level == "CRITICAL":
        color = Fore.RED + Style.BRIGHT
    elif level == "WARNING":
        color = Fore.YELLOW + Style.BRIGHT
    else:
        color = Fore.GREEN

    print(color + f"[{level}] {alert.get('message', '')}")


# ==============================
# CONFIDENCE
# ==============================

def print_confidence(confidence):
    print(Fore.MAGENTA + Style.BRIGHT + f"\n🧠 Confidence: {confidence}")


# ==============================
# SIGNAL ATTRIBUTION
# ==============================

def print_attribution(attribution):
    print_section("SIGNAL ATTRIBUTION")

    if not attribution:
        print(Fore.WHITE + "No contributing signals")
        return

    for item in attribution:
        typ = item.get("type", "unknown")
        source = item.get("source", "unknown")
        weight = item.get("weight", 0)

        # Color coding
        if typ == "clinical":
            color = Fore.GREEN
        elif typ == "knowledge":
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        print(color + f" - [{typ}] {source} (weight: {weight})")


# ==============================
# CONTEXT DISPLAY
# ==============================

def print_context(context):
    print("\n SBC CONTEXT")

    if "active_keys" in context:
        print(f"Active Signals : {context['active_keys']}")

    if "history_length" in context:
        print(f"History Length : {context['history_length']}")

    if "relation_count" in context:
        print(f"Relations      : {context.get('relation_count', 0)}")

    if "priority_score" in context:
        print(f"Priority Score : {context.get('priority_score', 0)}")


# ==============================
# DECISION DISPLAY
# ==============================

def print_decision(decision):
    print_section("PHYSICIAN DECISION")

    if decision.get("decision") == "override":
        print(Fore.MAGENTA + f"Override applied")
        print(Fore.WHITE + f"Reason: {decision.get('reason', '')}")
    else:
        print(Fore.GREEN + "Acknowledged")