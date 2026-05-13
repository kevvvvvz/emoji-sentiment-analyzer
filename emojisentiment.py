import demoji

def demoji_sentiment():
    # Sentence Examples:
    # "great day today 😊☀️"
    # "mixed feelings 😊😢"
    # "just a normal day"
    # "this is awful 😢💔"
    check = []
    while True:
        add = input("Enter sentence here (Type 'STOP' when done entering sentences): ")
        
        if add.upper() == "STOP":
            break
        else:
            check.append(add)
            print()
            print("Enter your next sentence.")
        
    new_list = []

    for this in check:
        anyways = demoji.findall(this)
        new_list.append(anyways)
    #print(new_list)
        
    positive = ["joy", "happy", "fire", "smiling", "sun", "star", "sparkling", "party", "clapping", "thumbs up", "muscle"]
    negative = ["crying", "enraged", "sad", "hate", "skull", "broken heart", "angry", "nauseated", "thumbs down", "cold sweat", "disappointed", "forbidden", "warning"]

    positive_counter = 0
    negative_counter = 0
    neutral_counter = 0

    for check in new_list:
        reset_positive = 0
        reset_negative = 0
        stuff = check.values()
        #print(stuff)
        
        for description in stuff:
            
            for this in positive:
                if this in description:
                    positive_counter += 1
                    reset_positive += 1
            
            for this in negative:
                if this in description:
                    negative_counter += 1
                    reset_negative += 1
        
        if reset_positive == 0 and reset_negative == 0:
            neutral_counter += 1
            
    return positive_counter, negative_counter, neutral_counter
        
        
def main():      
    print("<==> Enter a sentence that may or may not contain emojis <==>")
    print("<==> You may enter as many sentences as you wish <==>")
    print("<==> The emojis will be analyzed and the scores for positive, negative, or neutral emotions will be displayed at the end <==>")
    print()
    
    positive_counter, negative_counter, neutral_counter = demoji_sentiment()
    
    print()
    print(f"Positive Score: {positive_counter}")
    print(f"Negative Score: {negative_counter}")
    print(f"Neutral Score: {neutral_counter}")
    
    if positive_counter > negative_counter and positive_counter > neutral_counter:
        print("Overall Sentiment: Positive")
    elif  negative_counter > positive_counter and negative_counter > neutral_counter:
        print("Overall Sentiment: Negative")
    elif neutral_counter > positive_counter and neutral_counter > negative_counter:
        print("Overall Sentiment: Neutral")
    elif positive_counter == negative_counter:
        print("Overall Sentiment: Positive and Negative")
    else:
        print("Overall Sentiment: Mixed")
main()