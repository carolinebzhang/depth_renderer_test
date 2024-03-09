#from huggingface_hub import DatasetCard
from huggingface_hub import login
login()
import datasets

# If the dataset is gated/private, make sure you have run huggingface-cli login
#dataset = load_dataset("ShapeNet/ShapeNetCore")
datasets.load_dataset("ShapeNet/ShapeNetCore")
