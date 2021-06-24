# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend/

# Install Python dependencies for development
COPY ./backend/requirements.txt requirements.txt
RUN pip3 install --upgrade pip -r requirements.txt


# Add the rest of the code
COPY ./backend /app/backend/

# Make port 8000 available for the app
EXPOSE 8000

COPY ./docker/backend/django-entrypoint.sh /
RUN chmod +x /django-entrypoint.sh


#ENTRYPOINT ["/django-entrypoint.sh"]
