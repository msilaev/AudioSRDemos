models = {
    "AudioUnet": "upsample48_audiounet",
    "MU-GAN": "upsample48_gan",
    "HiFi-GAN": "upsample48_hifigan",
    "Wide bandwidth": "hr48",
    "Narrow bandwidth": "lr_input16",
}

base_path = "data/listening_test/p347/p347_178_"

# Open README.md and write the table
with open("README.md", "w", encoding="utf-8") as f:
    f.write("| **Model** | **p347** |\n")
    f.write("|-----------|-----------------------------------------------------------------|\n")

    for model_name, file_suffix in models.items():
        f.write(
            f"| **{model_name}** | <audio controls><source src=\"{base_path}{file_suffix}.wav\" type=\"audio/wav\"></audio> |\n")

print("README.md has been updated successfully!")
