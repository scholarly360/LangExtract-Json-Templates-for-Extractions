# LangExtract-Json-Templates-for-Extractions

Utilities built on top of Langextract that serve as Automatic Templates (in JSON format), making everything configurable instead of hard-coded


The code in langextract_util.py provides utility functions for loading and processing extraction tasks using the langextract library:

util_load_data(data_file): Loads and returns Template JSON data from a given file.

util_load_examples(items): Converts a list of example items (from JSON) into langextract.data.ExampleData objects, each containing extractions.

util_load_extraction_data(param_template_json_file, param_api_key, param_text, param_model_id):

Loads a template JSON file containing the extraction prompt and examples.
Uses the langextract library to perform extraction on the provided text, using the prompt and examples.
Saves the extraction result temporarily as a JSONL file, loads it, then deletes the temp file.
Returns the extraction result.
The code is designed to support a structured extraction workflow for merger and acquisition (M&A) deal data.

JSON Template File Format
```
{
  "task": "M&A extraction v1",
  "model_id": "gemini-2.5-flash",
  "prompt": "Task: Extract every merger or acquisition (including stake purchases and mergers) mentioned in the text.\n\nFor each deal, create ONE extraction with class \"ma_deal\".\nUse the SHORTEST exact text span that clearly refers to the deal (usually the sentence or key clause like \"X to acquire Y for $Z\").\n\nAttributes (use exact spans from the text; do not paraphrase):\n- acquirer: the buyer/first-named party (for mergers, use the first-named company).\n- target: the company being acquired / merged with.\n- amount_text: the deal value as written (e.g., \"$2.1 billion\", \"₹3,700 crore\", \"Rs 750 crore\"). If no value is stated, set to \"not disclosed\".\n\nRules:\n- Accept verbs/synonyms: acquire, buy, purchase, take over, merge with, combine with, acquire a % stake in, all-stock deal, cash-and-stock deal.\n- Prefer total deal value over per-share prices; if only a per-share price is present and clearly tied to the acquisition, use that per-share amount as amount_text (include the \"per share\" words).\n- Keep currency and units AS WRITTEN (support $, USD, ₹, Rs, INR, lakh, crore, million, billion). Do not normalize or convert.\n- If multiple deals appear, produce one \"ma_deal\" extraction per deal.\n- Do not invent amounts or company names not present in the text.",
  "examples": [
    {
      "text": "Canada's Gildan to buy Hanesbrands for $2.2 billion to expand basic apparel business",
      "extractions": [
        {
          "extraction_class": "ma_deal",
          "extraction_text": "Canada's Gildan to buy Hanesbrands for $2.2 billion",
          "attributes": {
            "acquirer": "Canada's Gildan",
            "target": "Hanesbrands",
            "amount_text": "$2.2 billion"
          }
        }
      ]
    }
  ]
}


```




