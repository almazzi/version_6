/**
 * Created with PyCharm.
 * User: User
 * Date: 11.09.14
 * Time: 0:01
 * To change this template use File | Settings | File Templates.
 */

var httpRequest;
if(window.XMLHttpRequest){
    httpRequest= new XMLHttpRequest();
}
else if(window.ActiveXObject){
    httpRequest=new ActiveXObject("Microsoft.XMLHTTP");
}
