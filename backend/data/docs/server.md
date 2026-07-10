# Server Troubleshooting Guide

## Common Symptoms
- The server does not start.
- Requests return 500 Internal Server Error.
- The API is slow under light load.
- Certain routes work while others fail.
- The application crashes after receiving a request.

## What to Check First
- Read the startup logs carefully.
- Confirm the correct Python environment is active.
- Verify required packages are installed.
- Check whether the app is running on the expected port.
- Make sure imports do not fail during startup.

## Typical Causes
- Missing dependency installation.
- A syntax or import error in the server code.
- Unhandled exceptions inside a route.
- Incorrect environment variables.
- Port conflicts with another process.

## Investigation Steps
- Start the server from the terminal and capture the first error.
- Send a simple request to the root endpoint.
- Inspect stack traces for the exact failing line.
- Compare local settings with the deployment settings.
- Verify that the server can read files and environment variables.

## Fixes That Often Help
- Install missing dependencies.
- Correct the broken import or configuration value.
- Add basic error handling around fragile code paths.
- Change to an unused port if another process is blocking it.
- Restart the server after configuration changes.

## Example Incident Notes
- A server crash happened after a new import was added.
- The imported package was not installed in the environment.
- Installing the package resolved the startup failure.

## Useful Logs
- Python tracebacks.
- Uvicorn startup messages.
- Route-level exception logs.
- Environment variable output.

## Summary
- Server issues are usually visible in the first startup error or traceback.
- Fix the root error before tuning anything else.