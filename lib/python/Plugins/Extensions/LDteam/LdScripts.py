from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from Components.ActionMap import ActionMap
from Components.config import config, ConfigText, configfile
from Components.Sources.List import List
from Components.Label import Label
from Components.PluginComponent import plugins
from Tools.Directories import resolveFilename, SCOPE_CURRENT_SKIN, SCOPE_SKIN_IMAGE, fileExists, pathExists, createDir
from Tools.LoadPixmap import LoadPixmap
from Plugins.Plugin import PluginDescriptor
from os import system, listdir, chdir, getcwd, remove as os_remove
from enigma import eDVBDB

class LDScripts(Screen):
	skin = """
	<screen name="LDSettings" position="center,center" size="800,560" title="OpenLD - Run Scripts">
		<widget source="list" render="Listbox" position="10,10" size="780,430" scrollbarMode="showOnDemand" >
			<convert type="StringList" />
		</widget>
		<widget name="statuslab" position="10,510" size="780,80" font="Regular;16" valign="center" noWrap="1" backgroundColor="#333f3f3f" foregroundColor="#FFC000" shadowOffset="-2,-2" shadowColor="black" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LDteam/images/buttons/red.png" position="350,460" size="140,40" alphatest="on" />
		<widget name="key_red" position="350,460" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
	</screen>"""
	
	def __init__(self, session):
		Screen.__init__(self, session)
		
		self["statuslab"] = Label("N/A")
		self["key_red"] = Label("Iniciar")
		self.mlist = []
		self.populateSL()
		self["list"] = List(self.mlist)
		self["list"].onSelectionChanged.append(self.schanged)
		
		self["actions"] = ActionMap(["WizardActions", "ColorActions"],
		{
			"ok": self.myGo,
			"back": self.close,
			"red": self.myGo
		})
		self.onLayoutFinish.append(self.refr_sel)
		
	def refr_sel(self):
		self["list"].index = 1
		self["list"].index = 0
		
	def populateSL(self):
		myscripts = listdir("/usr/lib/enigma2/python/Plugins/Extensions/LDteam/scripts")
		for fil in myscripts:
			if fil.find('.sh') != -1:
				fil2 = fil[:-3]
				desc = "N/A"
				f = open("/usr/lib/enigma2/python/Plugins/Extensions/LDteam/scripts/" + fil,'r')
				for line in f.readlines():
					if line.find('#DESCRIPTION=') != -1:
						line = line.strip()
						desc = line[13:]
				f.close()
				res = (fil2, desc)
				self.mlist.append(res)			

	def schanged(self):
		mysel = self["list"].getCurrent()
		if mysel:
			mytext = " " + mysel[1]
			self["statuslab"].setText(mytext)

			
	def myGo(self):
		mysel = self["list"].getCurrent()
		if mysel:
			mysel = mysel[0]
			mysel2 = "/usr/lib/enigma2/python/Plugins/Extensions/LDteam/scripts/" + mysel + ".sh"
			mytitle = "LD Team E2 Scripts: " + mysel
			self.session.open(Console, title=mytitle, cmdlist=[mysel2])