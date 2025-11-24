# SkillMatchApp

A Django-based skill matching application that helps users find relevant jobs, open-source projects, and online courses based on their skills and resume.

## Features

- Resume upload and skill extraction
- Job recommendations via Adzuna API
- Open-source project suggestions via GitHub API
- Course recommendations from online learning platforms
- User authentication and profile management

## Tech Stack

- **Backend**: Django 5.1.7
- **ML/NLP**: spaCy, scikit-learn
- **APIs**: Adzuna (jobs), GitHub (projects)
- **Database**: SQLite (development), PostgreSQL (production-ready)

## Quick Start

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/SharpKushagra/SkillMatchApp.git
   cd SkillMatchApp
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\Activate.ps1
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. Set up environment variables (create `.env` file):
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ADZUNA_API_ID=your-adzuna-api-id
   ADZUNA_API_KEY=your-adzuna-api-key
   GITHUB_API_TOKEN=your-github-token
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run development server:
   ```bash
   python manage.py runserver
   ```

8. Access the app at `http://127.0.0.1:8000`

## Deployment

This project is configured for easy deployment on **Render**. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy to Render

1. Push your code to GitHub
2. Sign up at [Render.com](https://render.com)
3. Create a new Web Service from your GitHub repository
4. Render will auto-detect the `render.yaml` configuration
5. Add your environment variables in the Render dashboard
6. Deploy!

Your app will be live at `https://your-app-name.onrender.com`

## Project Structure

```
SkillMatchApp/
├── core/                 # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── utils.py         # Utility functions (skill extraction, API calls)
│   └── templates/       # HTML templates
├── skillmatch/          # Django project settings
├── static/              # Static files (CSS, images)
├── requirements.txt     # Python dependencies
├── build.sh            # Build script for deployment
├── render.yaml         # Render deployment configuration
└── manage.py           # Django management script
```

## API Keys Setup

To use all features, you'll need:

1. **Adzuna API** (for job search):
   - Sign up at https://developer.adzuna.com/
   - Get your API ID and Key

2. **GitHub Personal Access Token** (for open-source projects):
   - Go to https://github.com/settings/tokens
   - Generate a new token with `public_repo` scope

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Authors

- Kushagra Saxena (@SharpKushagra)
- Aneesha Nigam (@AneeshaNigam)
