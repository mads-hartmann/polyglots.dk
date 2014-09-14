$(document).ready(function() {

    var url = "https://api.github.com/repos/mads379/polyglots.dk/contributors";

    $.getJSON(url, function(data, status) {
        var list = $("#contributors");
        $(data).each(function(index, element){
            var li = $("<li></li>").attr("class", "thumbnail text-center col-md-2 col-sm-2 col-xs-2");
            var link = $("<a></a>").attr("href", element.html_url);
            var username = $("<p>").text(element.login);
            var image = $("<img>").attr("src", element.avatar_url).attr("class", "img-circle");
            list.append(li.append(link.append(image).append(username)))
        });
    });

});
