from datasets import load_from_disk , DatasetDict
from transformers import AutoModelForSequenceClassification , Trainer, TrainingArguments, DataCollatorWithPadding ,AutoTokenizer
from sklearn.model_selection import train_test_split
from Sentiment_Anaylsis.entity import Datatrainingconfig
class Data_training:
    def __init__(self, config:Datatrainingconfig):
        self.config=config 
        self.dataset=load_from_disk(self.config.transformed_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.source_name,num_labels=5)
        
    def training_args(self):
        
        tokenized_datasets=self.dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])
        train_testvalid = self.dataset['train'].train_test_split(test_size=0.1)
        train_test = train_testvalid['train'].train_test_split(test_size=0.1)
        tokenized_datasets = DatasetDict({
        'train': train_test['train'],
        'test': train_testvalid['test'],
        'valid': train_test['test']
})
        train_dataset = tokenized_datasets['train']
        valid_dataset = tokenized_datasets['valid']
        test_dataset = tokenized_datasets['test']  
        tokenizer = AutoTokenizer.from_pretrained(self.config.source_name) 

        data_collator = DataCollatorWithPadding(tokenizer)
        training_args = TrainingArguments(
        output_dir='./results',          # output directory
        num_train_epochs=3,              # number of training epochs
        per_device_train_batch_size=8,   # batch size for training
        per_device_eval_batch_size=8,    # batch size for evaluation
        warmup_steps=500,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./logs',            # directory for storing logs
        logging_steps=10,
        evaluation_strategy='epoch'      # Evaluate every epoch
    )
        trainer = Trainer(
        model=self.model,                         # the instantiated 🤗 Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        train_dataset=train_dataset,         # training dataset
        eval_dataset=valid_dataset,          # evaluation dataset
        data_collator=data_collator          # data collator
    )
        trainer.train()

        validation_results = trainer.evaluate(eval_dataset=valid_dataset)
        print("Validation results:", validation_results)

        # Evaluate the model on the test set
        test_results = trainer.evaluate(eval_dataset=test_dataset)
        print("Test results:", test_results)

        model_save_path = "./"
        self.model.save_pretrained(self.config.saving_model)
        tokenizer.save_pretrained(self.config.saving_model)