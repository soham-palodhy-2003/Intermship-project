var player;
var video_list;
var recorded_video_list;
document.onreadystatechange = function (){
    if(document.readyState == 'interactive')
    player = document.getElementById('player')
    video_list = document.getElementById('video_list')
    recorded_video_list = document.getElementById('recorded_video_list')

     maintain_ratio()
}

function maintain_ratio() {
    var w = player.clientWidth
    var h = (w*9)/16
    console.log({w,h})
    player.height = h
    video_list.style.maxHeight = h + 'px'
    recorded_video_list.style.maxHeight = h + 'px'
}
window.onresize = maintain_ratio