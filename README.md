> docker build -t tokenizer .
> docker run -p 8000:8000 tokenizer

> curl -X POST http://localhost:8000/tokenize \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, world!"}'

Returns:
{"tokens": [19706, 11, 1879, 28808], "count": 4}