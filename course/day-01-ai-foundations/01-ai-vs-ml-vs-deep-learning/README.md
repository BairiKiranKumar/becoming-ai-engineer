# D01L01 — AI vs ML vs Deep Learning

## Start with one concrete example

Imagine an email filter. With hand-written rules, a programmer writes decisions such as checking known spam phrases. With machine learning, training examples pair emails with labels such as spam or normal, and the model learns patterns used to predict a new email’s label. Deep learning is a subset of machine learning that learns representations through many neural layers. For an image classifier, a simplified illustration shows simple visual patterns being combined into more complex patterns; exact layer roles vary by model. Keep the family relationship in mind: deep learning is inside ML, and ML is inside AI.

This is the worked example used in the revised editorial Reel. The sections below explain the details and limitations.


> Prepared locally for editorial review; not yet published.

**Day:** 01 · **Lesson:** 1/3 · **Level:** beginner · **Study time:** approximately 15–25 minutes
**Prepared:** 2026-11-05 · @kiranbuildswithai

Special series welcome; no previous lesson.

## What you will learn

- Explain AI, machine learning (ML), and deep learning (DL) without treating them as synonyms.
- Classify a system from its implementation, rather than from its marketing name.
- Separate training from inference and choose a sensible first baseline.

## Before you start

No coding or mathematics is required. A **model** is a mathematical system that maps inputs to outputs. **Data** means recorded examples. This is the first lesson of Becoming an AI Engineer: a sequence about building useful, testable systems. The 30 days describe the release schedule, not guaranteed mastery.

## Beginner explanation

**Artificial intelligence** is a broad field concerned with systems that perform tasks associated with intelligence, such as planning, perception, reasoning, and language. AI includes approaches based on explicit knowledge, rules, and search, as well as learning.

**Machine learning** is an approach within AI in which a model’s behavior is learned from data rather than every decision being explicitly programmed. Engineers still choose the objective, data, representation, and evaluation method. Learning does not mean the system is conscious or learns safely on its own.

**Deep learning** is a family of ML methods using neural networks with multiple processing layers. These layers can learn useful representations of the input. For example, an image network can transform pixel values into features useful for predicting an object label.

A useful map is **DL ⊂ ML ⊂ AI**. Membership overlaps: a deep-learning model is also an ML model and part of AI. These are not three successive products you must buy or three capability levels.

An analogy is nested toolboxes: the AI toolbox contains ML tools, and ML contains deep-learning tools. The analogy describes membership, not superiority or the exact historical boundary of every method.

## Visual explanation guidance

![AI contains ML, which contains deep learning; rule-based reasoning sits outside ML, while a deep image classifier belongs to all three.](visuals/D01L01-concept.svg)

Read from the outer box inward. Keep the rule-based example in AI but outside ML. Keep logistic regression in ML but outside DL. Put a deep neural image classifier inside DL. Do not draw three separate, disjoint circles. The cover’s glass sculpture is a metaphor; this labeled diagram carries the technical explanation.

## Deeper explanation: training, inference, and representations

For a supervised-learning example, the training set contains pairs `(x, y)`: inputs and desired labels. A spam example might use `x = email features` and `y = spam / not spam`. An algorithm adjusts parameters, often written θ, to reduce an average loss:

$$\theta^* = \arg\min_\theta \frac{1}{n}\sum_{i=1}^{n} L(f_\theta(x_i), y_i).$$

In words: choose model settings that reduce mistakes on training examples. This equation illustrates supervised learning; ML also includes unsupervised learning and reinforcement learning with different objectives.

**Training** changes parameters using data. **Inference** uses a trained model on a new input; parameters typically remain fixed. A chat with a model does not, by itself, demonstrate that its weights changed.

In logistic regression, an engineer can supply features such as a suspicious-link count, and the model learns weights on those features. Deep learning can learn layered representations as part of the model. A simple layer can be written `h = activation(Wx + b)`: weighted inputs, a bias, and a transformation. Composing layers enables complex functions. The popular “edges → shapes → objects” picture is a teaching illustration for some vision models, not a guaranteed description of every learned neuron or architecture.

