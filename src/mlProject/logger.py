import os
import sys
import logging
import datetime

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# Create a subdirectory for today's logs
today = datetime.date.today()
today_log_dir = os.path.join(log_dir, today.strftime('%Y-%m-%d'))
if not os.path.exists(today_log_dir):
    os.mkdir(today_log_dir)

# Create a log file with a timestamp
log_file = os.path.join(today_log_dir, f'app_{os.path.basename(sys.argv[0])}_{os.getpid()}.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Log the command-line arguments
logger.info('Command-line arguments: %s', sys.argv)

# Log the current working directory
logger.info('Current working directory: %s', os.getcwd())

# Log the process ID
logger.info('Process ID: %s', os.getpid())