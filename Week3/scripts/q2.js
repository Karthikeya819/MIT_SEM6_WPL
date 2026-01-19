function update_time(){
    var date = new Date();
    let hours = date.getHours();
    let hours_form = String(hours % 12).padStart(2, '0');
    let mins = String(date.getMinutes()).padStart(2, '0');
    let secs = String(date.getSeconds()).padStart(2, '0');
    let apm = (date.getHours() > 12)?'PM':'AM';
    document.getElementById('time').innerHTML = `${hours_form} : ${mins} : ${secs} ${apm}`;
    
    let greet = '';
    if(hours < 12){
        greet = "Good Morning";
    }else if(hours < 17){
        greet = "Good Afternoon";
    }else{
        greet = "Good Evening";
    }
    document.getElementById('span-greet').innerHTML = greet;
}

setInterval(update_time, 500);