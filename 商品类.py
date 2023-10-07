class goods:
    def __init__(self,num,name,single,all,remain_number):
        """num是商品序号，name是商品名，single是单价，all是总数量，remain是剩余数量"""
        self._num=num
        self._name=name
        self._single=single
        self._all=all
        self._remain_number=remain_number
    def display(self):
        print("商品序号是",self._num)
        print("商品名是",self._name)
        print("商品的单价是",self._single)
        print("商品的总价是",self._all)
        print("商品的剩余数量是",self._remain_number)
    def income(self):
        self.seld=self._all-self._remain_number
        return self.seld*self._single
    def setdata(self,num2,name2,single2,all2,remain_number2):
        self.num2=num2
        self.name2=name2
        self.single2=single2
        self.all2=all2
        self.remain_number2=remain_number2