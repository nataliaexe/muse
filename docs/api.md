# MUSE API Documentation

## Base URL

http://localhost:8000/api/v1
text


## Endpoints

### Health
- `GET /health/` - Check service health
- `GET /health/database` - Check database connection

### Users
- `POST /users/` - Create new user
- `GET /users/{user_id}` - Get user information
- `PUT /users/{user_id}/style-dna` - Update user Style DNA

### Events
- `POST /events/` - Create new event
- `GET /events/user/{user_id}` - Get user events
- `GET /events/types` - Get available event types

## Event Types

### User Events
- USER_LIKED_POST
- USER_SAVED_LOOK
- USER_REJECTED_LOOK
- USER_VIEWED_PRODUCT
- USER_SEARCHED_STYLE
- USER_ADDED_CLOTHING
- USER_WORE_OUTFIT
- USER_COMPLETED_QUIZ
- USER_DISCOVERED_STYLE
- USER_FOLLOWED_CREATOR
- USER_VIEWED_TREND
- USER_PURCHASED_PRODUCT

## Authentication

JWT-based authentication (to be implemented)
