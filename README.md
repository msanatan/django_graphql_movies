# django_graphql_movies

This is a sample application that will accompany my upcoming blog post on [Stack Abuse](https://stackabuse.com). This post introduces GraphQL, designs a schema for movies and details how to create the GraphQL API with Graphene and Django.

Aside from the Django application, this repo also includes the following:

* **schema.graphql** - the complete GraphQL schema
* **queries.graphql** - an exmaple of every query and mutation defined in the schema
* **actorQuery.sh** - a sample cURL request to communicate with the API
* **movies.json** - test data

## Setting up

Clone this repo, and in the directory follow these steps:

```bash
# Create virtual environment
python3 -m venv env
# Activate virtual environment
. env/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run DB migration
python manage.py migrate
# Optional: load test data
python manage.py loaddata movies.json
# Run the application
python manage.py runserver
```

If you go to http://127.0.0.1:8000/graphql/, you'll be able to interact with the API there.
