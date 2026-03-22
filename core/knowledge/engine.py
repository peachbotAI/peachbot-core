class KnowledgeEngine:
    def __init__(self, loader):
        self.loader = loader

    def _match_conditions(self, signal, conditions):
        for key, value in conditions.items():

            if key not in signal:
                return False

            signal_value = signal[key]

            # handle list comparison
            if isinstance(value, list) and isinstance(signal_value, list):
                if sorted(signal_value) != sorted(value):
                    return False
            else:
                if signal_value != value:
                    return False

        return True

    def match_rules(self, signal, rules):
        matched = []

        for rule in rules:
            conditions = rule.get("conditions", {})

            if self._match_conditions(signal, conditions):
                matched.append(rule)

        return matched

    def enrich(self, signal, domain):
        rules = self.loader.load(domain)
        matched_rules = self.match_rules(signal, rules)

        # Default enrichment (always present → no downstream break)
        enrichment = {
            "knowledge_tags": [],
            "knowledge_weight": 0,
            "knowledge_notes": []
        }

        for rule in matched_rules:
            enrichment["knowledge_tags"].extend(rule.get("tags", []))
            enrichment["knowledge_weight"] += rule.get("weight", 0)

            note = rule.get("note")
            if note:
                enrichment["knowledge_notes"].append(note)

        # Non-destructive merge
        enriched_signal = signal.copy()
        enriched_signal["knowledge"] = enrichment

        return enriched_signal