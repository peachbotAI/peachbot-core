class AdaptiveEngine:
    def __init__(self, store, threshold=3):
        self.store = store
        self.threshold = threshold
        self.pattern_memory = {}

    def _pattern_key(self, data):
        """
        Extract pattern from pre-SBC signal
        """
        symptoms = tuple(sorted(data.get("symptoms", [])))
        severity = data.get("severity")

        return (symptoms, severity)


    def observe(self, data):
        key = self._pattern_key(data)

        if key not in self.pattern_memory:
            self.pattern_memory[key] = 0

        self.pattern_memory[key] += 1

        print("ADAPTIVE OBSERVE:", key, self.pattern_memory[key])

        # ALWAYS reinforce AFTER threshold
        if self.pattern_memory[key] >= self.threshold:
            self._create_rule(key)

        # Apply decay
        self.store.decay_weights()
        
    def _create_rule(self, key):
        symptoms, severity = key

        if not symptoms:
            return

        rule = {
            "conditions": {
                "symptoms": list(symptoms),
                "severity": severity
            },
            "tags": ["adaptive_pattern"],
            "weight": 1,
            "note": f"Learned pattern: {symptoms} with severity {severity}"
        }

        self.store.add_rule(rule)