from lib._5_design_a_class import *

def test_add_single_task():
    todo = TodoList()
    todo.add_task("Walk dog")
    assert todo.get_tasks() == ["Walk dog"] 

def test_add_multiple_tasks():
    todo = TodoList()
    todo.add_task("Walk dog")
    todo.add_task("Go shopping")
    assert todo.get_tasks() == ["Walk dog", "Go shopping"] 

def test_add_and_complete_task():
    todo = TodoList()
    todo.add_task("Walk dog")
    todo.add_task("Go shopping")
    todo.mark_task_complete("Walk dog")
    assert todo.get_tasks() == ["Go shopping"]
