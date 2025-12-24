class FAQPageAgent:
    def run(self, questions, product, logic):
        faqs = []
        for category, qs in questions.items():
            for q in qs:
                faqs.append({
                    "question": q,
                    "answer": logic.faq_answer(category, product)
                })
                if len(faqs) >= 5:
                    break
            if len(faqs) >= 5:
                break

        return {
            "page_type": "FAQ",
            "product_name": product["name"],
            "faqs": faqs
        }
