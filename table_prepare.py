models = {
    "AudioUnet": "upsample48_audiounet",
    "MU-GAN": "upsample48_gan",
    "HiFi-GAN": "upsample48_hifigan",
    "Wide bandwidth": "hr48",
    "Narrow bandwidth": "lr_input16",
}

base_path_347 = "data/listening_test/p347/p347_178_"
base_path_351 = "data/listening_test/p351/p351_181_"
base_path_360 = "data/listening_test/p360/p360_223_"
base_path_361_1 = "data/listening_test/p361/p361_094_"
base_path_361_2 = "data/listening_test/p361/p361_302_"

base_path_362_1 = "data/listening_test/p362/p362_125_"
base_path_362_2 = "data/listening_test/p362/p362_260_"

base_path_363 = "data/listening_test/p363/p363_307_"
base_path_364 = "data/listening_test/p364/p364_256_"
base_path_374 = "data/listening_test/p374/p374_028_"
base_path_376 = "data/listening_test/p376/p376_037_"

audio_examples = {
    "p347_178": base_path_347,
    "p351_181": base_path_351,
    "p360_223": base_path_360,
    "p361_094": base_path_361_1,
    "p361_302": base_path_361_2,
    "p362_125": base_path_362_1,
    "p362_260": base_path_363,
    "p363_307": base_path_364,
    "p364_256": base_path_374,
    "p376_037": base_path_376
}



# Open README.md and write the table
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Listening test" + "|\n")
    # Listening test

    head_str = f"| **Model** "
    delimeter_str = f"|-----------"

    for audio_name, base_path in audio_examples.items():
        str = f"| **{audio_name}** "
        head_str = head_str + str

        str = "|-----------------------------------------------------------------"
        #f.write("|-----------|-----------------------------------------------------------------|\n")
        delimeter_str = delimeter_str + str

    f.write(head_str + "|\n")
    f.write(delimeter_str + "|\n")

    for model_name, file_suffix in models.items():
        audio_str = f"| **{model_name}** "
        #f.write(f"| **{model_name}** ")
        #f.write(f"| **{model_name}** | <audio controls><source src=\"{base_path}{file_suffix}.wav\" type=\"audio/wav\"></audio> |\n")

        for audio_name, base_path in audio_examples.items():
            str = f"| <audio controls><source src=\"{base_path}{file_suffix}.wav\" type=\"audio/wav\"></audio> "
            audio_str = audio_str + str

            #f.write(f"| **Model** | **{audio_name}** |\n")
            #str = "|-----------------------------------------------------------------"
            #f.write("|-----------|-----------------------------------------------------------------|\n")
            #delimeter_str = delimeter_str + str

        f.write(audio_str + "|\n")



print("README.md has been updated successfully!")
