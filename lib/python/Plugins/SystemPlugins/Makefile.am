installdir = $(pkglibdir)/python/Plugins/SystemPlugins

SUBDIRS = PositionerSetup Satfinder SoftwareManager \
	VideoTune Hotplug CableScan NetDrive \
	DefaultServicesScanner CommonInterfaceAssignment \
	VideoEnhancement WirelessLan NetworkWizard VideoClippingSetup \
	SatelliteEquipmentControl DiseqcTester HdmiCEC FastScan LCNScanner

if HAVE_LIBVUGLES2
SUBDIRS += AnimationSetup
endif

if HAVE_OSDANIMATION
SUBDIRS += AnimationSetup
endif

if WETEK
SUBDIRS += WetekFRQ WetekSync WetekAudio
endif

if DREAMBOX
SUBDIRS += FrontprocessorUpgrade NFIFlash
endif

install_PYTHON = __init__.py
