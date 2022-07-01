function formValidation()
{
var name = document.registration.name;
var fname = document.registration.fname;
var uadd = document.registration.address;
var ucountry = document.registration.country;
var uemail = document.registration.email;
var umsex = document.registration.msex;
var ufsex = document.registration.fsex; 
if(name_validation(name))
{
if(name_validation(fname))
{ 
if(countryselect(ucountry))
{
}
} 
}
return false;
}

function name_validation(uid)
{
var uid_len = uid.value.length;
if (uid_len == 0 || uid_len >= my || uid_len < mx)
{
alert("Name should not be empty / length be between 5 to 12 ");
uid.focus();
return false;
}
return true;
}
function countryselect(ucountry)
{
if(ucountry.value == "Default")
{
alert('Select your country from the list');
ucountry.focus();
return false;
}
else
{
return true;
}
}