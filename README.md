# Flask API Deployment

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your values
3. Install dependencies: `pip install -r requirements.txt`

## Local Development

```bash
python flask_app.py
```

## Deployment Steps

### Database Setup
1. Create a PostgreSQL database on Render
2. Copy the database URI to your `.env` file

### Render Deployment
1. Push code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add environment variables:
   - `DATABASE_URI`
   - `SECRET_KEY`
5. Deploy

### Update Swagger Documentation
After deployment:
- Update swagger host to your Render URL (without https://)
- Change swagger schemes from `http` to `https`

### GitHub Secrets
Add these secrets to your GitHub repository:
- `RENDER_API_KEY` - Your Render API key
- `SERVICE_ID` - Your Render service ID

## CI/CD Pipeline

The pipeline runs automatically on push to main:
1. Build - Installs dependencies
2. Test - Runs pytest
3. Deploy - Deploys to Render (only after tests pass)
