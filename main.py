from operation import Operation
from detail import Detail
from algorithms import ghant

task_times = {
    1: [2, 3, 1],
    2: [3, 2, 1],
    3: [4, 1, 2],
    4: [1, 2, 3]
}

details = []
operations = []

for key, value in task_times.items():
    details.append(Detail(key,value))

for i in range(len(task_times.get(1))):
    operations.append(Operation())

for detail in details:
    ghant(detail, operations)
    
for operation in operations:
    print(operation)
