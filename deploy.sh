micro_services_folder=`ls ./src`
for eachfile in $micro_services_folder
do    
    pip freeze > ./src/"$eachfile"/requirements.txt
    
done

# sam build
# sam deploy
