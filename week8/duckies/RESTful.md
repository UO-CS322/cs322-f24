
# Adding a RESTful API

To extend your Flask application with a RESTful API endpoint that retrieves a list of all the ducks from the MongoDB database, you can add a new route. This route will query the MongoDB collection and return the results in JSON format.

## Step-by-Step Guide
Here's how you can add this functionality:

1. Define a new route for the RESTful API that retrieves all ducks.

2. Query the Database to fetch all duck documents from the ducks collection.

3. Return the Data in JSON format.

4. Update your `app.py` file to include the following changes:

```python
@app.route('/ducks', methods=['GET'])
def get_all_ducks():
    # Fetch all duck documents from the collection
    ducks = list(ducks_collection.find())
    
    # Convert ObjectId to string and format documents
    for duck in ducks:
        duck['_id'] = str(duck['_id'])
        
    return jsonify(ducks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
```

## Explanation

* Route `/ducks`: This new endpoint responds to GET requests. It queries all documents from the ducks collection and returns them as a JSON array.

* ObjectId Conversion: MongoDB's default `_id` field is an ObjectId, which isn't JSON serializable. We convert it to a string for each document before returning them. Another way is to use `dumps` as we do in the `/search_duck` route.

* Return JSON Response with `jsonify`

## Testing the New Endpoint
To test this API, you can use tools like Postman or CURL, or simply navigate to http://localhost:5005/ducks in your browser, assuming your Flask server is running. This should return a JSON array containing all the ducks in the database.

Summary. This RESTful API extension provides a simple way to list all ducks, making it suitable for integration with other services or front-end applications that need access to this data.