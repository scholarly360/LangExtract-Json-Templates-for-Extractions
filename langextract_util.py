import json, os, uuid
import langextract as lx

""" Load JSON file """
def util_load_data(data_file):
    with open(data_file, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data

""" Load examples from JSON file """
def util_load_examples(items):
    out = []
    for item in items:
        ex_list = [
            lx.data.Extraction(
                extraction_class=e["extraction_class"],
                extraction_text=e["extraction_text"],
                attributes=e.get("attributes", {}),
            )
            for e in item["extractions"]
        ]
        out.append(lx.data.ExampleData(text=item["text"], extractions=ex_list))
    return out

""" Load extraction data using langextract """
def util_load_extraction_data(param_template_json_file,param_api_key, param_text, param_model_id):
    ## load
    cfg = util_load_data(param_template_json_file)
    prompt = cfg["prompt"]
    examples = util_load_examples(cfg["examples"])

    result = lx.extract(
        text_or_documents=param_text,
        prompt_description=prompt,
        examples=examples,
        api_key=param_api_key,
        model_id=param_model_id,
    )

    uuid_tmp = "/tmp/" + str(uuid.uuid4().hex)
    lx.io.save_annotated_documents([result], output_name=f"{uuid_tmp}.jsonl", output_dir=".")
    out_result = util_load_data(f"{uuid_tmp}.jsonl")
    ## clean
    if os.path.exists(f"{uuid_tmp}.jsonl"):
        os.remove(f"{uuid_tmp}.jsonl")
    return(out_result)