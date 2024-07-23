web: gunicorn run:app
web: GOOGLE_APPLICATION_CREDENTIALS=./exalted-breaker-425319-j4-943ef73cec94.json ./cloud_sql_proxy -instances=exalted-breaker-425319-j4:southamerica-west1:gestor-de-contratos=tcp:3306 & gunicorn run:app
