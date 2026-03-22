def show_mode_info(mode):
    print("\n==================================================")

    if mode == "medai":
        print("🩺 MEDAI — CLINICAL INTELLIGENCE SYSTEM\n")

        print("Description:")
        print("- Processes clinical inputs and symptoms")
        print("- Maintains structured patient state")
        print("- Performs tiered safety evaluation")
        print("- Supports physician acknowledgment and override")

        print("\nDisclaimer:")
        print("⚠️ This system is a decision-support tool only.")
        print("⚠️ It does NOT replace medical professionals.")
        print("⚠️ All outputs must be validated by a qualified physician.")

    elif mode == "eco":
        print("🌿 ECO — ENVIRONMENTAL INTELLIGENCE SYSTEM\n")

        print("Description:")
        print("- Monitors environmental conditions")
        print("- Detects pollution and ecosystem risks")
        print("- Supports real-time environmental insights")

        print("\nDisclaimer:")
        print("⚠️ Outputs are indicative and based on input signals.")
        print("⚠️ Field validation is required for critical decisions.")

    elif mode == "agri":
        print("🌾 AGRIAI — AGRICULTURAL INTELLIGENCE SYSTEM\n")

        print("Description:")
        print("- Analyzes agricultural conditions")
        print("- Detects soil, moisture, and pest risks")
        print("- Supports farm-level decision insights")

        print("\nDisclaimer:")
        print("⚠️ Recommendations are advisory in nature.")
        print("⚠️ Actual farm conditions may vary.")

    elif mode == "bio":
        print("🧬 BIO — BIOLOGICAL / GNN ANALYSIS SYSTEM\n")

        print("Description:")
        print("- Processes biological and molecular inputs")
        print("- Identifies graph-based interaction patterns")
        print("- Supports research-level insights (GNN-based)")

        print("\nDisclaimer:")
        print("⚠️ This module is for research and exploratory use only.")
        print("⚠️ Not intended for clinical or diagnostic decisions.")

    print("\n==================================================\n")