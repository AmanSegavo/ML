import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Definisi lingkungan
umur_tbs = [0, 1, 2, 3, 4, 5]  # Minggu 0-5
tanah_levels = ["kering", "normal", "basah"]
pupuk_levels = ["kurang", "cukup"]
cuaca = ["cerah", "hujan"]
harga_pasar = ["rendah", "normal", "tinggi"]

actions = ["panen", "tunda", "pupuk", "irigasi"]

# Inisialisasi Q-table
q_table = np.zeros((len(umur_tbs), len(tanah_levels), len(pupuk_levels), len(cuaca), len(harga_pasar), len(actions)))

# Parameter RL
alpha = 0.1   # Learning rate
gamma = 0.9   # Discount factor
epsilon = 0.1 # Probabilitas eksplorasi
episodes = 1000  # Jumlah latihan

# Fungsi memilih aksi (Eksplorasi vs Eksploitasi)
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, len(actions) - 1)  # Random
    return np.argmax(q_table[state])  # Pilih aksi terbaik

# Fungsi simulasi transisi keadaan
def step(state, action):
    umur, tanah, pupuk, cuaca_now, harga = state

    # Efek dari aksi
    if action == 0:  # Panen
        if umur < 3:  # Panen terlalu muda
            reward = -100
        else:
            reward = 50 + (harga * 50)  # Panen di harga tinggi lebih untung
            umur = 0  # Reset umur TBS setelah panen
    elif action == 1:  # Tunda Panen
        reward = 10
        if umur < 5:
            umur += 1
    elif action == 2:  # Pupuk
        pupuk = 1  # Pupuk jadi cukup
        reward = 20
    elif action == 3:  # Irigasi
        tanah = 1  # Tanah jadi normal
        reward = 30
    else:
        reward = -10

    # Perubahan cuaca dan harga pasar secara acak
    cuaca_now = random.choice([0, 1])
    harga = random.choice([0, 1, 2])

    return (umur, tanah, pupuk, cuaca_now, harga), reward

# **Latih AI untuk mengoptimalkan panen sawit**
for _ in range(episodes):
    state = (random.randint(0, 5), random.randint(0, 2), random.randint(0, 1), random.randint(0, 1), random.randint(0, 2))
    
    while True:
        action = choose_action(state)
        next_state, reward = step(state, action)
        q_table[state][action] = (1 - alpha) * q_table[state][action] + alpha * (reward + gamma * np.max(q_table[next_state]))
        
        if next_state[0] == 0:  # Jika umur kembali ke 0 (panen), reset episode
            break
        
        state = next_state

print("AI selesai belajar!")
