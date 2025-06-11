FROM nginx:alpine
RUN apk add --no-cache git
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
RUN git https://github.com/dhearahma7/final-destination-12.git .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
