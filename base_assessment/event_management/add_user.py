#from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


db = SessionLocal()


hashed_password = pwd_context.hash("testpassword1")
db_user = User(username="testuser1", email="testuser1@example.com", password=hashed_password)


db.add(db_user)
db.commit()
db.refresh(db_user)

db.close()

print("User created successfully!")