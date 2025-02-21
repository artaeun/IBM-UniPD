first = int(input("Inserire il primo orario (es. 0930): "))
second = int(input("Inserire il secondo orario (successivo al primo): "))
hours1 = first // 100
minutes1 = first % 100 + hours1 * 60
hours2 = second // 100
minutes2 = second % 100 + hours2 * 60
timediff = minutes2 - minutes1
hours = timediff // 60
minutes = timediff % 60
print("Tempo trascorso:", hours, "ore e", minutes, "minuti")