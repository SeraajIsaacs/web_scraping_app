from app import create_app  # Importing create_app from app/__init__.py

app = create_app()

# Root URL route
@app.route('/')
def home():
    return '''
        <html>
            <head>
                <meta http-equiv="refresh" content="5; url=/auth/register" />
            </head>
            <body>
                <h1>Welcome to the Web Scraping App!</h1>
                <p>You will be redirected to the registration page shortly...</p>
            </body>
        </html>
    '''

# Ensure app runs with debug mode on
if __name__ == "__main__":
    app.run(debug=True)
