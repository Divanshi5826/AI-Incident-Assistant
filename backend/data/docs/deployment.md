# Deployment Troubleshooting Guide

## Common Symptoms
- The service works locally but fails after deployment.
- The app starts and then exits immediately.
- Environment variables are missing in production.
- The frontend cannot reach the backend service.
- Static assets or API routes return 404 errors.

## What to Check First
- Confirm the correct start command is used.
- Verify all required environment variables exist.
- Check whether the deployed port matches the platform expectation.
- Make sure the process is listening on the right host.
- Review the deployment logs from startup.

## Typical Causes
- Missing `.env` values in production.
- Wrong host binding, such as using `127.0.0.1` instead of `0.0.0.0`.
- Build artifacts not copied correctly.
- Incorrect backend URL in the frontend.
- Platform-specific timeouts or resource limits.

## Investigation Steps
- Read the first error in the startup logs.
- Verify the app boots on the deployed machine.
- Compare local and production environment settings.
- Test the deployed endpoint with a simple request.
- Confirm the reverse proxy or platform routing is correct.

## Fixes That Often Help
- Set the correct environment variables in the hosting dashboard.
- Update the startup command to match the project structure.
- Bind the server to `0.0.0.0` when required.
- Rebuild the project after configuration changes.
- Redeploy after clearing stale artifacts.

## Example Incident Notes
- A release succeeded locally but failed on the host.
- The issue was a missing environment variable in production.
- Adding the variable and redeploying restored the service.

## Useful Logs
- Application startup logs.
- Platform deployment logs.
- Reverse proxy error logs.
- Environment configuration output.

## Summary
- Deployment issues are usually configuration or startup problems.
- The fastest path is to compare local behavior with production logs.