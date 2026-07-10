# Authentication Troubleshooting Guide

## Common Symptoms
- Users receive 401 Unauthorized when calling protected endpoints.
- Login works in development but fails in staging.
- Tokens are accepted by one service but rejected by another.
- Session cookies are missing in the browser.
- Requests succeed locally but fail after deployment.

## What to Check First
- Confirm the token or session has not expired.
- Verify the client is sending the `Authorization` header correctly.
- Check whether the backend expects `Bearer <token>` format.
- Make sure the browser is allowed to send cookies.
- Compare local and deployed environment variables.

## Typical Causes
- Wrong secret key or mismatched signing key.
- Clock drift between machines causing token validation issues.
- Missing CORS configuration for authenticated requests.
- Incorrect cookie settings such as `HttpOnly`, `Secure`, or `SameSite`.
- Disabled or misconfigured identity provider settings.

## Investigation Steps
- Reproduce the issue with a simple API client.
- Inspect request headers in browser dev tools.
- Check backend logs for authentication errors.
- Decode the token to confirm the expected claims are present.
- Verify the user record still exists in the database.

## Fixes That Often Help
- Regenerate the token using the correct signing secret.
- Align environment variables across all environments.
- Update cookie settings for HTTPS deployment.
- Ensure the frontend sends credentials when required.
- Clear stale browser cookies and test again.

## Example Incident Notes
- After a deploy, users reported repeated login failures.
- The root cause was a changed secret in production.
- Updating the secret and reissuing tokens resolved the issue.
- A follow-up check was added to prevent future mismatches.

## Useful Logs
- Authentication failures from the API gateway.
- Token validation errors in backend logs.
- Browser console messages about blocked cookies.
- Identity provider rejection messages.

## Summary
- Focus on token format, secret consistency, and cookie behavior.
- Most issues are configuration-related rather than code bugs.