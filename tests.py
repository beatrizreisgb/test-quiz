import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# 10 novos testes de unidade

# teste 1: remover todas as alternativas
def test_remove_all_choices():
    q = Question(title='q1')
    q.add_choice('a', False)
    q.add_choice('b', True)

    q.remove_all_choices()

    assert len(q.choices) == 0

# teste 2: remover alternativa por id
def test_remove_choice_by_id():
    q = Question(title='q1')
    c1 = q.add_choice('a', False)
    c2 = q.add_choice('b', True)

    q.remove_choice_by_id(c1.id)

    assert len(q.choices) == 1
    assert q.choices[0].id == c2.id

# teste 3: remover alternativa com id inválido
def test_remove_choice_invalid_id():
    q = Question(title='q1')
    q.add_choice('a', False)

    with pytest.raises(Exception):
        q.remove_choice_by_id(2)

# teste 4: definir alternativa correta com id inválido
def test_set_correct_choices_invalid_id():
    q = Question(title='q1')
    q.add_choice('a', False)

    with pytest.raises(Exception):
        q.set_correct_choices([1, 2])

# teste 5: definir múltiplas alternativas corretas
def test_set_multiple_correct_choices():
    q = Question("q1", max_selections=2)
    c1 = q.add_choice('a')
    c2 = q.add_choice('b')

    q.set_correct_choices([c1.id, c2.id])

    assert c1.is_correct
    assert c2.is_correct

# teste 6: corrigir seleção com múltiplas alternativas corretas
def test_correct_multiple_choices():
    q = Question("q1", max_selections=2)
    q.add_choice('a', True)
    q.add_choice('b', True)

    result = q.correct_selected_choices([1, 2])

    assert len(result) == 2
    assert 1 in result
    assert 2 in result

# teste 7: exceder número máximo de seleções
def test_exceed_max_selections():
    q = Question(title='q1', max_selections=2)
    q.add_choice('a', True)
    q.add_choice('b', True)
    q.add_choice('c', False)

    with pytest.raises(Exception):
        q.correct_selected_choices([1, 2, 3])

# teste 8: criar alternativa com texto vazio
def test_add_choice_empty_text():
    q = Question(title='q1')

    with pytest.raises(Exception):
        q.add_choice('', False)

# teste 9: criar alternativa com texto muito longo
def test_add_choice_text_too_long():
    q = Question(title='q1')

    with pytest.raises(Exception):
        q.add_choice('a' * 101, False)

# teste 10: avaliar questão sem alternativas corretas
def test_no_correct_choices():
    q = Question(title='q1', max_selections=2)
    q.add_choice('a', False)
    q.add_choice('b', False)

    result = q.correct_selected_choices([1, 2])

    assert len(result) == 0