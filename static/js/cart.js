var updateBtns= document.getElementsByClassName('update-cart')
for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId= this.dataset.product
        var action= this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('user', user )
        if (user == 'AnonymousUser' ){
            console.log("no user logged in")
        }else{
            updateuserorder(productId, action)
        }

    })
}
//his function sends a POST request to the specified URL 
//with JSON data containing the productId and action parameters. 
function  updateuserorder(productId, action){
    console.log("user logged in , sending data.. ")
    var url='update_item'
    fetch(url, {    // fetch is a  modern browser API used to make HTTP requests.
        method:'POST',
        headers:{
            'content-type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action}), // the body is th data being sent to the backend 

    })
    .then((respose)=>{
        return respose.json()
    })
    .then((data)=>{
        console.log('data:',data)
    })
}
