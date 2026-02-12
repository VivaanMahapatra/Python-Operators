def shutdown(choice):
    if choice == "Yes":
        print("Shutting down")
    elif choice == "No":
        print("Abort shutdown")
    else:
        print("Sorry")

user_input = input("Do you want to shutdown? (Yes/No): ")
shutdown(user_input)
