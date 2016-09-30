answers={"привет": "привет!", "как дела": "Очень хорошо. А у тебя?",
 "пока": "Еще увидимся!", "как погода у тебя": "Норм.", "пока": "Еще увидимся!"}
}
def get_answer(question, answers):
	return answers.get(question)

def ask_user(answers):
	while True:
		user_input = input("Скажи что-нибудь: ")
		answer = get_answer(user_input, answers)
		print(answer)

		if user_input == "пока":
			break	
if __name__ == '__main__':
	ask_user(answers)