from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="DontSurf API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your extension's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextContent(BaseModel):
    title: str
    content: str

class BookRecommendation(BaseModel):
    title: str
    author: str
    description: str
    topics: List[str]

# Dummy book database
BOOKS: Dict[str, List[BookRecommendation]] = {
    "technology": [
        BookRecommendation(
            title="Clean Code",
            author="Robert C. Martin",
            description="A handbook of agile software craftsmanship",
            topics=["technology", "programming"]
        ),
        BookRecommendation(
            title="The Pragmatic Programmer",
            author="Andrew Hunt, David Thomas",
            description="Your journey to mastery",
            topics=["technology", "programming"]
        )
    ],
    "psychology": [
        BookRecommendation(
            title="Thinking, Fast and Slow",
            author="Daniel Kahneman",
            description="Understanding how our minds work",
            topics=["psychology", "science"]
        ),
        BookRecommendation(
            title="Atomic Habits",
            author="James Clear",
            description="Tiny changes, remarkable results",
            topics=["psychology", "self-help"]
        )
    ],
    "science": [
        BookRecommendation(
            title="A Brief History of Time",
            author="Stephen Hawking",
            description="From the Big Bang to Black Holes",
            topics=["science", "physics"]
        ),
        BookRecommendation(
            title="Sapiens",
            author="Yuval Noah Harari",
            description="A Brief History of Humankind",
            topics=["science", "history"]
        )
    ],
    "business": [
        BookRecommendation(
            title="Zero to One",
            author="Peter Thiel",
            description="Notes on startups, or how to build the future",
            topics=["business", "entrepreneurship"]
        ),
        BookRecommendation(
            title="Good to Great",
            author="Jim Collins",
            description="Why some companies make the leap and others don't",
            topics=["business", "management"]
        )
    ],
    "health": [
        BookRecommendation(
            title="Why We Sleep",
            author="Matthew Walker",
            description="Unlocking the power of sleep and dreams",
            topics=["health", "science"]
        ),
        BookRecommendation(
            title="The 4-Hour Body",
            author="Timothy Ferriss",
            description="An uncommon guide to rapid fat-loss, incredible sex, and becoming superhuman",
            topics=["health", "fitness"]
        )
    ],
    "general": [
        BookRecommendation(
            title="The Alchemist",
            author="Paulo Coelho",
            description="A philosophical novel",
            topics=["fiction", "philosophy"]
        ),
        BookRecommendation(
            title="Meditations",
            author="Marcus Aurelius",
            description="Personal writings of the Roman Emperor",
            topics=["philosophy", "self-help"]
        )
    ]
}

@app.get("/ping")
async def ping():
    return {"message": "Hello, world!"}

@app.post("/classify")
async def classify_text(text_content: TextContent) -> List[str]:
    """
    Classify the given text content into topics.
    For now, returns dummy topics based on simple keyword matching.
    """
    # Dummy implementation - in real app, this would use ML/NLP
    topics = []
    
    # Simple keyword matching
    keywords = {
        "technology": ["tech", "computer", "software", "hardware", "programming", "code"],
        "psychology": ["mind", "behavior", "psychology", "mental", "brain"],
        "science": ["science", "research", "experiment", "study", "scientific"],
        "business": ["business", "market", "company", "startup", "entrepreneur"],
        "health": ["health", "fitness", "wellness", "medical", "diet"]
    }
    
    # Check title and content for keywords
    text = f"{text_content.title} {text_content.content}".lower()
    
    for topic, words in keywords.items():
        if any(word in text for word in words):
            topics.append(topic)
    
    # If no topics found, return a default
    if not topics:
        topics = ["general"]
    
    return topics

@app.get("/recommend")
async def get_recommendations(topics: str) -> List[BookRecommendation]:
    """
    Get book recommendations based on topics.
    Topics should be comma-separated, e.g., "technology,psychology"
    """
    # Split topics string into list
    topic_list = [t.strip() for t in topics.split(",")]
    
    # Get recommendations for each topic
    recommendations = []
    for topic in topic_list:
        if topic in BOOKS:
            recommendations.extend(BOOKS[topic])
    
    # If no recommendations found, return general recommendations
    if not recommendations:
        recommendations = BOOKS["general"]
    
    # Return up to 5 recommendations
    return recommendations[:5]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 