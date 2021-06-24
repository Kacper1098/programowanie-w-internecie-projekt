# Use an official node runtime as a parent image
FROM node:alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# Install dependencies
COPY ./frontend/package*.json /app/
RUN npm install --silent --save-dev dotenv
RUN npm install @vue/cli@3.12.1 -g

# Add rest of the client code
COPY ./frontend /app/

EXPOSE 8080

CMD ["npm", "run", "serve"]