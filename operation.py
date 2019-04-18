class Operation (object):
    def __init__(self):
        self.execution_time = 0
        self.schedule = []

    def execute(self, task):
        self.execution_time += 1
        self.schedule.append(task)

    def execute_times(self, times, task):
        while times > 0:
            self.execute(task)
            times -= 1

    def wait(self):
        self.execution_time += 1

    def wait_times(self, times):
        while times > 0:
            self.wait()
            times -= 1

    def get_processing_time(self):
        processing_time = 0
        for task in self.schedule:
            if task is not 0:
                processing_time += 1
        return processing_time

    def get_execution_time(self):
        return self.execution_time

    def get_preprocessing_time(self):
        preprocessing_time = 0
        for task in self.schedule:
            if task is not 0:
                return preprocessing_time
            else:
                preprocessing_time += 1

    def get_waiting_time(self):
        waiting_time = 0
        is_active = False
        for task in self.schedule:
            if not is_active:
                if task is not 0:
                    is_active = True
                pass
            if task is 0:
                waiting_time += 1
        return waiting_time

    def get_schedule(self):
        return self.schedule

    def __repr__(self):
        return 'schedule: {}'.format(self.get_schedule()) + '\n'\
            'execution time: {}'.format(self.get_execution_time()) + '\n'\
            'preprocessing time: {}'.format(self.get_preprocessing_time()) + '\n'\
            'waiting time: {}'.format(self.get_waiting_time()) + '\n'\
            'processing time: {}'.format(self.get_processing_time()) + '\n'
