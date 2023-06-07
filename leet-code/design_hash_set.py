class MyHashSet:

    def __init__(self):
        self.capacity = 512
        self.table = [None]*self.capacity
        self.size = 0
        self.max_load_factor = 0.75

    def _resize(self):
        self.capacity = self.capacity*2
        self.size = 0
        old_table = self.table
        self.table = [None] * self.capacity
        for key in old_table:
            if key is not None:
                self.add(key)

    def _get_hash(self, key: int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        self.size += 1
        hashed_key = self._get_hash(key)
        while self.table[hashed_key] is not None:
            if self.table[hashed_key] == key:
                self.size -= 1
                break
            key += 1
            hashed_key = self._get_hash(key)
        self.table[hashed_key] = key
        if self.size / self.capacity >= self.max_load_factor:
            self._resize()
    
    def find_key(self, key: int) -> int:
        """
        Returns the hash of the key
        """
        hashed_key = self._get_hash(key)
        if self.table[hashed_key] is None:
            return -1
        if self.table[hashed_key] != key:
            original_key = hashed_key
            while self.table[hashed_key] != key:
                key += 1
                hashed_key = self._get_hash(key)
                if self.table[hashed_key] is None:
                    return -1
                if hashed_key == original_key:
                    return -1
        return hashed_key

    def remove(self, key: int) -> None:
        hashed_key = self.find_key(key=key)
        if hashed_key != -1:
            self.table[hashed_key] = None
        
    def contains(self, key: int) -> bool:
        return self.find_key(key=key) != -1
    

obj = MyHashSet()


ops = ["contains","remove","add","add","contains","remove","contains","contains","add","add","add","add","remove","add","add","add","add","add","add","add","add","add","add","contains","add","contains","add","add","contains","add","add","remove","add","add","add","add","add","contains","add","add","add","remove","contains","add","contains","add","add","add","add","add","contains","remove","remove","add","remove","contains","add","remove","add","add","add","add","contains","contains","add","remove","remove","remove","remove","add","add","contains","add","add","remove","add","add","add","add","add","add","add","add","remove","add","remove","remove","add","remove","add","remove","add","add","add","remove","remove","remove","add","contains","add"]
values = [[72],[91],[48],[41],[96],[87],[48],[49],[84],[82],[24],[7],[56],[87],[81],[55],[19],[40],[68],[23],[80],[53],[76],[93],[95],[95],[67],[31],[80],[62],[73],[97],[33],[28],[62],[81],[57],[40],[11],[89],[28],[97],[86],[20],[5],[77],[52],[57],[88],[20],[48],[42],[86],[49],[62],[53],[43],[98],[32],[15],[42],[50],[19],[32],[67],[84],[60],[8],[85],[43],[59],[65],[40],[81],[55],[56],[54],[59],[78],[53],[0],[24],[7],[53],[33],[69],[86],[7],[1],[16],[58],[61],[34],[53],[84],[21],[58],[25],[45],[3]]

res = []
for i,j in zip(ops, values):
    print(obj.table)
    if i == "contains":
        res.append(obj.contains(j[0]))
    if i == "remove":
        res.append(obj.remove(j[0]))
    if i == "add":
        res.append(obj.add(j[0]))
