import json
import os


class AdaptiveStore:
    def __init__(self, path="knowledge/base/adaptive_medai.json"):
        self.path = path
        self.data = self._load()

        self.MAX_WEIGHT = 10
        self.MIN_WEIGHT = 1
        self.DECAY_RATE = 0.1

    def _load(self):
        if not os.path.exists(self.path):
            return []

        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    # 🔥 CRITICAL FIX — normalize conditions
    def _normalize_conditions(self, conditions):
        return {
            "symptoms": sorted(conditions.get("symptoms", [])),
            "severity": conditions.get("severity")
        }

    def add_rule(self, new_rule):
        new_cond = self._normalize_conditions(new_rule["conditions"])

        for rule in self.data:
            existing_cond = self._normalize_conditions(rule["conditions"])

            if existing_cond == new_cond:
                # 🔥 REINFORCEMENT (FIXED)
                current_weight = rule.get("weight", 1)

                # Use integer growth (clear + visible)
                new_weight = current_weight + 1

                rule["weight"] = min(new_weight, self.MAX_WEIGHT)

                rule["note"] = "Reinforced adaptive pattern"

                print("REINFORCING RULE → weight:", rule["weight"])  # DEBUG

                self.save()
                return

        # NEW RULE
        print("CREATING NEW RULE")  # DEBUG
        self.data.append(new_rule)
        self.save()

    def decay_weights(self):
        updated = False

        for rule in self.data:
            weight = rule.get("weight", 1)

            new_weight = max(self.MIN_WEIGHT, weight - self.DECAY_RATE)

            if new_weight != weight:
                rule["weight"] = round(new_weight, 2)
                updated = True

        if updated:
            self.save()