# Database Troubleshooting Guide

## Common Symptoms
- Queries are slow during normal traffic.
- The application cannot connect to the database.
- New records are not appearing after writes.
- Migrations succeed locally but fail in production.
- The app shows intermittent timeout errors.

## What to Check First
- Confirm the database URL is correct.
- Verify the database service is running.
- Check whether the app has permission to connect.
- Look for connection pool exhaustion.
- Review recent schema changes.

## Typical Causes
- Incorrect host, port, username, or password.
- Missing tables or columns after a deployment.
- Too many open connections from the application.
- Locked rows or long-running transactions.
- SQLite file path issues in local development.

## Investigation Steps
- Test the connection from the server machine.
- Run the same query directly against the database.
- Inspect slow query logs if they are available.
- Check whether indexes exist on frequently filtered columns.
- Review migration history for skipped steps.

## Fixes That Often Help
- Correct the connection string and restart the app.
- Run the missing migration before retrying.
- Add or improve indexes for common lookups.
- Reduce transaction size if locks are occurring.
- Increase timeout values only after confirming the real issue.

## Example Incident Notes
- A deployment introduced a new table column.
- Old application code still expected the previous schema.
- The mismatch caused write failures in production.
- Applying the migration and redeploying fixed the issue.

## Useful Logs
- Database connection errors.
- Migration output.
- Timeout messages.
- SQL exceptions from the backend.

## Summary
- Most database incidents come from connection, schema, or performance issues.
- Always compare the database state with the application version.