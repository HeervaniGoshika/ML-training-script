import subprocess

def test_training_script_runs():
    """Ensure train_model.py runs without errors"""
    result = subprocess.run(["python", "train_model.py"], capture_output=True, text=True)

    # If return code ≠ 0, script crashed
    assert result.returncode == 0, f"Training script failed:\n{result.stderr}"

    # Check for expected print message
    assert "Model trained successfully!" in result.stdout
