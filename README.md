# Project

the point of this is to just give me an easy and quick starting point for a python project that I can move quick with.

Since it's meant to move quick, I've set it up using a dockerized Python backend using: sqlAlchemy, flask, poetry, and alembic. I'm using Pytest and factory boy for my test generation.

The front end is made in react.

The db is postgres.

## Running the App

you'll want to copy the `.env.example` as `.env` and then build the app with docker.

```
docker compose build
```

followed by:

```
docker compose up
```

To create the `example_table` in the db, you need to create a migration, and then migrate up.

First you need to run the alembic migration version command (utilizes the models to generate a version file at `flaskBackend/alembic/versions`):

```
docker compose exec api poetry run alembic revision --autogenerate -m "create example table"
```

Then you need to migrate up with:

```
docker compose exec api alembic upgrade head
```

As you create additional sqlAlchemy models, you will need to follow the above process again.

### Testing

The tests I have setup are pretty limited at the moment.

Backend:

```
docker compose exec api poetry run pytest
```

UI:

```
docker compose exec ui yarn test
```

## Package management

Python utilizes poetry here. I find it significantly easier than juggling pip and venv's.

React uses yarn.

## Backend Design Patterns

This follows the common design patterns you see for backend designs. An example of two prominent patterns:

### Chain of Responsibility:

- controller layer for handling the routing
- service layer to help with business logic
- model/repo layer to handle database interactions

### Factory Pattern:

- create a service layer
- create a model layer

Cutting it up this way limits how easy it is to replace each segmented responsibility of the app, and enables creation of each class to be more easily maintained.

## Tradeoffs

This is using postgres which in and of itself limits the app structure to SQL, however that model layer could be ripped out and replaced.

By using an ORM layer, and python package to control the db migrations, you're inherently tightly coupling your backend to your db. As we move to different db solutions to enable AI, that may not be a wise idea. Additionally, tightly coupling your backend packages to the db interactions and structure also potentially put you in a precarious position.

Flask has some negatives to it compared to other frameworks, but the current issues with fastAPI support make it seem very stable and friendly. It would be pretty easy to decouple the controller layer from the package if needed.
