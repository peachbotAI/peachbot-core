from core.audit.logger import log_event


def handle_decision(alert):
    print("\n⚠️  SAFETY ALERT:")
    print(alert["level"], "-", alert["message"])

    decision = input("\nEnter decision (ack / override): ").strip().lower()

    if decision not in ["ack", "override"]:
        print("Invalid input. Defaulting to acknowledgment.")
        decision = "ack"

    reason = ""

    if decision == "override":
        reason = input("Enter override reason: ")

    log_event({
        "alert": alert,
        "decision": decision,
        "reason": reason
    })

    return {
        "decision": decision,
        "reason": reason
    }