<?php
require_once 'login.php';

//1&2. connect to DBMS, select DB
$conn=new mysqli($db_hostname,$db_username,$db_password,$db_database);

if ($conn->connect_error)
{
 echo "Failed to connect: " . $conn->connect_error;
}else{
echo "success" ;
}

//3. build SQL query
$company=$_POST['company_name'];
$query="SELECT price FROM ipo_char WHERE company = '$company' ";

//4. execute the query
$result=$conn->query($query);

//5. use the result, check whether we fetched any record from the search
if ($result->num_rows ==0){
 echo "<script type='text/javascript'>alert('Please check the company name again!');
   window.location.href='dashboard.php';</script>";
 exit();
}
?>