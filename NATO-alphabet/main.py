import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# student_dict=student_data_frame.to_dict()


student_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

while input("Run?") == "yes":
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    user_input = input("Enter a Word! ").upper()

    answer_list = [student_dict[word] for word in user_input]

    print(answer_list)
