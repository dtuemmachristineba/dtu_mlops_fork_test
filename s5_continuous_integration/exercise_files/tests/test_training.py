import pytest
import torch
from unittest.mock import patch, MagicMock
from model import MyAwesomeModel
from train import train
from data import corrupt_mnist


# Test if the training function runs without errors
@patch("wandb.init")  # Mock wandb.init
@patch("wandb.log")   # Mock wandb.log
@patch("wandb.Artifact")  # Mock wandb.Artifact
@patch("torch.save")  # Mock torch.save
def test_training(mock_save, mock_artifact, mock_log, mock_init):
    # Mock wandb.init to return a dummy object
    mock_init.return_value = MagicMock()

    # Mock dataset
    def mock_corrupt_mnist():
        train_data = [(torch.rand(1, 28, 28), torch.randint(0, 10, (1,))) for _ in range(10)]  # 10 random samples
        test_data = train_data
        return train_data, test_data

    with patch("data.corrupt_mnist", side_effect=mock_corrupt_mnist):
        # Call the train function
        train(lr=0.001, batch_size=2, epochs=1)

    # Check if wandb.init was called
    mock_init.assert_called_once()

    # Check if wandb.log was called
    assert mock_log.called

    # Check if torch.save was called
    mock_save.assert_called_once()

    # Check if an artifact was created
    mock_artifact.assert_called_once_with(
        name="corrupt_mnist",
        type="model",
        description="A model trained to classify corrupt MNIST images",
        metadata=pytest.approx,  # Metadata values will vary
    )


# Test if the model produces the correct output shape
def test_model_forward_pass():
    model = MyAwesomeModel()
    x = torch.rand(1, 1, 28, 28)  # Random input tensor
    y = model(x)  # Forward pass
    assert y.shape == (1, 10), f"Expected output shape (1, 10), but got {y.shape}"


if __name__ == "__main__":
    pytest.main()
