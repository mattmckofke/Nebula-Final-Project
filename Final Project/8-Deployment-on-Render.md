### 🛠️ 8. Deployment on Render

Deploying your Flask application on Render involves several key steps from configuring the deployment settings to monitoring the application post-deployment.

#### Step 8.1: Prepare Your Application for Deployment

First, ensure your Flask application is ready for deployment. This includes organizing your project structure, setting up environment variables, and ensuring all dependencies are correctly listed.

1. **Organize Project Structure**: Ensure your project files are neatly organized. Typical Flask application structure:

   - `app.py`: Main application file where Flask app and routes are defined.
   - `requirements.txt`: List of all Python dependencies.
   - `Procfile`: Specifies the commands that are executed by the app on startup.

2. **Create a `requirements.txt`**:

   - List all the dependencies needed for your project. You can generate this file using pip:
     ```bash
     pip freeze > requirements.txt
     ```

3. **Create a `Procfile`**:
   - This file tells Render how to run your application.
     ```
     web: python app.py
     ```

#### Step 8.2: Create a GitHub Repository

Since Render deploys applications directly from your GitHub repository, you need to:

1. **Create a new GitHub repository** and initialize it in your project folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. **Push your local repository to GitHub**:
   ```bash
   git remote add origin [Your-GitHub-Repository-URL]
   git push -u origin master
   ```

#### Step 8.3: Set Up Deployment on Render

1. **Sign in to Render**: Go to [Render's website](https://render.com) and sign in or create an account.
2. **Create a New Web Service**:

   - Click on "New +", then select "Web Service".
   - Choose your repository and branch from GitHub.
   - Set the build command and start command as per your `Procfile`.
   - Configure environment variables if your application requires them (e.g., database URLs, API keys).

3. **Deploy Your Application**:
   - After configuring your settings, click "Create Web Service".
   - Render will build and deploy your application. You can monitor the progress and check logs directly on Render's dashboard.

#### Step 8.4: Monitor and Troubleshoot

Once your application is deployed, you should:

- **Check the logs**: Render provides logs where you can see the build and runtime output, which is useful for troubleshooting any issues.
- **Test the deployed application**: Ensure that the live application functions as expected by accessing the provided URL and testing all routes.

#### Step 8.5: Update and Redeploy

If you need to make changes to your application after the initial deployment:

- Make changes locally and commit them.
- Push the updates to GitHub.
- Render automatically detects changes to your repository and redeploy your application.

### 🚀 Next Steps

With your Flask application successfully deployed on Render, you now have a live API that can serve dynamic visualizations to users anywhere. The final step is to document the setup and API usage instructions, which will help users and future developers understand and utilize your application effectively.

Deploying on Render simplifies the management and scaling of your application, providing you a platform that automates much of the deployment and maintenance process.

# ⚠️ IF YOUR API IS NOT DEPLOYING PROPERLY, MAKE SURE THIS IS AT THE BOTTOM. RENDER USES PORT 10000 BY DEFAULT.

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
```
