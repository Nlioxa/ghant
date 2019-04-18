class Detail(object):
    def __init__(self, detail_number, steps_times):
        self.num = detail_number
        self.steps_times = steps_times

    def get_step_time(self, step_number):
        return self.steps_times[step_number]

    def get_steps_count(self):
        return len(self.steps_times)

    def get_number(self):
        return self.num