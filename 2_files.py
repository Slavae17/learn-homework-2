"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
with open('referat.txt','r', encoding='utf-8') as f:
        
        for words in f: 
            text = f.read()
            f.seek(0)                       
            words = f.read()
            words = words.replace(".","!")
            
            print(f'Количество слов в тексе - ', len(words.split(' '))) # Количество слов
        print(f'Длина строки в переменной -', len(text))  # Длина строки в переменной           
        
        

with open('referat2.txt','w',encoding='utf-8') as t:
    t.write(words)





if __name__ == "__main__":
    main()
