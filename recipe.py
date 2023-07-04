class Recipe:
    def __init__(self,dish,item,time) -> None:
        self.dish = dish
        self.item = item
        self.time = time

    def content(self):
        print('The ' + self.dish + 'has ' +str(self.item)+ \
              ' and takes ' +str(self.time)+ ' mins to prepare')
        
pizza = Recipe('Pizza', ['cheese','bread','tomato'],45)
rice = Recipe('Rice', ['stew','meat'],30)
print(pizza.content())


class bookAuthor:
    def __init__(self,name,book) -> None:
        self.name = name
        self.book = book

    def bookDet(self):
        print('Mr.' +str(self.name)+ ' wrote ' +str(self.book)+ ' book')

eugene = bookAuthor('Eugene','I am not Eugene')
print(eugene.bookDet())