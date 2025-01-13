import wandb
api = wandb.Api()
artifact_path = "s204605-danmarks-tekniske-universitet-dtu/corrupt_mnist/corrupt_mnist:v2"
artifact = api.artifact(artifact_path)
artifact.link(target_path="s204605-danmarks-tekniske-universitet-dtu-org/wandb-registry-mnist/corrupt_mnist_model")
artifact.save()