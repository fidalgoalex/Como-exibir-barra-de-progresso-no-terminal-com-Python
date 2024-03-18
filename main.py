from tqdm import tqdm
import time

# Número de iterações no loop
total_iterations = 100

# Usando tqdm para criar uma barra de progresso
for i in tqdm(range(total_iterations)):
    # Simulando algum trabalho com um pequeno atraso
    time.sleep(0.1)

print("Sucesso!")
