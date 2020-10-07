# GEO1000 - Assignment 3
# Authors :
# Studentnumbers :

def reverse_part(part):
    """Take as input a list
    Returns a new list with elements in input reversed
    Note: Pure function, so should not modify input!
    
    Example:
    
        >>> reverse_part(['t', 'h', 'i', 's'])
        ['s', 'i', 'h', 't']
    """
    revlist = part.copy()
    revlist.reverse()
    return revlist


def part_to_str(part):
    """Take as input a list with letters.
    Returns a new string with letters in the input list

    Example:

        >>> part_to_str(['a', 'b', 'c'])
        "abc"

    """
    strlist = part
    return "".join(strlist)


def split_in_parts(sentence):
    """Split the string into a list of lists (either containing letters, or just
    one character not part of the alphabet).

    Example:

        >>> split_in_parts("this is.")
        [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]

    """
    mainlist = []
    temp = []
    for i in sentence:
        if i.isalpha(): #check if is a letter
            temp.append(i)
        else: # if is not letter
            mainlist.append(temp)
            temp = []
            mainlist.append([i])
    return(mainlist)


def reverse_relevant_parts(parts):
    """Reverse only those sublists consisting of letters
    
    Input: list of lists, e.g. [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    Returns: list with sublists reversed that consist of letters only.
    """
    relev_rev_list = []
    for i in parts:
        if i[0].isalpha(): #if that part is relevant
            i.reverse()
            relev_rev_list.extend(i)
        else: #not relevant
            relev_rev_list.extend(i)
    return(relev_rev_list)


def glue(parts):
    """Transforms the list of sublists back into a new string
    
    Returns: string
    """
    return( ''.join( [''.join(i) for i in parts] ) )


def encrypt(sentence):
    """Reverses all consecutive letter parts in a string.
    
    Input: a string
    Returns: a string
    """
    pass


if __name__ == "__main__":

    paragraph = "toN ylno si ti ysae ot eil htiw spam, ti's laitnesse. oT yartrop lufgninaem spihsnoitaler rof a xelpmoc, eerht-lanoisnemid dlrow no a talf teehs fo repap ro a oediv neercs, a pam tsum trotsid ytilaer. sA a elacs ledom, eht pam tsum esu slobmys taht tsomla syawla era yllanoitroporp hcum reggib ro rekciht naht eht serutaef yeht tneserper. oT diova gnidih lacitirc noitamrofni ni a gof fo liated, eht pam tsum reffo a evitceles, etelpmocni weiv fo ytilaer. erehT's on epacse morf eht cihpargotrac xodarap: ot tneserp a lufesu dna lufhturht erutcip, na etarucca pam tsum llet etihw seil. --- woH ot eil htiw spam, kraM reinomnoM, 1996."
    print(encrypt(paragraph))
    assert encrypt(encrypt(paragraph)) == paragraph
