import logging
import os
from datetime import datetime

# Generate a dynamic log filename based on the current date and time
log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")


# Ensure logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Complete log file path
log_filepath = os.path.join(log_dir, log_filename)




logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



logger = logging.getLogger(__name__)

