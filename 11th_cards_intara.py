import itertools
import random
 
def set_card_pack():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
    suits = ["♣", "♦", "♥", "♠"]
    card_pack = list(itertools.product(ranks, suits))
    return card_pack
 
def get_shuffled_card_pack():
    new_card_pack = set_card_pack()
    return random.sample(new_card_pack, k=52)
 
def main():
    my_pack = set_card_pack()
    print (my_pack)
    print ()
 
    print(random.choice(my_pack))
    print()
 
    print(get_shuffled_card_pack())
 
if __name__ == "__main__":
    main()