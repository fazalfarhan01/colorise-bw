now="$(date +%B) $(date +%d) $(date +%Y) $(date +%T)"
commit_message="Adding Files on $now"
git add .
git commit -m "$commit_message"
git pull origin master
git push -u origin master
