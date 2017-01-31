FROM python:2-onbuild

EXPOSE 5000
CMD [ "python", "articles_sort_webserver.py" ]
