import time
import random
import msvcrt

def start_symbattle_russian():
    print("=== ⚔️ ДОБРО ПОЖАЛОВАТЬ НА РУССКУЮ АРЕНУ SYMBATTLE! ⚔️ ===")
    print("Правила: У тебя есть ровно 5 секунд, чтобы ввести слово и нажать Enter!\n")
    
    # Пул простых русских слов для битвы
    words_pool = ["код", "хакер", "питон", "база", "аэро", "чат", "лог", "скретч", "кейн", "лагерь"]
    
    hp_player = 100
    hp_boss = 100
    
    while hp_player > 0 and hp_boss > 0:
        # Выбираем случайное слово
        battle_word = random.choice(words_pool)
        print(f"🎯 БОЕВОЕ СЛОВО: {battle_word}")
        print("⏰ ВРЕМЯ ПОШЛО! Пиши: ", end="", flush=True)
        
        user_input = ""
        start_time = time.time()
        timeout = 5  # 5 секунд
        
        while time.time() - start_time < timeout:
            if msvcrt.kbhit():
                # Считываем символ. Декодируем в cp1251 для русской консоли Windows
                try:
                    char = msvcrt.getwch()
                except Exception:
                    continue
                    
                if char == '\r':  # Нажат Enter
                    break
                elif char == '\b':  # Нажат Backspace
                    if len(user_input) > 0:
                        user_input = user_input[:-1]
                        print("\b \b", end="", flush=True) # Стираем символ на экране
                else:
                    user_input += char
                    print(char, end="", flush=True)
                    
            time.sleep(0.05)
            
        print() # Перенос строки
        
        # Проверка времени и ввода
        if time.time() - start_time >= timeout:
            hp_player -= 25
            print(f"⏰ ВРЕМЯ ВЫШЛО! Робот нанёс удар! Твоё HP: {hp_player}\n")
        elif user_input.lower().strip() == battle_word:
            hp_boss -= 25
            print(f"💥 БУМ! Точный удар по Боссу! HP Босса: {hp_boss}\n")
        else:
            hp_player -= 15
            print(f"❌ ОШИБКА! Ты написал '{user_input}' вместо '{battle_word}'! Получаешь урон! Твоё HP: {hp_player}\n")
            
        time.sleep(1.5)
        
    if hp_player <= 0:
        print("💀 ИГРА ОКОНЧЕНА! ТЫ ПРОИГРАЛ НА РУССКОЙ АРЕНЕ!")
    else:
        print("👑 ПОБЕДА! Андрей — абсолютный чемпион SYMBATTLE!")

# Запуск
start_symbattle_russian()
