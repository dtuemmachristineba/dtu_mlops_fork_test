import wandb
import torch
from model import MyAwesomeModel
run = wandb.init()
artifact = run.use_artifact('s204605-danmarks-tekniske-universitet-dtu-org/wandb-registry-mnist/corrupt_mnist_model:v0', type='model')
artifact_dir = artifact.download("root")
model = MyAwesomeModel()
model.load_state_dict(torch.load("root/model.pth"))

