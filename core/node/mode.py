def select_mode():
    print("\nSelect System Mode:")
    print("1. MedAI   (Clinical Intelligence)")
    print("2. Eco     (Environmental Intelligence)")
    print("3. AgriAI  (Agricultural Intelligence)")
    print("4. Bio     (Bioinformatics / GNN Systems)")

    choice = input("\nEnter choice (1/2/3/4): ").strip()

    if choice == "2":
        return "eco"
    elif choice == "3":
        return "agri"
    elif choice == "4":
        return "bio"
    else:
        return "medai"