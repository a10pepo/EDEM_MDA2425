#!/bin/bash

touch /var/log/cron.log
chmod 0644 /var/log/cron.log

# Write the cron job dynamically using runtime environment variables
echo "*/1 * * * * root PROJECT_ID=${PROJECT_ID} POSTGRES_IP=${POSTGRES_IP} HOST_IP=${HOST_IP} GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS} /bin/bash /app/cron_run.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/cron_job

# Set correct permissions
chmod 0644 /etc/cron.d/cron_job

# Print environment variables for debugging
echo "Environment Variables:"
echo "GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}"
echo "PROJECT_ID=${PROJECT_ID}"
echo "POSTGRES_IP=${POSTGRES_IP}"
echo "HOST_IP=${HOST_IP}"

# Start cron
echo "Starting cron..."
cron

# Keep the container alive by tailing the log file
tail -f /var/log/cron.log
