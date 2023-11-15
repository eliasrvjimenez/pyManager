import time
import sys

output_stream = sys.stdout
def print_status(event, start_time):
    end_time = time.time()
    output_stream.write('Current Run Time: %s' % ((start_time-end_time)))
    