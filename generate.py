from main import Defaults, GPU

Defaults("FullDataFewEpoch", max_bytes=6*10**9, GPU=GPU.a80, epochs_per_dataset=0.2, data_folder_name="dataset_filtered_lichess_db_standard_rated_2023-09cleaned")
