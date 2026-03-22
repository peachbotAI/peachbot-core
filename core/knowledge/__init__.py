from .loader import KnowledgeLoader
from .engine import KnowledgeEngine

from .adaptive.engine import AdaptiveEngine
from .adaptive.store import AdaptiveStore

_loader = KnowledgeLoader()
_engine = KnowledgeEngine(_loader)

# 🆕 Adaptive system
_adaptive_store = AdaptiveStore()
_adaptive_engine = AdaptiveEngine(_adaptive_store)


def enrich_with_knowledge(signal, domain):
    return _engine.enrich(signal, domain)


def adaptive_learn(state):
    """
    Called AFTER SBC update
    """
    _adaptive_engine.observe(state)