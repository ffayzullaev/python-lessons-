friends = []
friends.append("Alisher")
friends.append("Fazliddin")
friends.append("Steave")
friends.append("Ahmad")

friends.remove("Ahmad")
friends.remove("Steave")
friends.insert(0, "Jamshid")
friends.insert(3, "Vali")
friends.insert(4, "G'ani")

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)
