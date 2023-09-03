def solution(todo_list, finished):
    return [e for i,e in enumerate(todo_list) if not finished[i]]