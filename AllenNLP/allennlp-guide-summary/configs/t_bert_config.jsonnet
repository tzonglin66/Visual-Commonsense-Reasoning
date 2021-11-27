{
    "dataset_reader": {
        "type": "t_classification-tsv",
        "tokenizer": {
            "type": "pretrained_transformer",
            "model_name": "bert-base-uncased"
        },
        "token_indexers": {
            "bert": {
                "type": "pretrained_transformer",
                "model_name": "bert-base-uncased"
            }
        },
        "max_tokens": 512
    },
    "train_data_path": "data/movie_review/train.tsv",
    "validation_data_path": "data/movie_review/dev.tsv",
    "model": {
        "type": "t_simple_classifier",
        "embedder": {
            "type": "basic",
            "token_embedders": {
                "bert": {
                    "type": "pretrained_transformer",
                    "model_name": "bert-base-uncased"
                }
            }
        },
        "encoder": {
            "type": "bert_pooler",
            "pretrained_model": "bert-base-uncased"
        }
    },
    "data_loader": {
        "batch_size": 8,
        "shuffle": true
    },
    "trainer": {
        "type": "gradient_descent",
        "optimizer": {
            "type": "huggingface_adamw",
            "lr": 1.0e-5
        },
        "num_epochs": 5
    }
}