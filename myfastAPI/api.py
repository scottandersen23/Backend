from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserResponse
from auth import get_current_user, create_access_token, hash_password, verify_password
from security import create_jwt_token, decode_jwt_token

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_verified=False,
        role="user",
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/token")
def login_for_access_token(form_data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data["username"]).first()
    if not user or not verify_password(form_data["password"], user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not user.is_verified:
        raise HTTPException(status_code=400, detail="Email not verified")
    access_token = create_jwt_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/verify-email/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):
    payload = decode_jwt_token(token)
    user = db.query(User).filter(User.email == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    user.is_verified = True
    db.commit()
    return {"message": "Email successfully verified"}
