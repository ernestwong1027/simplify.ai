from transformers import PegasusForConditionalGeneration, PegasusTokenizer, Trainer, TrainingArguments
import torch

#TODO: Test training with vm

class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __get__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels['input_ids'][idx])
        return item
    def __len__(self):
        return len(self.labels['input_ids'])

      
def prepare_data(model_name, train_texts, train_labels, val_texts=None, val_labels=None, test_texts=None, test_labels=None):

    tokenizer = PegasusTokenizer.from_pretrained(model_name)

    prepare_val = False if val_texts is None or val_labels is None else True
    prepare_test = False if test_texts is None or test_labels is None else True

    def tokenize_data(texts, labels):
        encodings = tokenizer(texts, truncation=True, padding=True)
        decodings = tokenizer(labels, truncation=True, padding=True)
        dataset_tokenized = Dataset(encodings, decodings)
        return dataset_tokenized

    train_dataset = tokenize_data(train_texts, train_labels)
    val_dataset = tokenize_data(val_texts, val_labels) if prepare_val else None
    test_dataset = tokenize_data(test_texts, test_labels) if prepare_test else None

    return train_dataset, val_dataset, test_dataset, tokenizer


def init_fine_tuning(model_name, tokenizer, train_dataset, val_dataset=None, freeze_encoder=False, output_dir='./results'):
 
  torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
  model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

  if freeze_encoder:
    for param in model.model.encoder.parameters():
      param.requires_grad = False

  if val_dataset is not None:
    training_args = TrainingArguments(
      output_dir=output_dir,           
      num_train_epochs=2000,          
      per_device_train_batch_size=1,   
      per_device_eval_batch_size=1,   
      save_steps=500,                 
      save_total_limit=5,             
      evaluation_strategy='steps',    
      eval_steps=100,                 
      warmup_steps=500,                
      weight_decay=0.01,              
      logging_dir='./logs',           
      logging_steps=10,
    )

    trainer = Trainer(
      model=model,                        
      args=training_args,                 
      train_dataset=train_dataset,      
      eval_dataset=val_dataset,          
      tokenizer=tokenizer
    )

  else:
    training_args = TrainingArguments(
      output_dir=output_dir,          
      num_train_epochs=2000,           
      per_device_train_batch_size=1,  
      save_steps=500,                  
      save_total_limit=5,              
      warmup_steps=500,              
      weight_decay=0.01,              
      logging_dir='./logs',           
      logging_steps=10,
    )

    trainer = Trainer(
      model=model,                        
      args=training_args,                  
      train_dataset=train_dataset,        
      tokenizer=tokenizer
    )

  return trainer


