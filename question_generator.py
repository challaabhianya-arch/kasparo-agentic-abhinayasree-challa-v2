from typing import List, Dict


def generate_questions(product_data: Dict) -> List[str]:
    """
    Generates follow-up questions based on product data.
    This file is NOT run directly.
    It is used by other modules (orchestrator / logic_blocks).
    """

    questions = []

    product_name = product_data.get("name", "this product")
    category = product_data.get("category", "")
    price = product_data.get("price", None)
    features = product_data.get("features", [])

    # Generic questions
    questions.append(f"What would you like to know about {product_name}?")

    if category:
        questions.append(f"Are you looking for more options in {category}?")

    if price:
        questions.append(f"Is your budget around ₹{price}?")

    if features:
        questions.append("Which feature is most important to you?")

    questions.append("Would you like a comparison with similar products?")
    questions.append("Do you want to proceed with this product or explore more?")

    return questions
