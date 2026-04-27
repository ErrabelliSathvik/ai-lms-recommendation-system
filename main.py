
from fastapi import FastAPI
from recommender import recommend
from embeddings import get_embedding

app = FastAPI()

courses = [
    "Data Science",
    "Web Development",
    "Machine Learning"
]

@app.get("/")
def home():
    return {"message": "AI LMS Recommendation System Running"}

@app.post("/recommend")
def get_recommendation(user_input: str):
    user_vec = get_embedding(user_input)
    course_vecs = [get_embedding(c) for c in courses]

    scores = recommend(user_vec, course_vecs)

    return {
        "courses": courses,
        "scores": scores.tolist()
    }
