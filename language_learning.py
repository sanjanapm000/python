import random

words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "buenos días", "english": "good morning"},
    {"spanish": "buenas tardes", "english": "good afternoon"},
    {"spanish": "buenas noches", "english": ["good evening" ," good night"]},
    {"spanish": "agua", "english": "water"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "perro", "english": "dog"},
    {"spanish": "gato", "english": "cat"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "bebida", "english": "drink"},
    {"spanish": "ropa", "english": "clothes"},
    {"spanish": "dinero", "english": "money"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "libro", "english": "book"},
    {"spanish": "televisión", "english": "television"},
    {"spanish": "teléfono", "english": "telephone"},
    {"spanish": "computadora", "english": "computer"},
    {"spanish": "internet", "english": "internet"},
    {"spanish": "ciudad", "english": "city"},
    {"spanish": "país", "english": "country"},
    {"spanish": "playa", "english": "beach"},
    {"spanish": "montaña", "english": "mountain"},
    {"spanish": "sol", "english": "sun"},
    {"spanish": "luna", "english": "moon"},
    {"spanish": "estrella", "english": "star"},
    {"spanish": "aire", "english": "air"},
    {"spanish": "fuego", "english": "fire"},
    {"spanish": "tierra", "english": "earth"},
    {"spanish": "planta", "english": "plant"},
    {"spanish": "animal", "english": "animal"},
    {"spanish": "persona", "english": "person"},
    {"spanish": "música", "english": "music"},
    {"spanish": "arte", "english": "art"},
    {"spanish": "película", "english": "movie"},
    {"spanish": "juego", "english": "game"},
    {"spanish": "deporte", "english": "sport"},
    {"spanish": "bicicleta", "english": "bicycle"},
    {"spanish": "automóvil", "english": "car"},
    {"spanish": "autobús", "english": "bus"},
    {"spanish": "tren", "english": "train"},
    {"spanish": "avión", "english": "airplane"},
    {"spanish": "barco", "english": "ship"},
    {"spanish": "caminar", "english": "to walk"},
    {"spanish": "correr", "english": "to run"},
    {"spanish": "nadar", "english": "to swim"},
    {"spanish": "saltar", "english": "to jump"},
    {"spanish": "dormir", "english": "to sleep"},
    {"spanish": "comer", "english": "to eat"},
    {"spanish": "beber", "english": "to drink"},
    {"spanish": "hablar", "english": "to talk"},
    {"spanish": "escuchar", "english": "to listen"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "mirar", "english": "to watch"},
    {"spanish": "leer", "english": "to read"},
    {"spanish": "escribir", "english": "to write"},
    {"spanish": "aprender", "english": "to learn"},
    {"spanish": "enseñar", "english": "to teach"},
    {"spanish": "trabajar", "english": "to work"},
    {"spanish": "estudiar", "english": "to study"},
    {"spanish": "viajar", "english": "to travel"},
    {"spanish": "amar", "english": "to love"},
    {"spanish": "odiar", "english": "to hate"},
    {"spanish": "sentir", "english": "to feel"},
    {"spanish": "pensar", "english": "to think"},
    {"spanish": "creer", "english": "to believe"},
    {"spanish": "saber", "english": "to know"},
    {"spanish": "entender", "english": "to understand"},
    {"spanish": "querer", "english": "to want"},
    {"spanish": "necesitar", "english": "to need"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "estar", "english": "to be (temporary)"},
    {"spanish": "ser", "english": "to be (permanent)"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "venir", "english": "to come"},
    {"spanish": "poder", "english": ["to be able to "," can"]},
    {"spanish": "deber", "english": ["to must" ," should"]},
    {"spanish": "poner", "english": "to put"},
    {"spanish": "quitar", "english": "to remove"},
    {"spanish": "tomar", "english": "to take"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "recibir", "english": "to receive"},
    {"spanish": "buscar", "english": "to search"},
    {"spanish": "encontrar", "english": "to find"},
    {"spanish": "perder", "english": "to lose"},
    {"spanish": "ganar", "english": "to win"},
    {"spanish": "comprar", "english": "to buy"},
    {"spanish": "vender", "english": "to sell"},
    {"spanish": "pagar", "english": "to pay"},
    {"spanish": "costar", "english": "to cost"},
    {"spanish": "hacer", "english": ["to do" ," to make"]},
    {"spanish": "decir", "english": "to say"},
    {"spanish": "preguntar", "english": "to ask"},
    {"spanish": "contestar", "english": "to answer"},
    {"spanish": "olvidar", "english": "to forget"},
    {"spanish": "recordar", "english": "to remember"},
    {"spanish": "esperar", "english": ["to wait" ," to hope"]},
    {"spanish": "salir", "english": ["to leave" ," to go out"]},
    {"spanish": "entrar", "english": "to enter"},
    {"spanish": "abrir", "english": "to open"},
    {"spanish": "cerrar", "english": "to close"},
    {"spanish": "empezar", "english": ["to start" ," to begin"]},
    {"spanish": "terminar", "english": ["to finish ", "to end"]},
    {"spanish": "ayudar", "english": "to help"},
    {"spanish": "cuidar", "english": "to take care of"},
    {"spanish": "tocar", "english": ["to touch "," to play (an instrument)"]},
    {"spanish": "cantar", "english": "to sing"},
    {"spanish": "bailar", "english": "to dance"},
    {"spanish": "reír", "english": "to laugh"},
    {"spanish": "llorar", "english": "to cry"},
    {"spanish": "besar", "english": "to kiss"},
    {"spanish": "abrazar", "english": "to hug"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong , The correct answer is'{word['english']}'.\n")
        print(f"Quiz complete! Your score: {score}/{len(words)}")
        reply = input("Do you want to continue (Y/N)? ").upper()
        if reply == "N":
            break




def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz..")
    quiz_user(words)



if __name__ == '__main__':
     main()


