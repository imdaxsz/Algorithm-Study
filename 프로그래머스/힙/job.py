def jobScheduling (jobs):
    schedule = []
    noMachine = 0
    jobs.sort()
    
    while jobs:
        task = jobs.pop(0)
        found = False
        for mi in schedule:
            if mi[0] <= task[0]:
                mi.append(task)
                mi[0] = task[1]
                found = True
                break;
        if not found:
            noMachine += 1
            schedule.append([task[1], task])

    return schedule

jobs = [[7, 8], [3, 7], [1, 5], [5, 9], [0, 2], [6, 8], [1, 6]]
schedule = jobScheduling(jobs)
print("The number of used machines is", len(schedule))
print(schedule)
