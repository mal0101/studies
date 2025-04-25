import { useState } from "react"
import "./Task.css"

const Task = ({ task, onDelete, onToggle, onEdit }) => {
  const [isEditing, setIsEditing] = useState(false)
  const [editText, setEditText] = useState(task.text)

  const handleEdit = () => {
    if (editText.trim()) {
      onEdit(task.id, editText)
      setIsEditing(false)
    }
  }

  const cancelEdit = () => {
    setEditText(task.text)
    setIsEditing(false)
  }

  return (
    <div className={`task ${task.completed ? "completed" : ""}`}>
      <div className="task-content">
        <input type="checkbox" checked={task.completed} onChange={() => onToggle(task.id)} />

        {isEditing ? (
          <input
            type="text"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
            className="edit-input"
            autoFocus
          />
        ) : (
          <span className={task.completed ? "completed-text" : ""}>{task.text}</span>
        )}
      </div>

      <div className="task-actions">
        {isEditing ? (
          <>
            <button onClick={handleEdit} className="save-btn">
              Enregistrer
            </button>
            <button onClick={cancelEdit} className="cancel-btn">
              Annuler
            </button>
          </>
        ) : (
          <>
            <button onClick={() => setIsEditing(true)} className="edit-btn">
              Modifier
            </button>
            <button onClick={() => onDelete(task.id)} className="delete-btn">
              Supprimer
            </button>
          </>
        )}
      </div>
    </div>
  )
}

export default Task