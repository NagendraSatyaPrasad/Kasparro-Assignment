import json
from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

class OrchestratorAgent:
    def run(self):
        raw = json.load(open("data/product_input.json"))

        product = ProductParserAgent().run(raw)
        questions = QuestionGenerationAgent().run(product)
        logic = ContentLogicAgent()

        faq = FAQPageAgent().run(questions, product, logic)
        product_page = ProductPageAgent().run(product, logic)
        comparison = ComparisonPageAgent().run(product)

        json.dump(faq, open("outputs/faq.json", "w"), indent=2)
        json.dump(product_page, open("outputs/product_page.json", "w"), indent=2)
        json.dump(comparison, open("outputs/comparison_page.json", "w"), indent=2)
