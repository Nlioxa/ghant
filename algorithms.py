def ghant(detail, operations):
    for i in range(len(operations)):
        if i == 0:
            operations[i].execute_times(
                detail.get_step_time(i), detail.get_number())
        else:
            previous_time = operations[i - 1].get_execution_time()
            wait_time = previous_time - operations[i].get_execution_time()
            if wait_time > 0:
                operations[i].execute_times(wait_time, 0)
            operations[i].execute_times(
                detail.get_step_time(i), detail.get_number())
