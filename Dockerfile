FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./accomodation_website /app/accomodation_website
COPY ./uwsgi.ini /app/uswgi.ini
