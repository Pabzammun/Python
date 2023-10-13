secret_num = str(58)
selected_num = str((input("Select one number : ")))


if secret_num == selected_num :
    print ("WELL DONE, you guessed the number")
    

elif selected_num > secret_num :
    print ("UPSS!! YOU ARE CLOSE, THE NUMBER YOU ARE LOKING FOR IS SMALLER ")

elif selected_num < secret_num :
    print("UPSS!! YOU ARE CLOSE, THE NUMBER YOU ARE LOKING FOR IS BIGGER")