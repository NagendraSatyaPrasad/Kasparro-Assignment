class ProductParserAgent:
    def run(self, raw_data):
        return {
            "name": raw_data["Product Name"],
            "concentration": raw_data["Concentration"],
            "skin_type": [s.strip() for s in raw_data["Skin Type"].split(",")],
            "ingredients": [i.strip() for i in raw_data["Key Ingredients"].split(",")],
            "benefits": [b.strip() for b in raw_data["Benefits"].split(",")],
            "usage": raw_data["How to Use"],
            "side_effects": raw_data["Side Effects"],
            "price": raw_data["Price"]
        }
