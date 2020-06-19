'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    count = 0
    def recursion(next_word):
        index = next_word.find('th')
        if index != -1:
            nonlocal count
            count += 1
            if len(next_word) >= index + 4:
                spliced = next_word[index+2:]
                recursion(spliced)
        else:
            return
        pass

    recursion(word)
    

    # TBC
    
    return count


count_th("mathath")