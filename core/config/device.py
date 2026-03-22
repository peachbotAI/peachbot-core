import platform


def detect_device():
    system = platform.system()

    # Detect architecture
    machine = platform.machine().lower()

    # Windows / macOS → PC
    if system in ["Windows", "Darwin"]:
        return "pc"

    # Linux split (simple heuristic)
    if system == "Linux":
        if "arm" in machine or "aarch" in machine:
            return "sbc"
        else:
            return "pc"

    return "pc"


def get_capabilities(device):
    if device == "micro":
        return {
            "mode": "lightweight",
            "modules": ["eco", "agri"],
            "ml": False,
            "ui": "minimal"
        }

    elif device == "sbc":
        return {
            "mode": "edge",
            "modules": ["medai", "eco", "agri", "bio"],
            "ml": False,
            "ui": "cli"
        }

    elif device == "pc":
        return {
            "mode": "full",
            "modules": ["medai", "eco", "agri", "bio"],
            "ml": True,
            "ui": "enhanced"
        }

    elif device == "soc":
        return {
            "mode": "accelerated",
            "modules": ["medai", "eco", "agri", "bio"],
            "ml": True,
            "ui": "embedded"
        }