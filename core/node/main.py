from core.node.banner import show_banner
from core.node.mode import select_mode
from core.io.input_handler import get_input
from core.node.ui import print_state, print_alert, print_decision, print_divider

from core.engine.runner import execute

from core.shared.session import start_session, add_record, save_session
from core.safety.physician import handle_decision
from core.node.descriptions import show_mode_info
from core.config.device import detect_device, get_capabilities


def run():
    # Boot screen
    show_banner()

    device = detect_device()
    capabilities = get_capabilities(device)

    print(f"Device Type : {device.upper()}")
    print(f"Mode        : {capabilities['mode']}")
    print(f"Modules     : {', '.join(capabilities['modules'])}")
    print(f"ML Support  : {'Yes' if capabilities['ml'] else 'No'}\n")

    # Select mode
    mode = select_mode()

    # Show mode info
    show_mode_info(mode)

    mode_names = {
        "medai": "MEDAI (Clinical)",
        "eco": "ECO (Environmental)",
        "agri": "AGRI (Agriculture)",
        "bio": "BIO (Bioinformatics)"
    }

    print(f"\nRunning: {mode_names.get(mode, mode)}\n")

    # Start session
    start_session()

    while True:
        # Get input (mode-aware)
        data = get_input(mode)

        # Exit condition
        if data["text"].lower() in ["exit", "quit"]:
            save_session()
            print("Session Ended")
            break

        # Execute selected module
        result = execute(mode, data)

        # --- DOMAIN-SPECIFIC OUTPUT ---
        if mode == "medai":
            print_state(result["state"])
            print_alert(result["alert"])

        elif mode == "eco":
            print("\n🌿 ECO SYSTEM STATE")
            print(result["state"])

            print("\n🌿 ECO ALERT")
            print(result["alert"]["message"])

        elif mode == "agri":
            print("\n🌾 AGRI SYSTEM STATE")
            print(result["state"])

            print("\n🌾 AGRI ALERT")
            print(result["alert"]["message"])

        elif mode == "bio":
            print("\n🧬 BIO SYSTEM STATE")
            print(result["state"])

            print("\n🧬 BIO INSIGHT")
            print(result["alert"]["message"])

        # --- DECISION (ONLY FOR MEDAI) ---
        decision = None

        if result.get("decision_required"):
            decision = handle_decision(result["alert"])
            print_decision(decision)

        # --- SESSION LOGGING ---
        add_record(data["text"], result["state"], result["alert"], decision)

        # --- UI ---
        print("\n(Type 'exit' to end session)")
        print_divider()


if __name__ == "__main__":
    run()