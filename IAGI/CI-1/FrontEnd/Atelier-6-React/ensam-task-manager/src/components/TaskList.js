import { useContext } from "react"
import Task from "./Task"
import { TaskContext } from "../context/TaskContext"
import "./TaskList.css"

const TaskList = () => {
  const { tasks, deleteTask, toggleTask, editTask } = useContext(TaskContext)

  return (
    <div className="task-list">
      {tasks.length === 0 ? (
        <p className="no-tasks">Aucune tâche à afficher</p>
      ) : (
        tasks.map((task) => (
          <Task key={task.id} task={task} onDelete={deleteTask} onToggle={toggleTask} onEdit={editTask} />
        ))
      )}
    </div>
  )
}

export default TaskList
