#clone the repository

# install the dependencies
pip install -r requirements.txt

#set up the database 
python init_db.py

#run the application 
PS C:\to \your \path \event_management> uvicorn main:app --reload


#adding user and getting acccess token
python  add_user.py
python access_token.py


#user the access token aand test the apis using thunder clinet or postman  or swaggger
