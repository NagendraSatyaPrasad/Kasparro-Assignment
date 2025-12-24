class QuestionGenerationAgent:
    def run(self, product):
        return {
            "Informational": [
                "What is " + product["name"] + "?",
                "What concentration does it have?"
            ],
            "Usage": [
                "How do I apply the serum?",
                "When should I use it?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is it suitable for sensitive skin?"
            ],
            "Purchase": [
                "What is the price of the product?"
            ],
            "Comparison": [
                "How does this compare with other serums?"
            ]
        }
