from flask import render_template, url_for, flash, redirect, request, jsonify
from app import app, db
from app.models import FAQ, Interaction
from app.forms import QueryForm
import spacy

nlp = spacy.load('en_core_web_sm')

def find_answer(query):
    faqs = FAQ.query.all()
    best_match = None
    highest_similarity = 0
    doc1 = nlp(query)
    for faq in faqs:
        doc2 = nlp(faq.question)
        similarity = doc1.similarity(doc2)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = faq
    return best_match.answer if best_match else "I'm sorry, I don't understand your question. Can you please rephrase?"

@app.route("/", methods=['GET', 'POST'])
def chat():
    form = QueryForm()
    if form.validate_on_submit():
        user_query = form.query.data
        bot_response = find_answer(user_query)
        interaction = Interaction(user_query=user_query, bot_response=bot_response)
        db.session.add(interaction)
        db.session.commit()
        return jsonify({'response': bot_response})
    return render_template('chat.html', form=form)
