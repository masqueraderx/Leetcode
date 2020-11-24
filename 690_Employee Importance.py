# Name: 690. Employee Importance
# Link:
# Time: 11/24/2020

class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solutions:
    def getImportance(self, employees: list['Employee'], id: int):

        employees = {e.id: e for e in employees}
        # BFS
        q = [id]
        sum = 0
        while q:
            cur = q.pop()
            sum += employees[cur].importance
            for subordinate in employees[cur].subordinates:
                q.append(subordinate)
        return sum