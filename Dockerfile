FROM nginx:alpine
RUN apk add --no-cache git
WORKDIR /tmp
RUN git clone https://github.com/dhearahma7/final-destination-12.git
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
<<<<<<< HEAD
RUN git https://github.com/dhearahma7/final-destination-12.git .
=======
RUN cp -r /tmp/final-destination-12/webapp/* .
>>>>>>> 5186f38 (update dockerfile)
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
