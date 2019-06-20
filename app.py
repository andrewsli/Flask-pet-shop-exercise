"""Flask application for a pet store: can view and add pets."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from db import Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

toolbar = DebugToolbarExtension(app)


@app.route("/")
def show_all_pets():
    """Passes list of pet objects to template to return a list of all pets"""
    return render_template('show-pets.html', pets=Pet.get_all())


@app.route("/pets/add-pet")
def add_pet_form():
    """Form to add a pet to inventory"""
    return render_template("add-pet-form.html")


@app.route("/pets/add-pet", methods=["POST"])
def add_pet():
    """When form is submitted, create a new instance of a pet
    and adds to inventory. Then redirects user to the homepage"""
    post_data = request.form
    Pet.add(
        post_data["name"], 
        post_data["age"], 
        post_data["color"], 
        post_data["photo"]
    )
    flash("Your pet has been added to inventory!")
    return redirect("/")


@app.route("/pets/<id_of_pet>")
def show_pet(id_of_pet):
    """Displays pet information.
    If pet does not exist in inventory, redirects to homepage with flashed message.
    """
    if not Pet.find_by_id(id_of_pet):
        flash("Your pet could not be found.")
        return redirect("/")

    pet = Pet.find_by_id(id_of_pet)
    return render_template('show-pet.html', pet_name=pet.name, pet_age=pet.age, 
                                        pet_color=pet.color, pet_img=pet.photo_url)
    