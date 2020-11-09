import math

if __name__ == "__main__":
    assert(add(2,3)==5)
    print("This will run when 11th_les_my_mod.py is called normally")

def sum_prod_bon(*args):
    return sum([math.prod(i) for i in args])