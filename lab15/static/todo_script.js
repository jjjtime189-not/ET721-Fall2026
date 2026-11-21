function loadTasks() {
    fetch("/get_tasks")
        .then(response => {
            if (!response.ok) {
                throw new Error("Could not load tasks");
            }
            return response.json();
        })
        .then(tasks => {
            const list = document.querySelector("#taskList");
            list.innerHTML = "";
            if (!Array.isArray(tasks)) {
                return;
            }
            tasks.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.task;
                li.classList.add("task_item");
                list.appendChild(li);
                const btn = document.createElement("button");
                btn.innerHTML = "&#10060;";
                btn.classList.add("btndeletetask");
                btn.onclick = () => deleteTask(task.id);
                li.appendChild(btn);
            });
        })
        .catch(error => console.error(error));
}

window.onload = loadTasks;

function deleteTask(taskId) {
    fetch("/delete_task", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({id: taskId})
    })
    .then(() => loadTasks());
}

function addTask() {
    const input = document.querySelector("#taskInput");
    const task = input.value.trim();
    if (task === "") return;
    fetch("/add_task", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ task: task })
    })
    .then(()=>{
        input.value = "";
        loadTasks();
    });
}