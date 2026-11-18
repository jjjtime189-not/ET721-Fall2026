const list = document.querySelector('#taskList');
const li = document.createElement('li');
function loadTasks() {
    fetch("/get_tasks")
        .then(Response => Response.json())
        .then(tasks => {
            const list = document.querySelector("#taskList");
            list.innerHTML = "";
        tasks.forEach(task => {
            const li = document.createElement("li");
            li.textContent = task.task;
            li.classList.add("task_item");
            list.appendChild(li);
            const btn= document.createElement("button");
            btn.innerHTML = "&#10060;";
            btn.classList.add("btndeletetask");
            btn.onclick = () => {
                fetch("/delete_task", {
                    method: "POST",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({task: task.task})
                })
                .then(() => loadTasks());
                };
                li.appendChild(btn);
            });
        });
}
window.onload = loadTasks;
function addTask() {
    const inputtask = document.querySelector("#taskInput");
    const task = inputtask.value.trim();
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