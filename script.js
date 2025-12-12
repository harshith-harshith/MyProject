/* ====================================================
   Smart Study Planner - JavaScript
==================================================== */

/* ------------------------------
   Initialize Tasks from Local Storage
------------------------------ */
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

const taskList = document.getElementById("task-list");
const progressBar = document.getElementById("progress");

/* ------------------------------
   Save Tasks to Local Storage
------------------------------ */
function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

/* ------------------------------
   Add New Task
------------------------------ */
document.getElementById("add-task").addEventListener("click", () => {
    const name = document.getElementById("task-name").value.trim();
    const duration = parseInt(document.getElementById("task-duration").value);
    const priority = document.getElementById("task-priority").value;

    if (!name || !duration) {
        alert("Enter valid task name & duration!");
        return;
    }

    tasks.push({
        name,
        duration,
        priority,
        completed: false,
        date: new Date().toDateString()
    });

    document.getElementById("task-name").value = "";
    document.getElementById("task-duration").value = "";

    scheduleTasks();
});

/* ------------------------------
   Smart Scheduler by Priority
------------------------------ */
function scheduleTasks() {
    const priorityMap = { High: 3, Medium: 2, Low: 1 };
    tasks.sort((a, b) => priorityMap[b.priority] - priorityMap[a.priority]);
    
    renderTasks();
    saveTasks();
    updateProgress();
}

/* ------------------------------
   Render Tasks in the List
------------------------------ */
function renderTasks() {
    taskList.innerHTML = "";

    tasks.forEach((task, index) => {
        const li = document.createElement("li");
        li.className = task.completed ? "completed" : "";

        const emoji = task.priority === "High" ? "🔥" :
                      task.priority === "Medium" ? "🙂" : "😴";

        li.innerHTML = `
            ${emoji} <b>${task.name}</b> (${task.duration}h)
            <span>
                <button class="complete-btn" onclick="toggleComplete(${index})">✔</button>
                <button class="delete-btn" onclick="deleteTask(${index})">✖</button>
            </span>
        `;

        taskList.appendChild(li);
    });
}

/* ------------------------------
   Complete / Delete Task
------------------------------ */
function toggleComplete(index) {
    tasks[index].completed = !tasks[index].completed;
    scheduleTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    scheduleTasks();
}

/* ------------------------------
   Update Progress Bar
------------------------------ */
function updateProgress() {
    if (tasks.length === 0) {
        progressBar.style.width = "0%";
        return;
    }

    const completedTasks = tasks.filter(t => t.completed).length;
    const percent = Math.round((completedTasks / tasks.length) * 100);
    progressBar.style.width = percent + "%";
}

/* ------------------------------
   Suggest Time Slots
------------------------------ */
document.getElementById("suggest-times").addEventListener("click", () => {
    const availableHours = parseInt(document.getElementById("available-hours").value);

    if (!availableHours || availableHours <= 0) {
        alert("Enter available hours!");
        return;
    }

    const remainingHours = tasks.reduce((sum, task) => {
        return sum + (task.completed ? 0 : task.duration);
    }, 0);

    let msg = "";
    if (remainingHours <= availableHours) {
        msg = "✔ You can finish all tasks today!";
    } else {
        msg = `⚠ You need ${remainingHours - availableHours} more hours. Focus on HIGH priority tasks!`;
    }

    alert(msg);
});

/* ------------------------------
   Daily / Weekly View
------------------------------ */
document.getElementById("daily-view").addEventListener("click", () => {
    const today = new Date().toDateString();
    tasks = tasks.filter(task => task.date === today);
    scheduleTasks();
});

document.getElementById("weekly-view").addEventListener("click", () => {
    tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    scheduleTasks();
});

/* ------------------------------
   Initialize App
------------------------------ */
scheduleTasks();
