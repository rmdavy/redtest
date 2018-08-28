#! /usr/bin/python
import os,sys,subprocess

def main(argv):

	
	print """
    ______           .____________                     _____  
\______   \ ____   __| _/   _____/ ____ _____ ________/ ____\ 
 |       _// __ \ / __ |\_____  \ /    \\__  \\_  __ \   __\  
 |    |   \  ___// /_/ |/        \   |  \/ __ \|  | \/|  |    
 |____|_  /\___  >____ /_______  /___|  (____  /__|   |__|    
        \/     \/     \/       \/     \/     \/                      
                                  redsnarf.ff0000@gmail.com
                                                  @redsnarf
"""

	print "[+]RedSnarf Quick and Dirty Installer (Tested on Kali Linux)"
	print "[+]Starting Installation Process"
	os.system("apt-get update")
	os.system("apt-get install python-ipy python2.7-dev libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev --fix-missing")
	os.system("pip install netaddr")
	os.system("pip install termcolor")
	os.system("pip install python-ldap")
	os.system("pip install pysmb")
	os.system("pip install docopt")
	os.system("pip install pyuserinput")
	os.system("pip install wget")
	os.system("pip install pywinrm")
	
	if not os.path.isfile('/opt/python-libnmap/setup.py'):
		os.system("git clone https://github.com/savon-noir/python-libnmap.git /opt/python-libnmap")
		os.chdir("/opt/python-libnmap")
		os.system("python setup.py install")
		
	if not os.path.isfile('/opt/creddump7/pwdump.py'):
		os.system("git clone https://github.com/Neohapsis/creddump7 /opt/creddump7")

	if not os.path.isfile('/usr/local/bin/secretsdump.py'):
		if not os.path.isfile('/tmp/impacket/setup.py'):
			os.system("git clone https://github.com/CoreSecurity/impacket.git /tmp/impacket")
		
		os.system("chmod 777 /tmp/impacket/setup.py")
		os.chdir("/tmp/impacket")
		os.system("python setup.py install")
	
	if not os.path.isfile('/opt/JohnTheRipper'):
		os.system("apt-get install libssl-dev")
		os.system("git clone https://github.com/magnumripper/JohnTheRipper.git /opt/JohnTheRipper")
		os.chdir("/opt/JohnTheRipper/src")
		os.system("./configure CFLAGS=\"-g -O2 -mno-avx2\"")
		os.system("make clean && make -s")
	
	os.chdir("/opt/redtest")
	os.system("chmod 777 /opt/redtest/redsnarf.py")
	os.system("python /opt/redtest/redsnarf.py --auto_complete install")
		
	print "[+]Bye"

if __name__ == "__main__":
   main(sys.argv[1:])
