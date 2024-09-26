from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Task list to store tasks
todo_list = [
    {"id": 1, "title": "Learn Flask", "complete": False},
    {"id": 2, "title": "Build a To-Do App", "complete": False},
    {"id": 3, "title": "Deploy the app", "complete": False}
]

# Home route
@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

# Add new task
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_id = len(todo_list) + 1
        todo_list.append({"id": new_id, "title": title, "complete": False})
    return redirect(url_for('index'))

# Update task completion
@app.route('/update/<int:task_id>')
def update(task_id):
    for task in todo_list:
        if task["id"] == task_id:
            task["complete"] = not task["complete"]
            break
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    for task in todo_list:
        if task["id"] == task_id:
            todo_list.remove(task)
            break
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
