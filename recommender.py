
from sklearn.metrics.pairwise import cosine_similarity

def recommend(user_vector, course_vectors):
    similarity = cosine_similarity([user_vector], course_vectors)
    return similarity[0]
