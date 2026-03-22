from colorama import Fore, Style, init

init(autoreset=True)

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


def print_section(title):
    print(Fore.CYAN + Style.BRIGHT + f"\n=== {title} ===")


def print_state(state):
    print_section("CLINICAL STATE")

    print(Fore.WHITE + f"Symptoms : {', '.join(state['symptoms']) if state['symptoms'] else 'None'}")
    print(Fore.WHITE + f"Severity : {state['severity']}")


def print_alert(alert):
    print_section("SAFETY EVALUATION")

    level = alert["level"]

    if level == "CRITICAL":
        color = Fore.RED + Style.BRIGHT
    elif level == "WARNING":
        color = Fore.YELLOW + Style.BRIGHT
    else:
        color = Fore.GREEN

    print(color + f"[{level}] {alert['message']}")


def print_decision(decision):
    print_section("PHYSICIAN DECISION")

    if decision["decision"] == "override":
        print(Fore.MAGENTA + f"Override applied")
        print(Fore.WHITE + f"Reason: {decision['reason']}")
    else:
        print(Fore.GREEN + "Acknowledged")


def print_divider():
    print(Fore.BLUE + "-" * 50)