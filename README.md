<h1> Webkiosk_Attendance_Bot</h1>
<p>Running the script automatically logs in to the student's account on the JIIT Webkiosk and fetches their attendance. This is done using selenium. Currently it is only able to show the subjects I have registered for in this semester but the future versions will be more universal
</p>
<p> To run the bot please follow the following steps</p>
<ul>
<li>Download the script and open it in a text editor.</li>
<li>Type your details including JIIT enrollment number, Date of Birth and Password into the variables given.</li>
<li>For the password variable I would suggest creating an environment variable in your system with the password for your webkiosk login for extra safety but hard coding the password in the script works too</li>
<li>Run the script.</li>
</ul>
<p>With the current version of this script it may not show all subjects you have been registered for as I had hardcoded the fields of the html id tags of the subjects I have registered for but feel free to tinker around and optimise the code to work better with your subjects.</p>
