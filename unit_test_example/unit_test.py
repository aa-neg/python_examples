import unittest
import os
import sys

class UFDataTest(unittest.TestCase):
	def test_integration(self):

		import updateTrackCondConfig
		import datetime

		test_conf = updateTrackCondConfig.marketsAndChangeInformation

		updateTimeStamp = datetime.datetime.utcnow()
		# Clean all the possible queues
		for market in test_conf:
			cleanDevQueues(test_conf[market]["request_queue"].replace('rqst', 'dev'))

		time.sleep(2)

		# Contains an array of lines read from the old config file
		os.chdir(orginalWD)
		# # Give 5.5 seconds for process to finish appending to queue (this will change once we move to thrift i think)
		time.sleep(10)

		if config["ab"] == "thing":
			sys.path.insert(0, '../somedir')

			from subscriberClass import SubscriberClass
			from publisherClass import PublisherClass
			from twisted.internet import reactor
			from pprint import pprint
			import threading
		# Starting publisher client to start reactor from publisher clients thread (same as in production as we don't have a subscriber)
			publisherClient = threading.Thread(target=publisher.startClassReactor)
			publisherClient.setDaemon(True)
			publisherClient.start()

			self.assertTrue(publisherClient.isAlive())

			# Connecting our subscriber to the thread
			subscribeEvent = threading.Event()
			reactor.callFromThread(subscriber.createClientConnection, subscribeEvent, market, updateTimeStamp)
			subscribeEventPass = subscribeEvent.wait(10)

			self.assertTrue(subscribeEventPass)
			self.assertTrue(publisherClient.isAlive())
			subscribeEvent.clear()

			for market in test_conf:

				expectedUpdates = getExpectedUpdates(market, test_conf[market])



				for factor in expectedUpdates:
					recievedUpdates = []


					counter = 1
					for update in expectedUpdates[factor]:
						print counter
						counter += 1
						getMessageEvent = threading.Event()
						reactor.callFromThread(subscriber.getNextMessage, getMessageEvent)

						getMessageEventPass = getMessageEvent.wait(10)

						self.assertTrue(getMessageEventPass)
						self.assertTrue(publisherClient.isAlive())

						envelope = subscriber.getMessageEnvelope()

						recievedUpdates.append(envelope.Message)


					self.assertEqual(len(recievedUpdates), len(expectedUpdates[factor]))



	orginalWD = os.getcwd()
		os.chdir(config['mainDirectory'])
		# Kill all processes
		subprocess.call(["python", "testscript.py", "-K"])
		os.chdir(orginalWD)


if __name__ == "__main__":

	sys.path.insert(0, '../')

	with open('config.json') as config_file:
		config = json.load(config_file)

	# Calls UFDataTest and runs all the functoions as assertions
	unittest.main()