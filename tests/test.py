#!/usr/bin/env python3


from Game.players import AI_Player


def test1():
    AI_p = AI_Player("Computer")
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mem = []
    
    for i in range(100):
        x = AI_p.guess_letter(mem)
        if x == "null":
            break
        mem.append(x)
        if x in letters:
            letters.remove(x)
    
        
    assert(letters == [])

def run_tests():
    test1()

