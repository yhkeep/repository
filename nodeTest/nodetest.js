/*
var http=require('http');
http.createServer(function (request,response){
    response.writeHead(200,{'Content-Type':'text/plain'})
    response.end("hello,world\n");
    }).listen(8887);

console.log('Server runing at http://127.0.0.1:8887');
*/
//node.js返回重复的第一个
/*
const removeConsecutiveDuplicates = s => {
    // console.log(s.substring(s.length-1));
    let st = s.split(" ");
    let string = "";
    for (let i = 0; i <st.length-1 ; i++) {
        if(st[i] !== st[i+1]){
            string += st[i] + " ";
        }if (st[i]===st[i+1]){
            continue;
        }
    }
    //上面将st转为数组，所以可以直接通过数组索引取得最后一个值
    string = string+st[st.length-1];
    return string;
};
removeConsecutiveDuplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta gamma gamma ');
*/

