var contactsLength = document.querySelector(".cf-rpts-container").childNodes.length;
var propertyOwnerSlot;
var propertyOwnerInfo = [];

function getPropertyOwnerInfo(){

  let propertyOwnerInfoLength = document.querySelector(".cf-rpts-container").childNodes[3].childNodes[0].childNodes[0].childNodes[1].childNodes.length;

  for(let i = 0; i < propertyOwnerInfoLength; i++){

    propertyOwnerInfo.push(document.querySelector(".cf-rpts-container").childNodes[propertyOwnerSlot].childNodes[0].childNodes[0].childNodes[1].childNodes[i].innerText);

  }

  console.log(propertyOwnerInfo);

}
function scrapeNames(){

  for(let i = 0; i < contactsLength; i++){

    console.log(document.querySelector(".cf-rpts-container").childNodes[i].childNodes[0].childNodes[0].childNodes[1].childNodes[0].innerText);
    
    if(document.querySelector(".cf-rpts-container").childNodes[i].childNodes[0].childNodes[0].childNodes[1].childNodes[0].innerText == "Property Owner"){

      propertyOwnerSlot = i;
      getPropertyOwnerInfo();

    }

  }

}
scrapeNames();

/*------------------------------------------------------------------------------------------------------------------------------------------------------*/

var propertyCount = document.querySelector(".photo-cards").childNodes.length;
var propertyAddresses = [];
var propertyLinks = [];

function getPropertyAddresses(){

  for(let i = 0; i < propertyCount; i++){

    if(document.querySelector(".photo-cards").childNodes[i].childNodes[0].id != "nav-ad-container"){

      propertyAddresses.push(document.querySelector(".photo-cards").childNodes[i].childNodes[1].childNodes[0].childNodes[0].innerText);
      propertyLinks.push(document.querySelector(".photo-cards").childNodes[i].childNodes[1].childNodes[0].href);

    }

  }


  for(let i = 0; i < propertyAddresses.length; i++){
  console.log(propertyAddresses[i]+" - "+propertyLinks[i]);
  }


}
getPropertyAddresses();

/*------------------------------------------------------------------------------------------------------------------------------------------------------*/

var XMLurls = [];

function getXMLurl(){

  for(let i = 0; i < propertyAddresses.length; i++){

    let comma1 = propertyAddresses[i].indexOf(","); 
    let comma2 = propertyAddresses[i].indexOf(",", comma1+1);
    let street = (propertyAddresses[i].slice(0, comma1)).replace(/ /g, "+");
    let city = propertyAddresses[i].slice(comma1+2, comma2);
    let state = propertyAddresses[i].slice(comma2+2, propertyAddresses[i].length);
    let cityState = (city + " " + state).replace(/ /g, "+");
    let XMLurl = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1h8p3ss49hn_44w9p&address="+street+"&citystatezip="+cityState+"&rentzestimate=true";

    XMLurls.push(XMLurl);

  }

}
getXMLurl();

/*------------------------------------------------------------------------------------------------------------------------------------------------------*/

var zpidToCells = "";
var zpidToCells = "";
var cityToCells = "";
var stateToCells = "";
var zestimateToCells = "";
var rentzestimateToCells = "";
var zpidToCells = "";
var writeToCellsScript = "";
var extraVariables = "";

