from transformers import Trainer, TrainingArguments, PegasusTokenizer, DataCollatorWithPadding
from datasets import load_dataset
import pandas as pd

# TODO: create dataset based off of lecture files, use array as possible dataframe using pandas 

# df = pd.read_csv(r"")
# full_df = pd.DataFrame(data=targets_data)

class PegasusTraining:
  """
  Finetuning the Pegasus model 
  """

  def __init__(self, dataset_path):
    self.dataset_name = dataset_path

  def preprocess(data):
    return tokenizer(data["text"], truncation=True)
  
  def TrainModel():
    pegasus_training_model=PegasusForConditionalGeneration.from_pretrained(model_name, num_labels=2).to(device)

    summarization_dataset = load_dataset("csv", data_files=self.datasetpath, sep=";")
    summarization_dataset["train"][0]
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    tokenized_dataset = summarization_dataset.map(preprocess, batched=True)
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    # TODO: tailor arguments to our data and set up instantiation

    training_args = TrainingArguments(
        output_dir="./results",
        learning_rate=2e-5,
        per_device_train_batch_size=16,     
        per_device_eval_batch_size=16,      
        num_train_epochs=5,
        weight_decay=0.01,
    )

    trainer = Trainer(
        model=pegasus_training_model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()

if __name__ == "main": 

  # dataset_path = 
  training = PegasusTraining(dataset_path)