import time


class SBCState:
    def __init__(self):
        self.state = {}
        self.history = []
        self.relations = {}   # NEW: signal relationships

        self.decay_rate = 0.1

    def update(self, signal):
        current_time = time.time()

        for key, value in signal.items():

            weight = self._compute_weight(value)

            self.state[key] = {
                "value": value,
                "weight": weight,
                "timestamp": current_time
            }

        # NEW: update relationships
        self._update_relations(signal)

        self.history.append(signal)

    def _compute_weight(self, value):
        if value == "high":
            return 1.0
        elif value == "low":
            return 0.5
        return 0.7

    def _apply_decay(self, entry):
        age = time.time() - entry["timestamp"]
        return entry["weight"] * (1 / (1 + self.decay_rate * age))

    # ---------------------------
    # RELATION ENGINE
    # ---------------------------
    def _update_relations(self, signal):
        keys = list(signal.keys())

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                pair = tuple(sorted([keys[i], keys[j]]))

                if pair not in self.relations:
                    self.relations[pair] = 0

                self.relations[pair] += 1

    def get_state(self):
        computed = {}

        for key, entry in self.state.items():
            computed[key] = {
                "value": entry["value"],
                "effective_weight": round(self._apply_decay(entry), 3)
            }

        return computed

    def get_relations(self):
        return self.relations

    def get_context(self):
        return {
            "active_keys": len(self.state),
            "history_length": len(self.history),
            "relation_count": len(self.relations),
            "priority_score": self.compute_priority()
        }
    
    def compute_priority(self):
        """
        Compute overall system priority based on:
        - signal weights
        - number of active signals
        - interaction density
        """

        total_weight = 0

        for entry in self.state.values():
            total_weight += self._apply_decay(entry)

        signal_count = len(self.state)
        relation_count = len(self.relations)

        # simple composite score
        priority = total_weight * (1 + 0.2 * relation_count)

        return round(priority, 3)