curl \
  -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "{ actors { name } }" }' \
  http://127.0.0.1:8000/graphql/
