from backend.FST.FstController import *


# Luego, puedes procesar el texto con tu función process_text_with_fst


def menu():
    print("Select an option:")
    print("1. Change verb tenses (simple present to simple past)")
    print("2. Change verb tenses (simple past to simple present)")
    print("3. Change verb tenses (simple present to simple future)")
    print("4. Change verb tenses (simple present to present continuous)")
    print("5. Change pronouns to 'I'")
    print("6. Change pronouns to 'you'")
    print("7. Change pronouns to 'he'")
    print("8. Change pronouns to 'she'")
    print("9. Change pronouns to 'it'")
    print("10. Change pronouns to 'we'")
    print("11. Change pronouns to 'they'")
    print("12. Apply synonyms")
    print("13. Apply antonyms")
    print("0. Exit")


def main():
    original_text = """Hi this is a history interestiting because she writes about the best text in the world. He accepts the contract."""
    current_text = original_text

    while True:
        print("\nCurrent text:", current_text)
        menu()
        option = input("Enter the number of your option: ")

        if option == '0':
            print("Exiting...")
            break

        fst = None
        if option == '1':
            fst = create_fst_present_to_past_simple()

        elif option == '2':
            pass
            # fst = create_fst_past_simple_to_present_simple()

        elif option == '3':
            fst = create_fst_present_to_future_simple()

        elif option == '4':
            fst = create_fst_present_to_continuous()

        elif option == '5':
            fst = create_fst_pronouns_to_i()
        elif option == '6':
            fst = create_fst_pronouns_to_you()
        elif option == '7':
            fst = create_fst_pronouns_to_he()
        elif option == '8':
            fst = create_fst_pronouns_to_she()
        elif option == '9':
            fst = create_fst_pronouns_to_it()
        elif option == '10':
            fst = create_fst_pronouns_to_we()
        elif option == '11':
            fst = create_fst_pronouns_to_they()

        elif option == '12':
            fst = transformate_synonyms()

        elif option == '13':
            fst = transformate_antonyms()

        else:
            print("Invalid option. Try again.")
            continue

        if fst:
            current_text = process_text_with_fst(fst, current_text)
            print("Transformed text:", current_text)

        continue_option = input("Do you want to make another transformation? (y/n): ")
        if continue_option.lower() != 'y':
            break

    print("Final text:", current_text)


# Run the main program
if __name__ == "__main__":
    main()
