class ProductPageAgent:
    def run(self, product, logic):
        return {
            "page_type": "PRODUCT",
            "product_name": product["name"],
            "summary": logic.build_summary(product),
            "ingredients": product["ingredients"],
            "benefits": logic.build_benefits(product["benefits"]),
            "usage": logic.build_usage(product["usage"]),
            "safety_information": logic.build_safety(product["side_effects"]),
            "price": logic.build_price(product["price"])
        }