function getXMLToCellsScript(){

  zpidToCells += 'sheet.getRange("A2:A'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      zpidToCells += ", ";

    }

    zpidToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/address[1]/street[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  zpidToCells += ']);';
//

cityToCells += 'sheet.getRange("B2:B'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      cityToCells += ", ";

    }

    cityToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/address[1]/city[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  cityToCells += ']);';
//

stateToCells += 'sheet.getRange("C2:C'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      stateToCells += ", ";

    }

    stateToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/address[1]/state[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  stateToCells += ']);';
//

  zestimateToCells += 'sheet.getRange("D2:D'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      zestimateToCells += ", ";

    }

    zestimateToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/zestimate[1]/amount[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  zestimateToCells += ']);';
//

rentzestimateToCells += 'sheet.getRange("E2:E'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      rentzestimateToCells += ", ";

    }

    rentzestimateToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/rentzestimate[1]/amount[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  rentzestimateToCells += ']);';
//

zpidToCells += 'sheet.getRange("F2:F'+(XMLurls.length+1)+'").setValues([';
  
  for(let i = 0; i < XMLurls.length; i++){

    if(i != 0){

      zpidToCells += ", ";

    }

    zpidToCells += '['+"'"+'='+'IFNA('+'IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/zpid[1]'+'"'+')'+', "Unavailable")'+"'"+']';

  }

  zpidToCells += ']);';
//

extraVariables += "count="+XMLurls.length+";";

//

  //console.log(zpidToCells);
  //console.log(cityToCells);
  //console.log(stateToCells);
  //console.log(zestimateToCells);
  //console.log(rentzestimateToCells);
  //console.log(zpidToCells);

  writeToCellsScript = zpidToCells+cityToCells+stateToCells+zestimateToCells+rentzestimateToCells+zpidToCells+extraVariables;

  let exportdata = document.createElement("a");
  exportdata.href = "data:text/js;filename=Test;charset=utf-8," + writeToCellsScript;	
  exportdata.target = "_blank";
  exportdata.download = "Test.txt";
  document.body.appendChild(exportdata);
  exportdata.click();

}
getXMLToCellsScript();

/*------------------------------------------------------------------------------------------------------------------------------------------------------*/

document.querySelector(".cf-rpts-container").childNodes[3].childNodes[0].childNodes[0].childNodes[1].childNodes[0].innerText

document.querySelector(".photo-cards").childNodes[0].childNodes[1].childNodes[0].childNodes[0].innerText

https://www.zillow.com/homes/fsbo/mmm_pt/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-93.52272060263385,%22east%22:-93.15879848349323,%22south%22:30.647578625528663,%22north%22:31.099019242213984},%22isMapVisible%22:true,%22mapZoom%22:11,%22filterState%22:{%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false},%22isMakeMeMove%22:{%22value%22:false},%22isForSaleByAgent%22:{%22value%22:false},%22isForSaleForeclosure%22:{%22value%22:false},%22isAuction%22:{%22value%22:false},%22isNewConstruction%22:{%22value%22:false},%22isComingSoon%22:{%22value%22:false}},%22isListVisible%22:true}
https://www.zillow.com/homedetails/1175-Allison-Dr-Deridder-LA-70634/106017864_zpid/

1175 Allison Dr, Deridder, LA

properties1 = []; 
for(let i = 0; i < propertyAddresses.length; i++){
  properties1.push('['+"'"+propertyAddresses[i]+"'"+']');
  }

sheet.getRange("A1:A2").setValues([["Test1"],["Test2"]]);

http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1h8p3ss49hn_44w9p&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA&rentzestimate=true

=IMPORTXML("http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1h8p3ss49hn_44w9p&address=345+Allan+Ensminger+Rd&citystatezip=Deridder+LA&rentzestimate=true", "//response[1]/results[1]/result[1]/address[1]/street[1]")

"//response[1]/results[1]/result[1]/address[1]/street[1]"
"//response[1]/results[1]/result[1]/address[1]/city[1]"
"//response[1]/results[1]/result[1]/address[1]/state[1]"
"//response[1]/results[1]/result[1]/zestimate[1]/amount[1]"
"//response[1]/results[1]/result[1]/rentzestimate[1]/amount[1]"
"//response[1]/results[1]/result[1]/zpid[1]"

zestimateToCells += '['+"'"+'=IMPORTXML('+'"'+XMLurls[i]+'"'+', '+'"'+'//response[1]/results[1]/result[1]/zestimate[1]/amount[1]'+'"'+')'+"'"+']';

function drawBorders() {

let ss = SpreadsheetApp.getActiveSpreadsheet();
let sheet = ss.getSheets()[0];

let column;

 for(let x = 0; x < 2; x++){

 if(x == 0){
  column = "A";
 }
 else if(x == 1){
  column = "B";
 }
 else if(x == 2){
  column = "C";
 }
  
  for(let i = 1; i < 250; i++){

    let cell = sheet.getRange('"'+column+i+'"'); 

    if (cell.getValue() !== "") {
      cell.setBorder(true, true, true, true, true, true);
    }
    else {
      cell.setBorder(false, false, false, false, false, false);
    }

  }
 }
}

cell = sheet.getRange('"'+column+i+":"+column+i+'"'); 
