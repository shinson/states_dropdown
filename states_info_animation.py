#Turn CVS into a list of strings
with open("states.csv", "r") as states_file:
	states = states_file.read().split('\n')

states_file.close()
#Turn CVS with data on states into a list of strings
with open("states_info.csv", "r") as states_info_file:
	states_info = states_info_file.read().replace('"', "").split('\n')
states_info_file.close()
# Write New HTML File
with open("states_info2.html", "w") as state_info_file:
#Write the script section of the html doc incorporating a jquery api for animation effects
#The Jquery will only show which state was selected in the dropdown menu
	state_info_file.write('\n<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>')
	state_info_file.write('\n<script>')
	state_info_file.write("""$(document).ready(function () {\n$(".group").hide();\n$("#alabama").show();\n$("select").change(function () {\n\t$('.group').hide();\n\t$('#' + $(this).val()).show();});\n});""")
	state_info_file.write('\n</script>')
#Begin the Dropdown
#Change the value to be all lowercase and to have no spaces so that the Jquery would work
	state_info_file.write('<select name="states">')
	for index, state in enumerate(states):
		states[index] = states[index].split(",")
		state_info_file.write( "\n\t<option value='{0}'>{1}</option>".format(states[index][1].lower().replace(" ", "_"),states[index][1]));    
	state_info_file.write("\n</select>")
#Begin the Table
#Added the class gorup, and added the id="state name" all lower case and without spaces to match the values of the drop down menu
#Included Palau at the end to match the dropdown		
	state_info_file.write('\n<table border ="1">')
	for index, state_info in enumerate(states_info):
		states_info[index] = states_info[index].split(",")
		state_info_file.write("""\n<tr id="{0}" class="group">\n\t<td colspan="2">{1}</td>""".format(states_info[index][1].lower().replace(" ", "_"), states_info[index][1]));
		state_info_file.write("""\n\t<td>Rank: {0}</td>\n\t<td>Percent: {1}</td>""".format(states_info[index][0], states_info[index][4]));
		state_info_file.write("""\n\t<td>US House Members: {0}</td>\n\t<td>Population: {1}</td>\n</tr>""".format(states_info[index][3], states_info[index][2]));
	state_info_file.write('\n<tr id="palau" class="group">\n\t<td colspan="2">Palau</td>\n\t<td>No information! Sorry!</td>\n</tr>')	
	state_info_file.write('\n</table>')
	
	
import webbrowser
webbrowser.open_new_tab('file:///Users/SoniaHinson/Documents/PythonClass/Shannon_Py_Ladies/Class/states_info2.html')
