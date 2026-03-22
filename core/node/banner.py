import platform
import psutil


def get_system_info():
    return {
        "os": platform.system(),
        "cpu": platform.processor(),
        "cores": psutil.cpu_count(logical=True),
        "ram": round(psutil.virtual_memory().total / (1024**3), 2)
    }


def show_banner():
    print(r"""
      ____                  _     ____        _   
     |  _ \ ___  __ _  ___ | |__ | __ )  ___ | |_ 
     | |_) / _ \/ _` |/ _ \| '_ \|  _ \ / _ \| __|
     |  __/  __/ (_| | (_) | | | | |_) | (_) | |_ 
     |_|   \___|\__,_|\___/|_| |_|____/ \___/ \__|

           DISTRIBUTED EDGE INTELLIGENCE PLATFORM
                  SBC FOR BIOLOGICAL SYSTEMS
    """)

    print("--------------------------------------------------")
    print("🧠 PeachBot Core — Multi-Domain Intelligence System")
    print("👤 Created by: Swapin Vidya")
    print("🏢 PeachBot Research & Innovation Lab")

    print("\n📄 Patent:")
    print("Edge-Based Clinical Intelligence via Graph Neural Networks")
    print("App No: 202541127477")

    print("\n🔒 System Mode:")
    print("Edge-native | Privacy-preserving | Distributed")

    info = get_system_info()

    print("\n⚙️ SYSTEM INFO")
    print(f"OS        : {info['os']}")
    print(f"CPU       : {info['cpu']}")
    print(f"Cores     : {info['cores']}")
    print(f"Memory    : {info['ram']} GB")

    print("\n🧩 CORE CONFIG")
    print("FILA        : Enabled (Federated Learning Layer)")
    print("SBC         : Active (Adaptive Biological Computation)")
    print("Edge-GNN    : Integration Layer (In Progress)")
    print("Orchestrator: Local Node Controller")

    print("\n🌐 ACTIVE DOMAINS")
    print("MedAI   | Eco   | AgriAI   | Bio")

    print("\n--------------------------------------------------\n")