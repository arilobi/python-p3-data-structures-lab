spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods: 
        if 'name' in food: 
            names.append(food['name'])
    return names

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    heat_level = []
    for food in spicy_foods: 
        if food['heat_level'] > 5: 
            heat_level.append(food) 
    return heat_level 

print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods): 
    for food in spicy_foods: 
        heat_level_emojis = "🌶" * food["heat_level"] 
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level_emojis}')

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods: 
        if food["cuisine"] == cuisine:
            return food
        
get_spicy_food_by_cuisine(spicy_foods, "American")
get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods) 
    print_spicy_foods(spiciest_foods)

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods) 
    average_heat_level = total_heat_level / len(spicy_foods) 
    return int(average_heat_level)  

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food) 
    return spicy_foods 

spicy_food = { 
    'name': 'Griot', 
    'cuisine': 'Haitian', 
    'heat_level': 10, 
} 

updated_spicy_foods = create_spicy_food(spicy_foods, spicy_food) 
print(updated_spicy_foods)
