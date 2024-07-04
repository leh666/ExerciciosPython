from ex12_conta_alunos_baixos import conta_alunos_baixos

def test_01():
    assert conta_alunos_baixos([160,160,160],[11,11,11]) == 0
def test_02():
    assert conta_alunos_baixos([140,180,180],[13,11,11]) == 1
def test_03():
    assert conta_alunos_baixos([197,164,182],[14,13,15]) == 1