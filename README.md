# Telegram Bot Microservice
Basis for fully functional fine-grained bot microservice. Implements:
- REST API for integration with other services
- Generic, scalable driver for making requests to other services

## TECH STACK
- fastapi
- pyrogram
- poetry
- docker-compose

## TODO:
- [x] project structure
- [x] fastapi setup
- [x] sample receive endpoints
- [x] webhook server
- [x] sample message handler
- [x] endpoint for sending file to tg servers
- [x] generic message send endpoint
- [ ] driver
- [x] Telegram client message send
- [ ] logging
- [ ] elk integration

## ISSUES:
- [ ] database locked on multiple parallel requests to api, due to multiple instances of pyrogram clients are up
