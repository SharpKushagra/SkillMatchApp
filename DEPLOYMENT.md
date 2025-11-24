# Deployment Guide for SkillMatchApp

This guide will help you deploy your SkillMatchApp to Render.

## Prerequisites

1. A GitHub account with your repository: https://github.com/SharpKushagra/SkillMatchApp
2. A Render account (sign up at https://render.com - free tier available)
3. API keys (optional but recommended):
   - Adzuna API: https://developer.adzuna.com/
   - GitHub Personal Access Token: https://github.com/settings/tokens

## Deployment Steps

### Step 1: Push Changes to GitHub

Make sure all your changes are committed and pushed to GitHub:

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Step 2: Create Render Account

1. Go to https://render.com
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### Step 3: Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. In Render dashboard, click "New" → "Blueprint"
2. Connect your GitHub repository: `SharpKushagra/SkillMatchApp`
3. Render will automatically detect the `render.yaml` file
4. Click "Apply" to deploy

#### Option B: Manual Setup

1. In Render dashboard, click "New" → "Web Service"
2. Connect your GitHub repository: `SharpKushagra/SkillMatchApp`
3. Configure the service:
   - **Name**: `skillmatch-app` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn skillmatch.wsgi:application`
   - **Plan**: Free (or choose a paid plan)

### Step 4: Configure Environment Variables

In your Render service dashboard, go to "Environment" tab and add:

1. **SECRET_KEY**: 
   - Generate a new secret key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - Or use Render's auto-generated one

2. **DEBUG**: Set to `False` for production

3. **ALLOWED_HOSTS**: 
   - Your Render service URL (e.g., `skillmatch-app.onrender.com`)
   - Or use `*` for testing (not recommended for production)

4. **ADZUNA_API_ID**: Your Adzuna API ID (optional)

5. **ADZUNA_API_KEY**: Your Adzuna API Key (optional)

6. **GITHUB_API_TOKEN**: Your GitHub Personal Access Token (optional)

### Step 5: Deploy

1. Click "Create Web Service" (or "Apply" if using Blueprint)
2. Render will:
   - Clone your repository
   - Install dependencies
   - Download spacy model
   - Collect static files
   - Run migrations
   - Start the server

### Step 6: Access Your App

Once deployment is complete, your app will be available at:
`https://your-service-name.onrender.com`

## Post-Deployment

### Create a Superuser

To access the Django admin panel:

1. Go to your Render service dashboard
2. Open the "Shell" tab
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow the prompts to create an admin user

### Monitor Logs

- View logs in the Render dashboard under "Logs" tab
- Check for any errors or warnings

## Troubleshooting

### Build Fails

- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify the build script has execute permissions

### Static Files Not Loading

- Ensure `whitenoise` is installed (already in requirements.txt)
- Check that `collectstatic` ran successfully
- Verify `STATIC_ROOT` is set correctly

### Database Issues

- SQLite is used by default (works on free tier)
- For production, consider upgrading to PostgreSQL (paid plan)
- Run migrations: `python manage.py migrate`

### Spacy Model Issues

- The build script downloads `en_core_web_sm` automatically
- If it fails, check the build logs
- You can manually download it in the shell

## Alternative Deployment Platforms

### Railway

1. Go to https://railway.app
2. Connect GitHub repository
3. Railway auto-detects Django projects
4. Add environment variables
5. Deploy!

### Fly.io

1. Install flyctl: `curl -L https://fly.io/install.sh | sh`
2. Run: `fly launch`
3. Follow prompts
4. Deploy: `fly deploy`

### Heroku

1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Set environment variables
4. Deploy: `git push heroku main`

## Notes

- The free tier on Render may spin down after inactivity (takes ~30 seconds to wake up)
- For production, consider upgrading to a paid plan
- Always keep your `SECRET_KEY` secret and never commit it to Git
- Use environment variables for all sensitive data

## Support

For issues or questions:
- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

