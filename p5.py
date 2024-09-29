def fitness_test(oxygen_levels):
    
    num_trainees = 3
    num_rounds = 3

    
    oxygen = [[0] * num_rounds for _ in range(num_trainees)]
    
    
    index = 0
    for i in range(num_rounds):
        for j in range(num_trainees):
            if oxygen_levels[index] < 1 or oxygen_levels[index] > 100:
                print("INVALID INPUT")
                return
            oxygen[j][i] = oxygen_levels[index]
            index += 1

    
    avg_oxygen = []
    for trainee in range(num_trainees):
        avg = round(sum(oxygen[trainee]) / num_rounds)
        avg_oxygen.append(avg)

   
    max_avg = max(avg_oxygen)

    
    if max_avg < 70:
        print("All trainees are unfit")
        return

    
    for i in range(num_trainees):
        if avg_oxygen[i] == max_avg:
            print(f"Trainee Number : {i + 1}")


oxygen_levels = []
for _ in range(9):
    oxygen_levels.append(int(input()))


fitness_test(oxygen_levels)
