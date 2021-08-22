echo "Up frontend"
cd ./front
sudo docker-compose up --build -d

echo "Up API + db"
cd ../anl-api
sudo docker-compose up --build -d
echo "Migrating"
sudo docker exec analytics-backend pip install -r requirements-dev.txt
sudo docker exec analytics-backend alembic upgrade head
echo "Lead data"
sudo docker exec analytics-backend python init_db.py
sudo docker exec analytics-backend python init_db_certificates.py
sudo docker exec analytics-backend python init_db_certificates_scores.py
