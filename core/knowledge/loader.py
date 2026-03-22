import json
import os


class KnowledgeLoader:
    def __init__(self, base_path="knowledge/base"):
        self.base_path = base_path
        # REMOVE CACHE (causes stale knowledge issues)
        # self.cache = {}

    def _load_file(self, path):
        if not os.path.exists(path):
            return []

        try:
            with open(path, "r") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except Exception:
            return []

    def load(self, domain):
        """
        Load base + adaptive knowledge every time (no cache)
        Ensures adaptive learning is immediately reflected
        """

        # Base knowledge
        base_path = os.path.join(self.base_path, f"{domain}.json")

        # Adaptive knowledge
        adaptive_path = os.path.join(self.base_path, f"adaptive_{domain}.json")

        base_rules = self._load_file(base_path)
        adaptive_rules = self._load_file(adaptive_path)

        # Merge rules (adaptive appended → higher priority)
        merged_rules = base_rules + adaptive_rules

        return merged_rules