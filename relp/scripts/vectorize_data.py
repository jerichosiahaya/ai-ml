import os
import sys
# Add the 'model' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from store.store import Store

print("Starting to vectorize the data...")

# Data to be vectorized
DATA_PATH=""

# File name to save the vectorized data
VECTOR_PATH=""

EMBEDDING="indobert"

em = Store(embedding=EMBEDDING)

em.fit(
    data=DATA_PATH,
    key="text",
    save_name=VECTOR_PATH
)

print("Done vectorizing the data.")
