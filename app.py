"""Main Flask application file for Armstrong-Py."""

import logging
from flask import Flask, jsonify

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Kubernetes probes."""
    logger.info("Health check requested.")
    return jsonify({"status": "healthy"}), 200


@app.route('/', methods=['GET'])
def index():
    """Main application endpoint."""
    logger.info("Main endpoint requested.")
    return jsonify({"message": "Armstrong-Py: Houston, we have a server!"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
