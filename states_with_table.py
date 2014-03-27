#Open states.txt and use the information to generate an HTML drop-down menu 
#First create a list from a state csv
with open("states.csv", "r") as states_file:
	states = states_file.read().split('\n')

states_file.close()
#Second create a new list containing the information about the states
with open("states_info.csv", "r") as states_info_file:
	states_info = states_info_file.read().replace('"', "").split('\n')
states_info_file.close()

#Save the HTML as states.html instead of printing it to screen.
with open("states_info.html", "w") as state_info_file:
#Creating the drop down menu
	state_info_file.write('<select name="states">')	
	for index, state in enumerate(states):
		states[index] = states[index].split(",")
		state_info_file.write( "\n\t<option value='{0}'>{1}</option>".format(states[index][0], states[index][1]));    
	state_info_file.write("\n</select>")
#Creating the table	
	state_info_file.write('\n<table border ="1">')
	for index, state_info in enumerate(states_info):
		states_info[index] = states_info[index].split(",")
		state_info_file.write("""\n<div id="{0}">""".format(states_info[index][1]));
		state_info_file.write("""\n<tr>\n<td colspan="2">{0}</td>\n</tr>""".format(states_info[index][1]));
		state_info_file.write("""\n<tr>\n<td>Rank: {0}</td>\n<td>Percent: {1}</td>\n</tr>""".format(states_info[index][0], states_info[index][4]));
		state_info_file.write("""\n<tr>\n<td>US House Members: {0}</td>\n<td>Population: {1}</td>\n</tr>""".format(states_info[index][3], states_info[index][2]));
		state_info_file.write("""\n</div>""")
	state_info_file.write('\n</table>')
	
import webbrowser

webbrowser.open_new_tab("file:///Users/SoniaHinson/Documents/PythonClass/Shannon_Py_Ladies/Class/states_info.html")
 
