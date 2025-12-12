.

📘 Smart Study Planner

A lightweight, interactive study management web application built using HTML, CSS, and JavaScript.
The system helps students organize daily and weekly study tasks, prioritize work, track progress, and plan efficiently using smart time recommendations.

🚀 Features
1. Smart Task Scheduling

Tasks are automatically sorted using a priority-based scheduler:

🔥 High Priority

🙂 Medium Priority

😴 Low Priority

The system ensures that important tasks always appear at the top of the list.

2. Daily & Weekly Views

Users can switch between:

Daily View – Displays tasks created today

Weekly View – Displays all tasks saved locally

This helps maintain short-term and long-term planning.

3. Progress Tracking

A dynamic progress bar updates automatically as tasks are completed, giving a visual representation of daily productivity.

4. Time Slot Suggestion System

Based on the number of hours the user has available for the day, the system:

Calculates whether all tasks can be completed

Suggests focusing on high-priority tasks if time is insufficient

5. Local Storage Support

All tasks are saved in the browser’s localStorage, ensuring:

No login required

Tasks persist even after page refresh

6. Modern, Responsive UI

Gradient background

Clean card design

Hover animations

Intuitive task controls (complete/delete)

🏗️ Tech Stack
Frontend

HTML5

CSS3

JavaScript (ES6)

Storage

Browser LocalStorage

📂 Project Structure
│── index.html         # Main interface
│── style.css          # Styling and layout
│── script.js          # Core application logic
│── README.md          # Documentation

⚙️ How the System Works
1. Add Tasks

Users input:

Task name

Duration (in hours)

Priority level

Tasks are then stored and ranked automatically.

2. Smart Priority Scheduling

Tasks are sorted internally based on:

High Priority → Medium Priority → Low Priority

3. Completing or Deleting Tasks

✔ Mark tasks as completed

✖ Delete tasks
Both operations instantly update the progress bar and re-render the UI.

4. Time Slot Recommendation

The system calculates:

Total hours required for all pending tasks

Available hours entered by the user

It then provides suggestions such as:

“You can finish all tasks today.”

“You need 3 more hours. Focus on high-priority tasks.”

5. Persistent Storage

localStorage ensures tasks remain available every time the user revisits the page.
