<?php
$data = "theCityCode=792&theUserID=68720c726895429f81868baba95f488f";
$curl = curl_init();
curl_setopt($curl,CURLOPT_URL,"http://www.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather");
curl_setopt($curl,CURLOPT_HEADER,0);
curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
curl_setopt($curl,CURLOPT_POST,1);
curl_setopt($curl,CURLOPT_POSTFIELDS,$data);
curl_setopt($curl,CURLOPT_HTTPHEADER,array(
	"application/x-www-form-urlencoded;charset=utf-8",
	"Content-length:".strlen($data)
	));
$output=curl_exec($curl);

//if(!curl_errno($curl)){
	echo $output;
//}else{
//	echo 'Curl errno:'.curl_error($curl);
//}

curl_close($curl);
//echo str_replace("百度"，"傻比",$output);

?>