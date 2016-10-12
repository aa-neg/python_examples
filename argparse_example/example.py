

if __name__ == "__main__":
    # Library imports
    import datetime
    import sys
    import argparse
    import os
    import logging
    import json
    import time

    argparser = argparse.ArgumentParser(
            usage="here is some usage",
            description=""
            )


    argparser.add_argument(
            '--market',
            )

    argparser.add_argument(
            '--version',
            help=""
            )

    argparser.add_argument(
            '--fp',
            help="",
            default=""
            )

    argparser.add_argument(
            '--Name',
            help=""
            )

    argparser.add_argument(
            '--configLocation',
            help="",
            default=""
        )

    argparser.add_argument(
            '--queue',
            help="T",
            default=""
        )


    arguments = argparser.parse_args()

    queueName = arguments.queue
    arguments.__dict__.pop('queue', None)

    startTime = datetime.datetime.utcnow()
    if len(arguments.__dict__.keys()) == 1:
        print "Please specify some arguments to send"
        exit(1)

    else:
        originalWD = os.getcwd()
        os.chdir(arguments.configLocation)

        arguments.__dict__.pop('configLocation', None)
        from rabbitMQClient import RabbitMQClient

        with open('config.json') as config_file:
            config = json.load(config_file)