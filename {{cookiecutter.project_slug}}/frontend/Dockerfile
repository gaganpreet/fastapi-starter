FROM node:latest as build

WORKDIR /app

COPY package.json yarn.lock /app/

RUN yarn

COPY . /app/

RUN CI=1 yarn test

RUN yarn build


FROM nginx:latest

COPY --from=build /app/build /usr/share/nginx/html
