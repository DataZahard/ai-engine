from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database, models, ai_engine

app = FastAPI()

# Create tables on startup
models.Base.metadata.create_all(bind=database.engine)

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
