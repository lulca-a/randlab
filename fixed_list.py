from random import choice

CATEGORIES = {
        "name": [
            "Alice", "Bruno", "Clara", "David", "Elena",
            "Felix", "Grace", "Hector", "Iris", "James"
        ],
        "place": [
            "London", "Tokyo", "New York", "Berlin", "Paris",
            "Rome", "Sydney", "Cairo", "Toronto", "Dublin"
        ],
        "lang": [
            "English", "Spanish", "French", "German", "Japanese",
            "Chinese", "Portuguese", "Italian", "Russian", "Korean"
        ],
        "obj": [
            "Laptop", "Sword", "Backpack", "Book", "Keyboard",
            "Phone", "Camera", "Headphones", "Bottle", "Watch"
        ],
        "subj": [
            "Math", "Physics", "Biology", "History", "Art",
            "Music", "Chemistry", "Philosophy", "Economics", "Computing"
        ],
        "emote": [
            "😀", "😂", "😐", "😢", "😡",
            "😍", "😎", "🤔", "😭", "🤯"
        ],
        "feel": [
            "Happy", "Tired", "Angry", "Motivated", "Anxious",
            "Relaxed", "Sad", "Excited", "Curious", "Confident"
        ],
    }

all_categories = ['feel','emote','subj','obj','lang','place','name']
#test comment
def fixedlist(list_length: int=10, category = None):
    if not isinstance(list_length,int):
        raise TypeError('List legnth needs to be integer')
    
    if category in CATEGORIES:
        return [choice(CATEGORIES[category]) for _ in range(list_length)]
    
    elif category == None:
        cat_choosen = choice(all_categories)
        return  [choice(CATEGORIES[cat_choosen]) for _ in range(list_length)]
    
    else:
        raise ValueError(f'"{category}" does not exist in list categories. Try: \n {all_categories}') 
