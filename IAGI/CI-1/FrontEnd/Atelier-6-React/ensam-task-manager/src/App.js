import { TaskProvider } from "./context/TaskContext"
import Header from "./components/Header"
import TaskForm from "./components/TaskForm"
import TaskList from "./components/TaskList"
import Filter from "./components/Filter"
import "./App.css"

const App = () => {
  return (
    <TaskProvider>
      <div className="app">
        <Header />
        <TaskForm />
        <Filter />
        <TaskList />
      </div>
    </TaskProvider>
  )
}

export default App
