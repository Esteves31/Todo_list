class InvalidUserOrNoTodoList(Exception):
    def __init__(self):
        message = 'Invalid user or no TodoList'
        super().__init__(message)