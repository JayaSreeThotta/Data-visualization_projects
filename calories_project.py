from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


CALORIE_GOAL_LIMIT = 3000 #KCAL
PROTEIN_GOAL =180  #GM
FAT_GOAL=80 #GM
CARBS_GOAL=300  #GM

today=[]

@dataclass
class Food:
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int

done=False
while not done:
    print(""" 
          (1) Add a new food
           (2) visualize progress
         (3) quit""")
    option=input('choose an option:')
    if option=="1":
        print("Adding a new food")
        name=input("Name:")
        calories=int(input("calories:"))   
        proteins=int(input("proteins:"))
        fats=int(input("fats:"))
        carbs=int(input("carbs"))
        food=Food(name,calories,proteins,fats,carbs)
        today.append(food)
    elif option=="2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.proteins for food in today)
        fats_sum = sum(food.fats for food in today)
        carbs_sum= sum(food.carbs for food in today)
        fig, axs= plt.subplots(2,2)
        axs[0, 0].pie([protein_sum,fats_sum,carbs_sum], labels=["Proteins","fats","carbs"], autopct="%1.1f%%")
        axs[0, 0].set_title("Macronutrient Distribution")
        axs[0, 1].bar([0,1,2], [protein_sum,fats_sum,carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [protein_sum,fats_sum,carbs_sum], width=0.4)
        axs[0, 1].set_title("Macronutrient Distribution")
        axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum],labels=["Calories","Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal progress")
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]))
        axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT]* len(today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calories Goal over Time")
        fig.tight_layout()
        plt.show()
    elif option == "3":
        done = True
    else:
        print("invalid option")


    
    

    
    