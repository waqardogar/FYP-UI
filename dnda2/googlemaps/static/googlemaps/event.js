function live_p(){
    live_preview = document.getElementById('flexSwitchCheckDefault').checked
    if(live_preview){
        document.getElementById('video-screen').style = 'background-color: rgb(114, 100, 100);position: absolute;bottom: 0;right: 0;width: 550px;height: 300px;display: flex;align-items: center;justify-content: center;' 
    }
    else{
        document.getElementById('video-screen').style.display = 'none' 
    }
}