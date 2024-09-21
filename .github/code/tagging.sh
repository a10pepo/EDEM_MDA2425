#!/bin/bash

# Assign command line arguments to variables
LABEL=$1
REVIEWER=$2

# Fetch PR IDs with the specified label and store them in PR_IDS
PR_IDS=$(gh pr list --label "$LABEL" --json number --jq '.[].number')

while IFS= read -r PR_ID; do 
    gh pr edit "$PR_ID" --add-assignee $REVIEWER --add-reviewer $REVIEWER 
done <<< "$PR_IDS"
