var http = require('http');
var content = function(req,res) {
    res.end("Hello, World (on K8S) version 3.0!"+ "\n");
    res.writeHead(200);
}

var my_server = http.createServer(content);
my_server.listen(9000);