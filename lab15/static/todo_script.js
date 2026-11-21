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
            if (!Array.isArray(tasks)) {
                return;
            }
            list.innerHTML = "";
            if (tasks.length === 0) {
                return;
            }
            tasks.forEach(task => {
                const li = document.createElement("li");
                li.classList.add("task_item");
                li.dataset.taskId = task.id;
                const text = document.createElement("span");
                text.className = "task_text";
                text.textContent = task.task;
                li.appendChild(text);
                const btn = document.createElement("button");
                btn.innerHTML = "&#10060;";
                btn.classList.add("btndeletetask");
                btn.type = "button";
                btn.setAttribute("aria-label", "Delete task");
                btn.onclick = () => deleteTask(task.id);
                li.appendChild(btn);
                list.appendChild(li);
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
    .then(response => {
        if (!response.ok) {
            throw new Error("Could not delete task");
        }
        return response.json();
    })
    .then(() => loadTasks())
    .catch(error => console.error(error));
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
    .then(response => {
        if (!response.ok) {
            throw new Error("Could not add task");
        }
        return response.json();
    })
    .then(result => {
        input.value = "";
        if (result.status === "success") {
            const list = document.querySelector("#taskList");
            const li = document.createElement("li");
            li.className = "task_item";
            li.dataset.taskId = result.id;
            const text = document.createElement("span");
            text.className = "task_text";
            text.textContent = result.task;
            li.appendChild(text);
            const btn = document.createElement("button");
            btn.className = "btndeletetask";
            btn.type = "button";
            btn.innerHTML = "&#10060;";
            btn.setAttribute("aria-label", "Delete task");
            btn.onclick = () => deleteTask(result.id);
            li.appendChild(btn);
            list.appendChild(li);
        }
        loadTasks();
    })
    .catch(error => console.error(error));
}

document.querySelector("#taskInput").addEventListener("keydown", event => {
    if (event.key === "Enter") {
        addTask();
    }
});