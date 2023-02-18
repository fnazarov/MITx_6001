def PrintMoves(fr,to):
    print("Move ", fr, " to ", to)

def Hanoi(n,fr,spare, to):
    '''

    :param n: Number of Towers to mover. N should be integer
    :param fr: Is the First From Tower. fr is string
    :param spare: Is the Second Spare Tower. spare is string
    :param to: Is the 'To' Tower to move the last Tower. to is string
    :return: Print the moves of the Towers
    For example Hanoi(3,'P1','P2','P3') will print all the moves to move three towers
    '''
    if n==1:
        PrintMoves(fr,to)
    else:
        return Hanoi(n-1,fr,spare,to)
        return Hanoi(1,fr,to,spare)
        return Hanoi(n-1,spare,to,fr)