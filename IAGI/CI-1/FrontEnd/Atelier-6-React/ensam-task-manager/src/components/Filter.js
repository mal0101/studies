import { useContext } from "react"
import { TaskContext } from "../context/TaskContext"
import "./Filter.css"

const Filter = () => {
  const { setFilter, currentFilter } = useContext(TaskContext)

  return (
    <div className="filter">
      <button onClick={() => setFilter("all")} className={currentFilter === "all" ? "active" : ""}>
        Toutes
      </button>
      <button onClick={() => setFilter("active")} className={currentFilter === "active" ? "active" : ""}>
        Actives
      </button>
      <button onClick={() => setFilter("completed")} className={currentFilter === "completed" ? "active" : ""}>
        Terminées
      </button>
    </div>
  )
}

export default Filter
