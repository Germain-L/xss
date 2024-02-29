# XSS Vulnerability Demo

This project is a simple Flask application that demonstrates a Cross-Site Scripting (XSS) vulnerability. It's a basic comment system where users can post comments that are displayed to everyone.

## How it works

The application has a single page where users can submit comments via a form. The comments are stored in a list on the server and are rendered directly into the HTML of the page. This direct rendering of user input creates an XSS vulnerability.

## How to run the project

### Locally with Python

To run the application locally, follow these steps:

1. Clone the repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run the server with `python server.py`.

### Locally with Docker
You can also run the application using Docker. Here are the steps:

1. Build the Docker image: `docker build -t xss-demo .`
2. Run the Docker container: `docker run -p 5000:5000 xss-demo`

## How to test the XSS vulnerability

You can test the XSS vulnerability by posting a comment that includes some JavaScript code. For example, you could post the comment `<script>alert('XSS')</script>`, and an alert box will pop up for anyone who views the page.

## Live Demo

You can view a live demo of the application at [https://xss-production.up.railway.app](https://xss-production.up.railway.app).