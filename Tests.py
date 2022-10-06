def parse_index(index):
   numeric_index = []
   for element in index.split(","): # Разбиваем строку по запятым "1-5,7,9-11" -> ["1-5","7", "9-11"]
        if "-" in element: # Если "-" в элементе (например "1-5"), то
            start, end = (int(part) for part in element.split("-")) #Разбиваем строку по символу "-", и каждую часть преобразуем в Int: "1-5" -> ("1","5") -> (1,5)
            numeric_index.extend(list(range(start, end + 1))) # Генерируем наборы чисел из пслеовательности
            # range(start, end) - создаёт объект-диапозон чисел от start до end (не включая end, поэтому end + 1)
            # list() - преобразует объект range в list чисел 
            # numeric_index.exend() добавляет все числа из созданного диапозона в numeric_index
        else: # Если элемент не содержит "-" (значит число, а не последовательность)
