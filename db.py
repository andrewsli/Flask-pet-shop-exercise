"""API for storing, retrieving, and adding pets."""

# Used to "slugify" names -> id [see note below]
from slugify import slugify


PLACEHOLDER_IMG = "https://thehappypuppysite.com/wp-content/uploads/2017/09/cute4.jpg"


class Pet():
    """A pet, along with class methods for adding and retriving pets."""

    # We've named this with a leading underscore to
    # strongly warn users of this class not to use this variable directly,
    # but to instead use our public methods.

    _pets  = {}

    def __init__(self, name, color, age, photo_url):
        """Make Pet instance from data."""

        self.name = name
        self.color = color
        self.age = age
        self.photo_url = photo_url

        # For the ID, we'll use a "slugified" version of the pet name.
        # A "slug" is a term for a string that is very url-friendly (no spaces,
        # punctuation, and all lower case). So, for example, the name
        # "Whiskey the Dog" would turn into the slug "whiskey-the-dog".
        self.id = slugify(name)

    def __repr__(self):
        return f"""<Pet id="{self.id}" name="{self.name}">"""

    @classmethod
    def get_all(cls):
        """Returns list of pet instances of all pets in our pet shop."""

        return [pet for pet in cls._pets.values()]
    
    @classmethod
    def add(cls, name, color, age, photo_url):
        """Creates new pet and adds to storage of all pets."""

        if not photo_url:
            photo_url = PLACEHOLDER_IMG

        new_pet = cls(name, color, age, photo_url)
        cls._pets[new_pet.id] = new_pet
    
    @classmethod
    def find_by_id(cls, pet_id):
        """Find pet from the pet ID. If not found, returns None."""

        return cls._pets.get(pet_id)


Pet.add("Whiskey", "black & white", 7, "https://www.rithmschool.com/assets/team/whiskey-b19e7b9d17b43ac303323c552d46b3ddaf18d38ded9d10e4e1fa39f63c06622b.jpg")
Pet.add("Ezra", "orange", 8, "https://live.staticflickr.com/5245/5263873646_a01baff41b_b_d.jpg")