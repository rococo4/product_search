class Pfck:
    def __init__(self, protein, fat, carbohydrates, kcal):
        self.__protein = protein #double
        self.__fat = fat #double
        self.__carbohydrates = carbohydrates #double
        self.__kcal = kcal #double
    def get_protein(self):
        return self.__protein
    
    def get_fat(self):
        return self.__fat
    
    def get_carbohydrates(self):
        return self.__carbohydrates
    def get_kcal(self):
        return self.__kcal
    def __str__(self):
        return f"Protein: {self.__protein}g\nFat: {self.__fat}g\nCarbohydrates: {self.__carbohydrates}g\nKcal: {self.__kcal}"