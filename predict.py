from transformers import (
  AutoTokenizer, 
  AutoModelForSequenceClassification
)
import torch
from torch.nn import functional as F

MAX_SEQ_LEN = 150
MODEL_PATH = "model-5e-05-96-0.001-10/checkpoint-40"  # Local path
TOKENIZER = "qilowoq/AbLang_heavy"  # From HuggingFace


class PredictionPipeline:
  def __init__(self, sequence: str):
    """
    sequence to get stability prediction for
    """
    if len(sequence) > MAX_SEQ_LEN:
      raise ValueError(
        f"Sequence is too long.\nSequence length = {len(sequence)}, MAX_SEQ_LEN = {MAX_SEQ_LEN}"
      )
    self.seq = sequence
  
  def predict(self):
    """
    Runs self.seq through the model to get a stability prediction.
    Returns a dictionary that looks like:
    {
      'prediction' : "STABLE" or "UNSTABLE",
      'likelihood' : <likelihood of prediction> (float in range [0,1])
    }
    """
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    
    # Process and tokenize input sequence
    processed_seq = ' '.join(self.seq)
    encoded_input = tokenizer(processed_seq, return_tensors='pt')

    # Run sequence through model to get stability prediction
    with torch.no_grad():
      logits = model(**encoded_input).logits
      assert logits.size() == torch.Size([1, 2])

    prediction = logits.argmax().item()
    assert prediction in [0, 1]
    likelihood = F.softmax(logits, dim=-1).squeeze()[prediction].item()

    outputs = {0: "UNSTABLE", 1: "STABLE"}

    return {
      'prediction' : outputs[prediction],
      'likelihood' : likelihood
    }



     