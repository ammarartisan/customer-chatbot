# Navigate to your project directory
cd your\directory

# Activate the virtual environment
venv\Scripts\activate

# Install Flask and Other Dependencies:
pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-WTF spacy
python -m spacy download en_core_web_sm

# Start the Python shell
python

# Run these commands in the Python shell
from app import create_app, db
app = create_app()
app.app_context().push()
db.create_all()

# Optionally, add initial data
from app.models import FAQ
faq1 = FAQ(question="What is your return policy?", answer="You can return any item within 30 days of purchase.")
faq2 = FAQ(question="How can I track my order?", answer="You can track your order using the tracking number provided in the shipping confirmation email.")
db.session.add(faq1)
db.session.add(faq2)
db.session.commit()

# Exit the Python shell
exit()

# Run the Flask application
python run.py
