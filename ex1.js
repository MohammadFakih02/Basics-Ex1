var n = prompt("enter number of rows, output will be shown in console");
var i;
for(i=1;i<=n;i++){
    console.log(" ".repeat(n-i)+"* ".repeat(i));
}
for(i=n-1;i>0;i--){
    console.log(" ".repeat(n-i)+"* ".repeat(i));
}