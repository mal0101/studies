import { useState, useContext } from "react"
import { TaskContext } from "../context/TaskContext"
import "./TaskForm.css"

const TaskForm = () => {
  const [text, setText] = useState("")
  const { addTask } = useContext(TaskContext)

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!text.trim()) return
    addTask(text)
    setText("")
  }

  return (
    <form onSubmit={handleSubmit} className="task-form">
      <input type="text" placeholder="Ajouter une tâche" value={text} onChange={(e) => setText(e.target.value)} />
      <button type="submit">Ajouter</button>
    </form>
  )
}

export default TaskForm