from subprocess import Popen, PIPE
from re import split
from sys import stdout
import sys
import time
import re
import os
import signal
import argparse
import psutil
import socket


def listAllSubscribers(markets):
	pass

def getProcList():
	proc_list = []
	for proc in psutil.process_iter():
		try:
			print "here is our proc"
			print proc
			print dir(proc)
			pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
			print pinfo
			print dir(pinfo)

		except:
			pass


if __name__ == "__main__":

	argparser = argparse.ArgumentParser(
		description="Command line interface to run multiple synapse consumers"
		)

	getProcList()



