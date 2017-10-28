//document.body.style.border = "20px solid red";
//<div style="background: red;color: white;width: 100%;text-align: center;font-size: 45px;padding: 2px;"><strong>ACHTUNG DIESES VIDEO IST SCH**SSE</strong></div>
var link = window.location.href
var url = new URL(link);
var c = url.searchParams.get("v");

var xhr = new XMLHttpRequest();

xhr.open("GET","http://localhost:5000/id/"+c, true);
xhr.onreadystatechange = function(){
  if(xhr.readyState == 4){
    var response = JSON.parse(xhr.responseText)
    if(response.clickbait){
      var pagemanager = document.getElementById("page-manager")
      var ytdwatch = pagemanager.getElementsByTagName("ytd-watch")[0]
      var top = document.getElementById("top")

      var warning = document.createElement("div")
      warning.style = "background: red;color: white;width: 100%;text-align: center;font-size: 45px;padding: 2px; "
      var text = document.createTextNode("DIESES VIDEO IST CLICKBAIT")

      var strong = document.createElement("strong")
      strong.appendChild(text)
      warning.appendChild(strong)

      ytdwatch.insertBefore(warning, top)
    }
  }
}
xhr.send();
