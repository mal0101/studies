import { useContext } from "react"
import { TaskContext } from "../context/TaskContext"
import "./Header.css"

const Header = () => {
  const { tasks } = useContext(TaskContext)
  const completedTasks = tasks.filter((task) => task.completed).length

  return (
    <div className="header">
      <h1>ENSAM Task Manager</h1>
      <p>
        {tasks.length > 0 ? `${completedTasks} sur ${tasks.length} tâches terminées` : "Aucune tâche pour le moment"}
      </p>
    </div>
  )
}

export default Header