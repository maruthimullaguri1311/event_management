#clone the repository

# install the dependencies
pip install -r requirements.txt

#set up the database 
python init_db.py

#run the application 
PS C:\to \your \path \event_management> uvicorn main:app --reload


#login and gett access token 
python  add_user.py

#user the access token aand test the apis using thunder clinet or postman  or swaggger
