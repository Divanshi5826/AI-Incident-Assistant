# Redis Troubleshooting Guide

## Common Symptoms
- Cache reads return misses for expected keys.
- Jobs or queued tasks are delayed.
- The service cannot connect to Redis.
- Memory usage grows unexpectedly.
- Data disappears after a restart.

## What to Check First
- Verify the Redis host and port.
- Confirm authentication settings if Redis requires a password.
- Check whether the application is pointing at the correct database index.
- Inspect key expiry settings.
- Make sure the Redis service is actually running.

## Typical Causes
- Wrong connection string.
- Keys expiring too quickly.
- Cache invalidation clearing data too aggressively.
- Memory limits causing evictions.
- Local development using a different Redis instance than production.

## Investigation Steps
- Test the connection with a small client command.
- List recent keys to confirm the expected data exists.
- Review logs for connection or timeout errors.
- Check whether the application writes and reads the same key format.
- Look at eviction statistics if memory pressure is suspected.

## Fixes That Often Help
- Correct the host, password, or database number.
- Increase expiration time where appropriate.
- Align key naming across all services.
- Raise memory limits only after understanding the usage pattern.
- Restart the app after changing Redis settings.

## Example Incident Notes
- The app reported missing cached user sessions.
- Investigation showed the key prefix had changed after deployment.
- Restoring the old prefix fixed the mismatch.

## Useful Logs
- Redis connection failures.
- Cache miss counts.
- Eviction messages.
- Timeout errors from the application.

## Summary
- Redis problems are often caused by connection settings, key mismatches, or short expirations.
- Check configuration before assuming the cache is broken.