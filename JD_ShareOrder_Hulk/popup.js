var kittenGenerator = {
  GetItem:function(){
    var item=null
    chrome.windows.getCurrent(function(window){
      chrome.tabs.getSelected(window.id,function(tab){
        url=tab.url.split('/')[3]
        item=url.substr(0,url.indexOf('.'))
        url='http://www.kjt.name/getRelByItem/'+item
        isw.requestKittens(url)
      })
    })
    return item
  }

};

var isw={
  requestKittens: function(url) {
    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    req.onload = this.showPhotos_.bind(this);
    req.send(null);
  },

  showPhotos_: function (e) {
    var kittens = e.target.responseXML.querySelectorAll('task');
    var urls=new Array()
    for (var i = 0; i < kittens.length; i++) {
      imgsrc=this.constructKittenURL_(kittens[i]);
      urls[i]=imgsrc
    }
    chrome.windows.create({
      'url':urls
    })
  },

  constructKittenURL_: function (photo) {
    return photo.getAttribute("href")
  }
}

chrome.browserAction.onClicked.addListener(function(){
  kittenGenerator.GetItem()
})