**Generalization** means performing well on examples not used to fit the model. Low training error alone is not enough. Keep evaluation data separate; otherwise you may measure memorization or data leakage rather than useful learning.

## Examples: same broad task, different implementations

| Described implementation | AI? | ML? | DL? | Reason |
| --- | --- | --- | --- | --- |
| Rule-based expert system uses encoded facts and inference rules | Yes | No | No | Reasoning is explicitly specified |
| Logistic regression fitted to labeled spam emails | Yes | Yes | No | Weights are learned; not a deep network |
| Deep neural network trained for image classification | Yes | Yes | Yes | Learns through multiple neural layers |
| Calculator evaluates `2 + 2` | Not ordinarily classified as AI | No | No | Routine arithmetic alone is not evidence of AI |
| An app simply described as “a chatbot” | Unknown | Unknown | Unknown | The interface does not reveal the implementation |

### Worked activity

You need to route support tickets. Start with a keyword rule, compare a small learned classifier, and consider a deep language model only if its measured benefits justify the additional complexity. A rule may be brittle to paraphrases; a learned classifier needs representative labeled data; a large model can introduce latency, cost, and new failure modes.

Suppose a classifier labels 4 of 5 held-out tickets correctly. Accuracy is `4 / 5 = 0.8 = 80%`. This is an illustrative hand calculation, not a measured product result. Five tickets are far too few to establish reliability, and accuracy can hide important minority-class errors. Examine false positives and false negatives separately.

**Why no training code here?** This lesson teaches taxonomy and interpretation. The implementation-classification activity is the exercise; model training comes later. No API, GPU, or installation is required.

## Common mistakes and limitations

- **“Every automated rule is AI.”** Ordinary automation is not automatically intelligent reasoning. Describe the mechanism and task rather than stretching the label.
- **“All AI learns.”** Knowledge-based reasoning and search can be implemented without ML.
- **“All ML is deep learning.”** Linear models, trees, and many other ML methods are not DL.
- **“More layers always win.”** Data quality, task, compute, latency, interpretability, and evaluation matter. Stronger complexity requires evidence.
- **“An image proves the system uses DL.”** The same interface can hide different implementations.
- **“Training data is free to reuse.”** Check rights and remove unnecessary personal information before collecting or using data.

## Quick recap

AI is the broad field. ML learns behavior from data. DL uses multilayer neural networks within ML. Training fits parameters; inference applies them. The right choice depends on the problem and measured results.

## Practice questions

1. Does every DL model count as ML? Does every ML model count as DL?
2. A chatbot follows a hand-authored decision tree. Is its chat interface proof of ML?
3. A neural model gets perfect training accuracy but poor results on new emails. What should you investigate?
4. Your support-ticket rule gets 8 of 10 held-out tickets right. Compute accuracy and name one reason this is insufficient evidence.

<details><summary>Answers and reasoning</summary>

1. Yes; no. DL is a subset of ML.
2. No. A hand-authored tree is not learned from data. A *trained* decision tree would be ML; the word “tree” alone does not decide.
3. Overfitting, distribution differences, data leakage in earlier evaluation, and unrepresentative examples. Use a genuinely separate, representative evaluation set.
4. `8 / 10 = 80%`. The set is small; class imbalance or costly false negatives can make aggregate accuracy misleading.

</details>

## Glossary

- **Parameter:** a value adjusted during model training.
- **Feature:** an input representation useful for a task.
- **Inference:** applying a model to inputs.
- **Loss:** a measure of disagreement with the training objective.
- **Generalization:** useful performance beyond training examples.

## References

- Goodfellow, Bengio, Courville, *Deep Learning* (2016), [Chapter 1: Introduction](https://www.deeplearningbook.org/contents/intro.html). Primary textbook; taxonomy, representation learning, and layered functions. Consulted 2026-11-05. The diagram here is original, not a copied textbook figure.

## Continue learning

[Course roadmap](../../../ROADMAP.md). Next: D01L02 — Generative AI vs Traditional AI. See the roadmap for release availability; no future live guide is implied.
