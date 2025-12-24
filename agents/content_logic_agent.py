class ContentLogicAgent:

    def build_summary(self, product):
        return (
            f"{product['name']} is a {product['concentration']} serum suitable for "
            f"{', '.join(product['skin_type']).lower()} skin, designed to "
            f"{product['benefits'][0].lower()} and {product['benefits'][1].lower()}."
        )

    def build_benefits(self, benefits):
        return [f"Helps {b.lower()}" for b in benefits]

    def build_usage(self, usage):
        return {
            "step_1": "Apply 2–3 drops",
            "step_2": "Use in the morning",
            "step_3": "Apply before sunscreen"
        }

    def build_safety(self, side_effects):
        return f"Some users may experience {side_effects.lower()}."

    def build_price(self, price):
        return {
            "currency": "INR",
            "amount": price
        }

    def faq_answer(self, category, product):
        if category == "Usage":
            return product["usage"]
        if category == "Safety":
            return self.build_safety(product["side_effects"])
        if category == "Purchase":
            return f"The product is priced at ₹{product['price']}."
        return f"{product['name']} contains {', '.join(product['ingredients'])}."
