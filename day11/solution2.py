# Trick: If we do nothing, the worry values becomes huge and we can't quickly test whether test_divisor is a factor of the worry value. We can use a trick to keep the worry values manageable: If we take the lcm of the test_disivor values from all monkeys, then we have a number, N. If we take any worry value (w) and perform w % k, the resulting value will be smaller than w, but whether any test_divisor divies into the new value remains true or false. This is because:
# for all integers k: (a mod km) mod m = a mod m
# e.g. (1000 mod N*6) mod 6 = 1000 mod 6
class Monkey:
    def __init__(self, items, operation, operation_amount, test_divisor, monkey_target_true, monkey_target_false):
        self.items = items
        self.operation = operation
        self.operation_amount = operation_amount
        self.test_divisor = test_divisor
        self.monkey_target_true = monkey_target_true
        self.monkey_target_false = monkey_target_false
        self.inspection_count = 0

    def inspect_all_items(self):
        throw_targets = []
        for item in self.items:
            new_item = self.inspect_item(item)
            new_item = new_item % 9699690
            target_monkey = self.test_item(new_item)
            throw_targets.append((new_item, target_monkey))
            self.inspection_count += 1
        self.items = []
        return throw_targets

    def inspect_item(self, item):
        if self.operation == "plus":
            item += self.operation_amount
        elif self.operation == "multiply":
            if self.operation_amount == 0:
                item *= item
            else:
                item *= self.operation_amount

        return item    
    def test_item(self, item):
        target_monkey = None
        if  item % self.test_divisor == 0:
            target_monkey = self.monkey_target_true
        else:
            target_monkey = self.monkey_target_false
        return target_monkey

def calculate_monkey_business(all_monkeys):
    inspection_counts = [monkey.inspection_count for monkey in all_monkeys]
    inspection_counts = sorted(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]

monkey0 = Monkey([63, 84, 80, 83, 84, 53, 88, 72], "multiply", 11, 13, 4, 7)
monkey1 = Monkey([67, 56, 92, 88, 84], "plus", 4, 11, 5, 3)
monkey2 = Monkey([52], "multiply", 0, 2, 3, 1)
monkey3 = Monkey([59, 53, 60, 92, 69, 72], "plus", 2, 5, 5, 6)
monkey4 = Monkey([61, 52, 55, 61], "plus", 3, 7, 7, 2)
monkey5 = Monkey([79, 53], "plus", 1, 3, 0, 6)
monkey6 = Monkey([59, 86, 67, 95, 92, 77, 91], "plus", 5, 19, 4, 0)
monkey7 = Monkey([58, 83, 89], "multiply", 19, 17, 2, 1)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for _ in range(10000):
    for monkey in monkeys:
        throw_targets = monkey.inspect_all_items()
        for item, target in throw_targets:
            monkeys[target].items.append(item)

print(calculate_monkey_business(monkeys))