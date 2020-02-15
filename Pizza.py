class Pizza:
    def __init__(self, mapping, items, rows_N, colums_N):
        self.mapping = mapping
        self.items = items
        self.rowsN = rows_N
        self.columsN = colums_N

    # coupe la pizza en plusieurs "grosse part", la taille des parts est donné par row_lenght et column_lenght
    def split_pizza_into_map(self, row_lenght, column_lenght):
        splited_mapping = []
        i = 0
        j = 0
        cursorX = 0
        cursorY = 0
        while(i < self.rowsN and j < self.columsN):
            new_mapping = []
            for x in range(i, min(i+column_lenght, self.rowsN)):
                for y in range(j, min(j+row_lenght, self.columsN)):
                    new_mapping.append(self.mapping[x*self.columsN+y])
                    cursorX = x
                    cursorY = y
            j += row_lenght
            if(cursorY == self.columsN-1):
                j = 0
                i += column_lenght
            splited_mapping.append(new_mapping)
        return splited_mapping