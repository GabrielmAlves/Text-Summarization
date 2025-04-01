from process_text import process_text

def main():
    user_text = input("Please, write down the text you want to summarize: ")
    summarized_text = process_text(user_text)

    print(f"Summarized text: {summarized_text}")
    
if __name__ == "__main__":
    main()