from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database, models, ai_engine

app = FastAPI()

# --- CORS SETUP ---
# This allows your frontend to communicate with your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for easy testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"status": "Rayeva AI Engine is Online"}

@app.post("/catalog/auto-tag")
def tag_product(name: str, description: str, db: Session = Depends(database.get_db)):
    metadata = ai_engine.generate_product_metadata(name, description)
    new_product = models.Product(
        name=name, 
        category=metadata["primary_category"], 
        sustainability_score=metadata["sustainability_score"]
    )
    db.add(new_product)
    db.commit()
    return metadata

@app.post("/whatsapp/webhook")
def whatsapp_bot(user_id: str, message: str, db: Session = Depends(database.get_db)):
    logic = ai_engine.handle_whatsapp_logic(user_id, message)
    new_ticket = models.SupportTicket(
        user_id=user_id, 
        message=message, 
        escalated=logic["escalate"]
    )
    db.add(new_ticket)
    db.commit()
    return logic
