
# added by Anaconda2 5.0.0 installer
export PATH="/Users/Martin/anaconda2/bin:$PATH"

alias aqua="open -a Aquamacs"

#-------------------------------------
# Question 7
#------------------------------------

export ams209="/Users/Martin/Documents/College/UCSC/Fall-2017/AMS-209"
export ams209git="/Users/Martin/Documents/College/UCSC/Fall-2017/AMS-209/ams209git"

alias lsc="ls -G"


#------------------------------------------
# Question 8
#------------------------------------------
function cd_up(){
    cd $(printf "%0.0s../" $(seq 1 $1));
}
alias 'cd..'='cd_up'

function pwd_up(){
    current_directory=$(pwd);
    cd $(printf "%0.0s../" $(seq 1 $1)) && pwd && cd $current_directory;
}
alias 'pwd..'='pwd_up'

