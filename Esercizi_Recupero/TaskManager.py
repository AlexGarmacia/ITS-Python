import json
dict_task = None
with open("src/data/tasks.json", "r") as file:

    dict_tasks: dict[str, dict[str, str|bool]] = json.load(file)

class TaskManager:

    def __init__(self, tasks: dict[str,dict[str,str|bool]] = {}) -> None:

        self.tasks : dict[str,dict[str,str|bool]] = tasks

    def create_task(self, task_id: str, descrizione: str) -> dict[str,dict[str,str|bool]] | str:

        if task_id in self.tasks:

            return "Errore il task esiste già!"
        
        else:

            temp_dict : dict[str,str[bool]] = {
                "descrizione": descrizione,
                "completato": False
            }

            self.tasks[task_id] = temp_dict

        return{task_id: temp_dict}
    
    def complete_task(self, task_id:str) -> dict | str:

        if task_id not in self.tasks:

            return "Task non presente"
        
        else:
            self.tasks[task_id]["completato"] = True

            return {task_id: self.tasks[task_id]}
        
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict | str:

        if task_id not in self.tasks:

            return "Errore, il task non è presente !"
        
        else: 
            
            self.tasks[task_id]["descrizione"] = nuova_descrizione

            return [task_id: self.tasks[task_id]]

    def remove_tasks(self, task_id:str) -> dict | str:

        if task_id not in self.tasks:

            return "Errore, il task non esiste!"
        
        else: 

            value = self.task.pop(task_id)

            return[task_id: value]

    def list_tasks(self) -> list[str]:

        
task_manager_1: TaskManager = TaskManager(dict_task)