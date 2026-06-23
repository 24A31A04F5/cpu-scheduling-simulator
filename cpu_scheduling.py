n = int(input("Enter number of processes: "))

processes = []
burst_time = []

for i in range(n):
    p = input(f"Enter process name {i+1}: ")
    bt = int(input(f"Enter burst time for {p}: "))
    processes.append(p)
    burst_time.append(bt)

print("\nChoose Algorithm:")
print("1. FCFS")
print("2. SJF")
print("3. Round Robin")

choice = input("Enter choice: ")

# FCFS
if choice == "1":
    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i-1] + burst_time[i-1]

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]

    print("\n--- FCFS ---")

# SJF
elif choice == "2":
    combined = list(zip(processes, burst_time))
    combined.sort(key=lambda x: x[1])

    processes = [x[0] for x in combined]
    burst_time = [x[1] for x in combined]

    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i-1] + burst_time[i-1]

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]

    print("\n--- SJF ---")

# ROUND ROBIN
elif choice == "3":
    tq = int(input("Enter Time Quantum: "))

    remaining_bt = burst_time[:]
    wt = [0] * n
    tat = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > tq:
                    time += tq
                    remaining_bt[i] -= tq
                else:
                    time += remaining_bt[i]
                    wt[i] = time - burst_time[i]
                    remaining_bt[i] = 0
        if done:
            break

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]

    print("\n--- Round Robin ---")

else:
    print("Invalid choice")
    exit()

print("\nProcess\tBurst\tWaiting\tTurnaround")
for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t{wt[i]}\t{tat[i]}")

print("\nAverage Waiting Time:", sum(wt)/n)
print("Average Turnaround Time:", sum(tat)/n)