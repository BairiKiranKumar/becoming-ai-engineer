# Day 1 - Plain-English glossary

[Day 1 home](README.md) · [Class 1](01-ai-vs-ml-vs-deep-learning/README.md) · [Class 2](02-generative-ai-vs-traditional-ai/README.md) · [Class 3](03-what-ai-engineers-actually-build/README.md)

Use this as a lookup page, not a list to memorize. Definitions here are deliberately short; the linked classes show how the terms work together. References for the technical concepts are in each class.

## AI

**Artificial intelligence:** the broad field of building systems for tasks associated with intelligence, such as planning, recognizing patterns, reasoning, or handling language. AI includes methods that learn and methods based on explicit rules or search.

## Machine learning

An approach in which a model is fitted to examples, rather than a programmer writing every decision rule. People still choose the task, data, method, and tests. **ML** is the abbreviation.

## Deep learning

Machine learning using neural networks with multiple processing layers to learn representations. **DL** is the abbreviation. It is one part of ML, not a replacement for all other methods.

## Model

A mathematical system that turns an input into an output. In a learned model, some internal settings come from training. Example: email measurements go in; a spam score comes out.

## Algorithm

A procedure for doing a task. A training algorithm adjusts a model; the resulting fitted model is what you later use for predictions. The procedure and its learned result are different things.

## Dataset

A collection of examples. A training dataset is used to fit a model. A separate test dataset helps check how the resulting model behaves on examples kept out of training.

## Feature

An input value or representation used by a model. An email's link count could be a feature. Features can be designed by people or learned as representations.

## Label

The answer attached to an example in supervised learning, such as `spam` or `normal`. A model's predicted label can disagree with the correct label.

## Training

The process of adjusting a model using data and an objective. It is like practice with feedback, but the computer is changing numbers, not developing human experience.

## Inference

Using a fitted model to produce an output. Asking a model a question is usually inference; it does not by itself demonstrate that the model's parameters changed.

## Parameter

An adjustable value inside a model. Weights and biases are examples. Not every number in a program is a learned parameter.

## Neural network

A mathematical model made of connected processing units arranged in layers. Each unit transforms numbers received from earlier units. The name is inspired by biology; this is not a literal brain and does not establish consciousness. The usual term is **neural network**, rather than "neural networking."

[See the visual explanation in Class 1](01-ai-vs-ml-vs-deep-learning/README.md#neural-network)

## Neuron

One processing unit in an artificial neural network. It combines input numbers using weights and a bias, then applies a transformation called an activation function.

## Weight

A number that changes how strongly an input contributes to a unit's calculation. Its meaning depends on the model; a large weight is not automatically a reliable measure of a feature's real-world importance.

## Bias

An adjustable offset in a calculation. In the expression `2x + 3`, the `+3` plays the role of an offset. This mathematical meaning differs from unfair or social bias.

## Layer

A stage of processing in a neural network. Inputs enter the input layer, intermediate work happens in hidden layers, and an output is produced at the end. "Hidden" means between input and output, not secret or conscious.

## Activation function

A transformation applied within a neuron. A nonlinear activation lets layered networks represent relationships that repeated linear operations alone cannot. One example is ReLU: return zero for a negative input, otherwise return that input.

## Loss

A numerical penalty used during training. It measures how poorly predictions meet the chosen objective. Lower training loss does not automatically mean better real-world behavior.

## Generalization

Useful performance on relevant examples not used to fit the model. A spam filter must handle new emails, not only the training inbox.

## Overfitting

Fitting the training examples so closely that performance on new examples suffers. Memorizing a practice sheet is a useful analogy, but actual causes require investigation.

## Classification

Choosing a category, such as billing, delivery, or spam. A model may first produce scores and then select a label.

## Regression

Predicting a numerical quantity, such as delivery time. Predicting a category and predicting a number need different checks.

## Generative AI

AI used to produce content such as text, images, audio, or code. Generated content can be useful and still require verification.

## Language model

A model of language sequences. In the text-generation example here, it uses context to predict possible next tokens repeatedly. **LLM** means large language model; this guide does not define "large" by a fixed parameter cutoff.

## Token

A unit used to encode text for a model. A token can represent a whole word, part of a word, punctuation, or another text unit, depending on the tokenizer. A token is not necessarily a word.

## Tokenizer

The software that converts text into token IDs and back. Exact splits depend on the selected tokenizer. An illustrative split in a diagram is not a measured tokenizer output.

## Prompt

The input supplied to guide a model's response, such as an instruction, a question, or example answers. A prompt is not a substitute for application permissions.

## Context

The information available to the model for a particular request, such as the question and supplied document passages. Request context is different from the model's learned parameters.

## Hallucination

Generated content that is false, fabricated, or unsupported while appearing plausible. The term does not mean a model has human sensory experiences. A made-up refund date is an example.

## API

**Application programming interface:** a defined way for software components to communicate. A weather app can request a forecast through a service's API. An API is an interface, not necessarily an AI model or an internet service.

## Retrieval

Searching for information relevant to a request. Finding a permitted policy passage is retrieval; writing a reply from it is a separate step.

## RAG

**Retrieval-augmented generation:** supplying retrieved information to a generation process. It can help provide evidence but does not guarantee a correct or faithful answer.

## Authentication

Checking who a user or process is. Signing in is a familiar example.

## Authorization

Deciding what an identified user or process is allowed to access or do. Being signed in does not mean a user may read every document.

## Grounding

Supporting an answer's claims with suitable evidence. A citation only helps if the source actually supports the claim.

## Evaluation

Checking a system against defined examples and success criteria. It is a planned test, not simply asking whether one demo answer looks good.

## Baseline

A simple comparison approach used to judge whether a more complex approach adds value. A keyword rule or ordinary search could be a baseline.

## Latency

How long a request takes to get a response. Whole-system latency includes retrieval, model work, checks, and network time when relevant.

## Deployment

Making a version of a system available for its intended users. A notebook demonstration and a deployed application are different stages.

## Monitoring

Observing a running system's behavior, such as errors, response times, and user feedback. Monitoring does not automatically retrain the model.

## Escalation

Sending a case to an authorized person or process when the system cannot safely or confidently complete it.

## Rollback

Returning to a previously known system version when a change causes problems.

---

**Return to your class:** [1 - AI/ML/DL](01-ai-vs-ml-vs-deep-learning/README.md) · [2 - Prediction/generation](02-generative-ai-vs-traditional-ai/README.md) · [3 - AI engineering](03-what-ai-engineers-actually-build/README.md)
