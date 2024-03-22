from target_fibonacci import pertence_a_sequencia_fibonacci

def test_pertencem_sequencia_fibonacci():
    pertencem = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in pertencem:
        assert pertence_a_sequencia_fibonacci(i)
        
def test_nao_pertencem_sequencia_fibonacci():
    nao_pertencem = [4, 6, 7, 9, 10, 11, 12, 14, 15]
    for i in nao_pertencem:
        assert not pertence_a_sequencia_fibonacci(i)