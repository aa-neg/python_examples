import cx_Oracle
import sys
from logger import logger
from pprint import pprint

import datetime
from datetime import timedelta

class OracleLogger(object):
	def __init__(self, schema, ps, db):
		print "Spawning oracle logger"
		self.schema = schema
		self.ps = ps
		self.db = db
		self.connection = None
		self.connect()

	def connect(self):
		try:
			print "here are our schema ps and db"
			print self.schema
			print self.ps
			print self.db
			self.connection = cx_Oracle.connect(
					self.schema,
					self.ps,
					self.db
				)
			if (self.connection):
				logger.info("[Oracle Logger][connect] spawned connection to: " + str(self.schema))
			else:
				raise AssertionError("Connection object not found")
		except Exception, err:
			logger.info("[Oracle Logger][connect] failed to connect: " + str(err))

	def disconnect(self):
		try:
			self.connection.close()
		except Exception, err:
			logger.info("[Oracle Logger][disconnect] failed to disconnect: " + str(err))

	def executeQuery(self, query):
		try:
			if not self.connection:
				raise AssertionError("Connection object not found")
			else:
				cursor = self.connection.cursor()
				cursor.execute(query)
				self.connection.commit()
				logger.info("[Oracle Logger][execute query][Success]" + str(query))

		except Exception, err:
			logger.info("[Oracle Logger][executeQuery] " + str(err))

	def executeQueryBindVars(self, query, bindObject):
		try:
			if not self.connection:
				raise AssertionError("Connection object not found")
			else:
				cursor = self.connection.cursor()
				logger.info("Here is our bind object" + str(bindObject))
				cursor.execute(query, bindObject)
				self.connection.commit()
				logger.info("[Oracle Logger][execute query][Success]" + str(query))

		except Exception, err:
			logger.info("[Oracle Logger][executeQuery] " + str(err))


	# Formatts the SQL and returns the bind array to preserve ordering
	def insertSQLConstructor(self, insertDict):
		insertSQL = ""
		valueSQL = ""
		for key, value in insertDict.iteritems():
			insertSQL += key + ',\n'
			if ('DATE' in key) and (key is not 'LOG_DATE'):
				valueSQL += "to_date(:" + key + ", 'YYYY/MM/DD HH:MI:SS')" + ',\n'

				# Remove T for formatting.
				insertDict[key] = value.replace("T", " ")
			else:
				valueSQL += ":" + key + ',\n'

		insertSQL = insertSQL[:-2]
		valueSQL = valueSQL[:-2]

		return insertSQL, valueSQL

	def logSynapseConsumer(self, eventDict):
		# Note will always be inserting log date as sysdate.
		SQL = """
		insert into stage3_uf.uf_synapse_consumer_brjp_log@DPDB
		(
		"""
		insertSQL, valueSQL = self.insertSQLConstructor(eventDict)
		SQL += insertSQL + ")"
		SQL += "values ("
		SQL += valueSQL + ")"

		self.executeQueryBindVars(SQL, eventDict)




