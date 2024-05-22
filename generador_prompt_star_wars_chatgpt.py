import random

# Definición de las técnicas de prompting que se van a aplicar
def apply_zero_shot():
    return "Provide a detailed analysis of the selected movie in the Star Wars series."

def apply_one_shot(example):
    return f"For example, describe the character development in '{example}'."

def apply_chain_of_thought():
    return "Step-by-step, break down the sequence of events in the chosen scene and explain their significance."

def apply_role_play():
    return "As a Jedi master, explain the importance of this movie to a young Padawan, focusing on key lessons."

def apply_react():
    return "Describe how the characters' decisions impact the plot and their personal growth."

# Solicitud de datos al usuario
def get_user_input():
    pelicula = input("Ingrese la película de Star Wars: ")
    ano = input("Ingrese el año de la película: ")
    personajes_principales = input("Ingrese los personajes principales (separados por comas): ")
    personajes_preferidos = input("Ingrese sus personajes preferidos (separados por comas): ")
    escena_favorita = input("Describa su escena favorita: ")
    tema = input("Ingrese el tema o mensaje principal de la película: ")
    detalles_adicionales = input("Ingrese cualquier detalle adicional: ")
    return pelicula, ano, personajes_principales, personajes_preferidos, escena_favorita, tema, detalles_adicionales

# Generación del prompt para ChatGPT
def generate_prompt(pelicula, ano, personajes_principales, personajes_preferidos, escena_favorita, tema, detalles_adicionales):
    prompt = f"You are an expert on Star Wars. Based on the following details, provide a comprehensive response using the techniques of Zero-Shot, One-Shot, Chain of Thought, Role Play, and ReAct.\n\n"
    prompt += f"Title: Star Wars - {pelicula}\n"
    prompt += f"Year: {ano}\n"
    prompt += f"Main Characters: {personajes_principales}\n"
    prompt += f"Favorite Characters: {personajes_preferidos}\n"
    prompt += f"Favorite Scene: {escena_favorita}\n"
    prompt += f"Theme/Message: {tema}\n"
    prompt += f"Additional Details: {detalles_adicionales}\n\n"
    
    # Aplicación de técnicas de prompting
    prompt += "Techniques to use in your response:\n"
    prompt += "1. Zero-Shot: " + apply_zero_shot() + "\n"
    prompt += "2. One-Shot: " + apply_one_shot(pelicula) + "\n"
    prompt += "3. Chain of Thought: " + apply_chain_of_thought() + "\n"
    prompt += "4. Role Play: " + apply_role_play() + "\n"
    prompt += "5. ReAct: " + apply_react() + "\n"
    
    return prompt

# Función principal
def main():
    pelicula, ano, personajes_principales, personajes_preferidos, escena_favorita, tema, detalles_adicionales = get_user_input()
    prompt = generate_prompt(pelicula, ano, personajes_principales, personajes_preferidos, escena_favorita, tema, detalles_adicionales)
    print("\nGenerated Prompt for ChatGPT:\n")
    print(prompt)

if __name__ == "__main__":
    main()
