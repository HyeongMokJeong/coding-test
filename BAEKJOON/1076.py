c = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
color = [input() for _ in range(3)]
dic = {i : idx for idx, i in enumerate(c)}
print((dic[color[0]] * 10 + dic[color[1]]) * (10**dic[color[2]]))