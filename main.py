from ade_pipeline import run_ade


if __name__ == "__main__":
    image_path = "sample_invoice.png" 

    result = run_ade(image_path)

    print("\n✅ FINAL STRUCTURED OUTPUT:")
    print(result.model_dump())