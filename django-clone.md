# Airbnb Clone Schedule

(23/12/27)

- Why API
- Installation
- Categories API
  - Without DRF
  - @api_view
  - Serializer
  - GET /categories
  - GET /categories/1
  - \*args, \*\*kwargs
  - POST /categories (.create)
  - PUT /categories/1 (.update)
  - ModelSerializer
  - APIView
  - DELETE /categories/1
  - ModelViewSet
- Amenities API
- Perks API
- Rooms API
  - Serializer Relationships
  - owner=request.user
- Experiences API
- Medias API
  - ImageField -> URLField
- Reviews API
- Wishlists API
- Bookings API
- Direct Messages API

### Extras To Do:

Dynamic Serializer Fields (is_liked)
Pagination

## API Planning:

### Categories

GET POST /categories
GET(Rooms) PUT DELETE /categories/1

### Rooms

GET POST /rooms
GET PUT DELETE /rooms/1
GET /rooms/1/amenities
GET /rooms/1/reviews
GET POST /rooms/1/bookings
GET PUT DELETE /rooms/1/bookings/2
GET POST /amenities [x]
GET PUT DELETE /amenities/1 [x]

### Experiences

GET POST /experiences
GET PUT DELETE /experiences/1
GET /experiences/1/perks
GET POST /experiences/1/bookings
GET PUT DELETE /experiences/1/bookings/2
GET POST /perks
GET PUT DELETE /perks/1

### Medias

POST /medias
DELETE /medias/1

### Users

POST /users
GET /users/rooms
GET /users/experiences
GET /user/bookings
GET PUT /users/1
GET /users/1/reviews

### Reviews

POST /reviews

### Wishlists

GET POST /wishlists
GET PUT DELETE /wishlists/1

### Amenities

### Perks
