import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import os

credential_path = r"C:\\Users\\achra\\OneDrive\\Desktop\\Data Science\\MLops\\vertex-ai-mlops-main\\GCP\\achraj-demo-e87b4292b45a.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def generate():
  vertexai.init(project="achraj-demo", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-flash-001",
  )
  responses = model.generate_content(
      [image2, """Can you convert the detailed information in this chart to a table?"""],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  for response in responses:
    print(response.text, end="")

image1 = Part.from_data(
    mime_type="image/png",
    data=base64.b64decode("""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"""))

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

generate()

