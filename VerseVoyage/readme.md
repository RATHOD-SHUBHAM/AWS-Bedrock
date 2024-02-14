# Configure AWS CLI
- Add Access Key and Secret Access key of your user.
```commandline
terminal: 
% aws configure

>> Access Key
>> Secret Access Key
>> Region: us-east-1
>> output format: json
```

### llama2 Parameters

- [llama2-docs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-meta.html)
- [Example-Code](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-meta.html#api-inference-examples-meta-llama)
```commandline
Randomness and diversity
The Meta Llama 2 Chat and LLama 2 models supports the following parameters to control randomness and diversity in the response.

Temperature (temperature) – Use a lower value to decrease randomness in the response.

Top P (top_p) – Use a lower value to ignore less probable options. Set to 0 or 1.0 to disable.

Length
The Meta Llama 2 Chat and LLama 2 models support the following parameters to control the length of the generated response.

Maximum length (max_gen_len) – Specify the maximum number of tokens to use in the generated response. The model truncates the response once the generated text exceeds max_gen_len.
```

### AI21 Labs Jurassic-2 models

- [ai21 docs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html)
- [Code-Example](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html#api-inference-examples-a2i-jurassic)
```commandline
Randomness and Diversity
The AI21 Labs Jurassic-2 models support the following parameters to control randomness and diversity in the response.

Temperature (temperature)– Use a lower value to decrease randomness in the response.

Top P (topP) – Use a lower value to ignore less probable options.

Length
The AI21 Labs Jurassic-2 models support the following parameters to control the length of the generated response.

Max completion length (maxTokens) – Specify the maximum number of tokens to use in the generated response.

Stop sequences (stopSequences) – Configure stop sequences that the model recognizes and after which it stops generating further tokens. Press the Enter key to insert a newline character in a stop sequence. Use the Tab key to finish inserting a stop sequence.

```