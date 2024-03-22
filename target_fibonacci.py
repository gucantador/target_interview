def pertence_a_sequencia_fibonacci(x):
    sequencia = [0, 1]


    while True:
        sequencia.append(sequencia[-1] + sequencia[-2])
        if x in sequencia:
            print(f"O valor {x} pertence a sequencia de fibonacci")
            return True
        if x < sequencia[-1]:
            print(f"O valor {x} não pertence a sequencia de fibonacci")
            return False
        