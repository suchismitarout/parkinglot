class Parkinglot():

    def __init__(self, total_capacity):
        self.total_capacity = total_capacity
        self.slots = [-1] * self.total_capacity
        self.current_capacity = 0

    def _slot(self):
        """
        it will initialize elements in slots with -1
        with total_capacity number of times
        :return:
        """
        if self.current_capacity < self.total_capacity:
            for slot in range(len(self.slots)):
                if self.slots[slot] == -1:
                    return slot
        else:
            # means slot is not available
            return -1

    def _check_if_vehicle_present(self, reg_no):
        i = 0
        for slot in self.slots:
            if slot== reg_no:
                return i
            i+=1
        else:
            return -1

    def park(self, vehicle):
        slot = self._slot()
        if slot == -1:
            return False

        self.slots[slot] = vehicle
        self.current_capacity += 1
        return True

    def unpark(self, reg_no):
        # means no cab is there.
        if self.current_capacity == 0:
            return False

        # means vehicle is not present
        index = self._check_if_vehicle_present(reg_no)
        if index == -1:
            return False

        # now delete the index from the slots
        self.slots[index] = -1
        self.current_capacity -= 1
        return True

    def list_parked_vehicles(self):
        return self.slots
