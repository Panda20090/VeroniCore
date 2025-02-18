#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
BACKUP_DIR="/path/to/backup/directory"
DATABASE_NAME="VeroniCore_db"
DATABASE_USER="db_user"
DATABASE_HOST="localhost"
DATABASE_PORT="5432"
TIMESTAMP=$(date +"%F")
BACKUP_FILE="$BACKUP_DIR/VeroniCore_backup_$TIMESTAMP.sql"
LOG_FILE="$BACKUP_DIR/backup_$TIMESTAMP.log"
FILES_TO_BACKUP="/var/www/VeroniCore"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Start logging
exec &> >(tee -a "$LOG_FILE")

echo "Starting backup process..."

# Backup the database
echo "Backing up the database..."
pg_dump -h $DATABASE_HOST -p $DATABASE_PORT -U $DATABASE_USER $DATABASE_NAME > $BACKUP_FILE

# Compress the backup
echo "Compressing the backup file..."
gzip $BACKUP_FILE

# Backup important files
echo "Backing up important files..."
tar -czf "$BACKUP_DIR/VeroniCore_files_backup_$TIMESTAMP.tar.gz" $FILES_TO_BACKUP

echo "Backup process completed successfully!"

# Optional: Delete old backups (e.g., older than 7 days)
echo "Cleaning up old backups..."
find $BACKUP_DIR -type f -mtime +7 -name "*.gz" -exec rm {} \;

echo "Old backups cleaned up successfully!"
