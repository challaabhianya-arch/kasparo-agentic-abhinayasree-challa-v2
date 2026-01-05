from src.data_parser import parse_product_data
from src.question_generator import generate_questions
from src.page_assembler import assemble_pages

def main():
    product = parse_product_data()
    questions = generate_questions(product)
    assemble_pages(product, questions)
    print("✅ Output files generated in /output folder")

if __name__ == "__main__":
    main()


    