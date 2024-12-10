import os
import random
import tkinter as tk
from tkinter import messagebox

# Configuração inicial do jogador
player = {
    'gold': 200,
    'inventory': [],
    'hp': 100,
    'damage': 10
}

# Configuração inicial dos inimigos
monsters = [
    {'name': 'Goblin', 'hp': 30, 'damage': 5},
    {'name': 'Orc', 'hp': 50, 'damage': 8},
    {'name': 'Dragão', 'hp': 100, 'damage': 15}
]

# Loja de itens
items = {
    'Espada Flamejante': {'price': 150, 'stats': 'dano: (60) / dano/p/s: (20) / defesa: (32)'},
    'Armadura de Reflexão': {'price': 120, 'stats': 'defesa: 50 / dano: (20% do dano recebido)'},
    'Poção da Invisibilidade G': {'price': 100, 'stats': 'tempo de invisibilidade (60s)'}
}

def update_status():
    status_label.config(text=f"Gold: {player['gold']} | HP: {player['hp']}")

def show_inventory():
    inventory_text = "\n".join(player['inventory']) if player['inventory'] else "Inventário vazio."
    messagebox.showinfo("Inventário", inventory_text)

def open_shop():
    shop_window = tk.Toplevel(root)
    shop_window.title("Loja")

    def buy_item(item_name):
        item = items[item_name]
        if player['gold'] >= item['price']:
            player['gold'] -= item['price']
            player['inventory'].append(item_name)
            update_status()            
            messagebox.showinfo("Compra realizada", f"Você comprou {item_name} por {item['price']} golds!")
        else:
            messagebox.showerror("Erro", "Você não tem gold suficiente!")

    for item_name, item_data in items.items():
        btn = tk.Button(shop_window, text=f"{item_name} - {item_data['price']} golds\n{item_data['stats']}", 
                        command=lambda name=item_name: buy_item(name))
        btn.pack(pady=5)

    tk.Button(shop_window, text="Fechar Loja", command=shop_window.destroy).pack(pady=10)

def battle():
    monster = random.choice(monsters)
    battle_window = tk.Toplevel(root)
    battle_window.title("Batalha")

    monster_hp = monster['hp']

    def attack():
        nonlocal monster_hp
        monster_hp -= player['damage']
        battle_log.insert(tk.END, f"Você causou {player['damage']} de dano ao {monster['name']}!\n")

        if monster_hp <= 0:
            reward = random.randint(20, 50)
            player['gold'] += reward
            update_status()
            battle_log.insert(tk.END, f"Você derrotou o {monster['name']} e ganhou {reward} golds!\n")
            tk.Button(battle_window, text="Fechar", command=battle_window.destroy).pack(pady=10)
            return

        player['hp'] -= monster['damage']        
        battle_log.insert(tk.END, f"{monster['name']} causou {monster['damage']} de dano em você!\n")

        if player['hp'] <= 0:
            messagebox.showerror("Derrota", "Você foi derrotado. Fim de jogo!")
            root.quit()

    battle_log = tk.Text(battle_window, height=10, width=50)
    battle_log.pack(pady=5)

    battle_log.insert(tk.END, f"Você encontrou um {monster['name']}!\n")
    tk.Button(battle_window, text="Atacar", command=attack).pack(pady=5)
    tk.Button(battle_window, text="Fugir", command=battle_window.destroy).pack(pady=5)

# Configuração da janela principal
root = tk.Tk()
root.title("RPG Game")

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=10)
update_status()

btn_shop = tk.Button(root, text="Ir para a Loja", command=open_shop)
btn_shop.pack(pady=5)

btn_battle = tk.Button(root, text="Explorar e Batalhar", command=battle)
btn_battle.pack(pady=5)

btn_inventory = tk.Button(root, text="Ver Inventário", command=show_inventory)
btn_inventory.pack(pady=5)

btn_exit = tk.Button(root, text="Sair do Jogo", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()
