
# FastAPI Person Endpoints

This is a simple API with endpoints for creating, reading, updating, and deleting Person objects from a PostgreSQL database. A Person is an entity with the following properties: first name, last name, and age. I'm using Pydantic serializer to validate my requests/ responses and the SQLAlchemy toolkit for Object-Relational Mapping (see models.py file). There's no front-end, I'm just accessing these endpoints with the Swagger UI that comes built-in to FastAPI. It's very nifty! 


Thanks to the following tutorials for guiding me through this:
- https://www.fastapitutorial.com/blog/fastapi-course/
- https://youtu.be/hrWlXsx48Ss
- https://youtu.be/2g1ZjA6zHRo
- https://youtu.be/GN6ICac3OXY
