MODULES = {
    "medai": "core.modules.medai.module",
    "eco": "core.modules.eco.module",
    "agri": "core.modules.agri.module",
    "bio": "core.modules.bio.module"
}


def load_module(name):
    import importlib
    module = importlib.import_module(MODULES[name])
    return module


def execute(mode, data):
    module = load_module(mode)
    return module.run(data)