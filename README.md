<!---
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

This repository was modified for the purposes of these two papers:
[QA-Align: Representing Cross-Text Content Overlap by Aligning Question-Answer Propositions](https://arxiv.org/abs/2109.12655)
and
[Extending Multi-Text Sentence Fusion Resources via Pyramid Annotations](https://arxiv.org/abs/2110.04517)

Relevant modified code can be found [here](examples/seq2seq/).

Specifically the trainer files for training a seq2seq model were modified to train a BART model 
on the Sentence Fusion task.