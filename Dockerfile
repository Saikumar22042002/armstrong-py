# Stage 1: Builder
FROM python:3.11-slim-bookworm as builder

WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements and install dependencies into a target directory
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim-bookworm

WORKDIR /app

# Create a non-root user for security
RUN addgroup --system appuser && adduser --system --ingroup appuser appuser

# Copy installed packages from the builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY app.py .

# Set ownership and switch to the non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Expose the application port
EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:5000", "app:app"]
