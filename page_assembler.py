import json
import os

def assemble_pages(product, questions):
    os.makedirs("output", exist_ok=True)

    product_page = {
        "product_name": product["name"],
        "concentration": product["concentration"],
        "skin_type": product["skin_type"],
        "key_ingredients": product["key_ingredients"],
        "benefits": product["benefits"],
        "how_to_use": product["how_to_use"],
        "side_effects": product["side_effects"],
        "price": product["price"]
    }

    with open("output/product_page.json", "w") as f:
        json.dump(product_page, f, indent=2)

    with open("output/faq.json", "w") as f:
        json.dump(questions, f, indent=2)

