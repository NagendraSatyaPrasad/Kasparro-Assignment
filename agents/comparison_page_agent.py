class ComparisonPageAgent:
    def run(self, product):
        product_b = {
            "name": "RadiantFix Serum",
            "ingredients": ["Vitamin C"],
            "benefits": ["Skin brightening"],
            "price": 899
        }

        return {
            "page_type": "COMPARISON",
            "product_a": product,
            "product_b": product_b,
            "comparison": {
                "ingredients": "GlowBoost has more ingredients than Product B.",
                "benefits": "Both focus on skin brightening.",
                "price": "GlowBoost is more affordable."
            }
        }
