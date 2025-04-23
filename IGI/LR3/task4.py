def analyze_text():
    """
    Задание 4.
    Анализ текста: слова длиной 3, гласные=согласные, сортировка по длине.
    """
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    words = [word.strip(".,") for word in text.split()]

    # a) Слова длиной 3
    three_letter = [word for word in words if len(word) == 3]
    print(f"а) Слов длиной 3: {len(three_letter)}")

    # б) Гласные == согласные
    vowels = {'a', 'e', 'i', 'o', 'u'}
    matched = []
    for idx, word in enumerate(words, 1):
        v = sum(1 for c in word.lower() if c in vowels)
        c = len(word) - v
        if v == c:
            matched.append((idx, word))
    print("б) Слова с равными гласными и согласными:")
    for item in matched:
        print(f"Позиция {item[0]}: {item[1]}")

    # в) Сортировка по убыванию длины
    sorted_words = sorted(words, key=lambda x: -len(x))
    print("в) Слова по убыванию длины:", ", ".join(sorted_words))