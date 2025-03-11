# create an script that receives one argument that is personal or nw

if [ $# -ne 1 ]; then
    echo "Usage: $0 <personal|nw>"
    exit 1
fi

if [ "$1" = "personal" ]; then
    echo "This is a personal account"
    cp personal/personal/config  ~/.aws/config
    cp personal/personal/credentials  ~/.aws/credentials
    
elif [ "$1" = "nw" ]; then
    echo "This is a nw account"
    cp personal/nw/config  ~/.aws/config
    cp personal/nw/credentials  ~/.aws/credentials
else
    echo "Invalid argument"
    exit 1
fi

#mv ~/.aws/credentials.bak ~/.aws/credentials
#mv ~/.aws/config.bak ~/.aws/config