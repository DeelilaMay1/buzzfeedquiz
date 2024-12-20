def buzzfeed_quiz():
    print("Welcome to the 'Which Video Game is Your Favorite?' Quiz!")
    print("Answer these questions, and we'll guess your favorite video game!\n")

    
    print("Question 1: What's your favorite kind of snack?")
    print("1. Chips and Dip")
    print("2. Candy")
    print("3. Pizza")
    print("4. Sushi")
    snack = input("Enter the number of your choice: ")

    print("\nQuestion 2: What's your ideal vacation?")
    print("1. Exploring ancient ruins")
    print("2. A high-tech city adventure")
    print("3. A cozy getaway in the mountains")
    print("4. A tropical beach escape")
    vacation = input("Enter the number of your choice: ")

    print("\nQuestion 3: Pick a color:")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Yellow")
    color = input("Enter the number of your choice: ")

    print("\nQuestion 4: Which animal do you vibe with the most?")
    print("1. Wolf")
    print("2. Cat")
    print("3. Fox")
    print("4. Dragon")
    animal = input("Enter the number of your choice: ")

    # Logic to determine the result
    if snack == "1" and vacation == "1" and color == "1" and animal == "1":
        game = "The Legend of Zelda"
    elif snack == "2" and vacation == "2" and color == "2" and animal == "2":
        game = "Cyberpunk 2077"
    elif snack == "3" and vacation == "3" and color == "3" and animal == "3":
        game = "Stardew Valley"
    elif snack == "4" and vacation == "4" and color == "4" and animal == "4":
        game = "Skyrim"
    else:
        game = "Minecraft" 

    
    print(f"\nBased on your answers, your favorite video game might be: {game}!\n")

if __name__ == "__main__":
    buzzfeed_quiz()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('quiz.html')

@app.route('/result', methods=['POST'])
def result():
    # Collect user answers
    snack = request.form.get('snack')
    vacation = request.form.get('vacation')
    color = request.form.get('color')
    animal = request.form.get('animal')

    # Determine the result based on the answers
    if snack == "1" and vacation == "1" and color == "1" and animal == "1":
        game = "The Legend of Zelda"
    elif snack == "2" and vacation == "2" and color == "2" and animal == "2":
        game = "Cyberpunk 2077"
    elif snack == "3" and vacation == "3" and color == "3" and animal == "3":
        game = "Stardew Valley"
    elif snack == "4" and vacation == "4" and color == "4" and animal == "4":
        game = "Skyrim"
    else:
        game = "Minecraft"  # Default fallback

    return render_template('result.html', game=game)

if __name__ == "__main__":
    app.run(debug=True)

