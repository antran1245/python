from flask_app import app, bcrypt
from flask import render_template, request, redirect, url_for, session

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# Display routes
@app.route('/dashboard')
def showDashboard():
    if 'remember' in session:
        if 'uuid' in session:
            data = {
                "id" : session['uuid']
            }
            user = Recipe.get_all_from_user(data)
            if session['remember'] == 'off':
                del session['uuid']
                del session['remember']
            return render_template('dashboard.html', user=user)
    return redirect('/')

@app.route('/recipes/new')
def addRecipe():
    data = {
        "id" : session['uuid']
    }
    user = User.select(data)
    return render_template('add.html', user=user)

@app.route('/recipes/edit/<int:id>')
def editRecipe(id):
    data = {
        "recipe_id" : id
    }
    recipe = Recipe.get_one_from_user(data)
    return render_template('edit.html', recipe=recipe)

@app.route('/recipes/<int:id>')
def viewRecipe(id):
    data = {
        "recipe_id" : id
    }
    recipe = Recipe.get_one_from_user(data)
    return render_template('view.html', recipe=recipe)

@app.route('/recipes/delete/<int:id>')
def deleteRecipes(id):
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

# Action routes
@app.route('/process/add', methods=['POST'])
def addingRecipe():
    if not Recipe.validate_input(request.form):
        return redirect('/recipes/new')
    data = {
        "user_id" : session['uuid'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "time" : request.form['time']
    }
    Recipe.insert(data)
    return redirect('/dashboard')

@app.route('/process/edit/<int:id>', methods=['POST'])
def editingRecipe(id):
    if not Recipe.validate_input(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        "recipe_id" : id,
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "time" : request.form['time']
    }
    Recipe.update(data)
    return redirect('/dashboard')