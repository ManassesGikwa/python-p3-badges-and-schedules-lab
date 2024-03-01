def badge_maker(name):
        return f"Hello, my name is {name}."
badge_maker("Arel")

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]
    

def assign_rooms(names):
     return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index,name in enumerate(names)]

def printer(names):
    badges = batch_badge_creator(names)
    rooms   = (assign_rooms(names))
 
    for badge in badges:
         print(badge)  
    for room in rooms:
        print(room)
