from app import app as application
 
if __name__ == "__main__":
	application.run(host="0.0.0.0", debug=True )

# RUN COMMAND
# uwsgi --http :8000 --wsgi-file /h/home/deploy/Desidata/desidata/uwsgi.py
