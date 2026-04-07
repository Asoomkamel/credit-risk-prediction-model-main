# Deployment Guide

This document provides comprehensive deployment instructions for the Credit Risk Prediction Model.

## Local Development

### Prerequisites
- Python 3.11+
- pip or pip3

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Asoomkamel/credit-risk-prediction-model-main.git
cd credit-risk-prediction-model-main
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

## Docker Deployment

### Using Docker Compose (Recommended)

1. Ensure Docker and Docker Compose are installed
2. Run:
```bash
docker-compose up --build
```

3. Access at `http://localhost:8501`

### Manual Docker Build

1. Build the image:
```bash
docker build -t credit-risk-model:latest .
```

2. Run the container:
```bash
docker run -p 8501:8501 \
  -v $(pwd)/artifacts:/app/artifacts:ro \
  credit-risk-model:latest
```

## Streamlit Cloud Deployment

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `main.py`
6. Click "Deploy"

## Environment Variables

Configure the following environment variables as needed:

- `MODEL_PATH`: Path to the model file (default: `artifacts/model_data.joblib`)

Example:
```bash
export MODEL_PATH=/path/to/model_data.joblib
streamlit run main.py
```

## Production Considerations

### Performance Optimization
- Model is loaded once and cached for efficiency
- Streamlit's built-in caching prevents redundant computations
- Use `@st.cache_resource` for singleton resources

### Security
- Validate all user inputs
- Use environment variables for sensitive configurations
- Run behind a reverse proxy (nginx/Apache) in production
- Enable HTTPS/TLS

### Monitoring
- Monitor application logs
- Track prediction latency
- Set up alerts for errors
- Monitor resource usage (CPU, memory)

### Scaling
- Use container orchestration (Kubernetes) for horizontal scaling
- Implement load balancing
- Consider async processing for high-volume predictions

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

## CI/CD Pipeline

The project includes GitHub Actions for automated testing and building:
- Linting with flake8
- Code formatting checks with black
- Unit tests with pytest
- Docker image building

Workflows are triggered on push to main/develop branches and pull requests.

## Troubleshooting

### Model Loading Error
- Ensure `artifacts/model_data.joblib` exists
- Check file permissions
- Verify `MODEL_PATH` environment variable

### Port Already in Use
```bash
# Change port in docker-compose.yml or use:
streamlit run main.py --server.port 8502
```

### Memory Issues
- Increase Docker memory allocation
- Optimize model size
- Consider model quantization

## Maintenance

### Updating Dependencies
1. Update `requirements.txt`
2. Rebuild Docker image
3. Run tests
4. Deploy

### Model Updates
1. Replace `artifacts/model_data.joblib`
2. Test predictions
3. Deploy

## Support

For issues or questions, open an issue on the GitHub repository.
