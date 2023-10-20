def simple_chatbot():
    print("CHATBOT:Hello,I am ur chatbot!,How could i help you?")
    
    while True:
        user_input=input("YOU:")
        
        if  user_input.lower()=="hello":
            print("CHATBOT:Wassup!,What's on your agenda today?")
            
        elif user_input.lower()=="ntg":
             print("CHATBOT:Cool, a chill day then!ENjoy ur downtime")
            
        
        elif user_input.lower()=="who are you":
            print("CHATBOT:I'm a chatbot.")

        elif user_input.lower()=="yep":
             print("NIce to know")
            
        elif user_input.lower()=="about ai":
                print("CHATBOT:AI or artificial intelligence, is a tech field that focuses on creating smart machines.Cool,right?")
            
        elif user_input.lower()=="bye":
            print("CHATBOT:Have a good day,Catch you later!")
        
        
        
        
        else:
            print("CHATBOT:I'm sorry, I didn't understand that. Please ask another question.")
            
simple_chatbot()
