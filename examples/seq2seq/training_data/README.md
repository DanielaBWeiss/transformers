## Training Fusion Sets

**This file contains information about the different fusion training sets and formats. All training files were split into roughly 75/10/15/. The data splits are based on the same splits by year that were done in 2013.**

`train_y = ['TAC2008', 'TAC2009', 'TAC2010','DUC2007-update']`<br/>
`val_y = ['TAC2011']`<br/>
`test_y = ['DUC2005', 'DUC2006','DUC2007']`<br/>

*With roughly the same cluster size distributions for cluster sizes.*

### Data files

**All folders in this directory contain train files formatted for the Fusion baseline model. TODO: link to huggingface seq2seq dir**
**Each folder contains trian/val/test files:**
`train.source, train.target, val.source, val.targer, test.source, test.target`

1. **Folders starting with pyr_**
These files represent fusion instances coming only from the reference summary sentences.
~4600 train instances.

2. **Folders starting with thadani_**
These files represent fusion instances coming from Thadani's recreated dataset.
~900 train instances.

3. **Folders starting with doc_**
These files represent fusion instances coming from the document source sentences.
~800 train instances.

4. **Folders starting with summdoc_**
These files represent fusion instances coming from both summary and document source sentences.
~5700 train instances.

4. Folders starting with "tiny" represent roughly 200 fusion instances used for debugging.


### -------- Different input formats ------------

**Each type of input format can have either a "size4" type, meaning clusters have a maximum of 4 input sentences.
(they were sorted based on word overlap first, then top 4 are taken).
"fullclus" means that clusters can have more than 4 input sentences. (max clusters are of size 10, larger were filtered)**

1. `Folders containing "concate"`
- These are input sentences from the same fusion instance that are concatenated with a " " only.
ex. "...... ...... ...... ......."

2. `Folders containing "sep"`
- These are input sentences with the " </s> " token between sentences.
ex. "...... </s> ........ </s> ......... </s> .........."


#### Min max lengths (in tokens) for each data type - parameters for beam search and fine-tuning

###### Pyramid source data
Max source input - 265 tokens (same for full cluster input and for max 4 sentences)

Max target input - 30 tokens
min target input - 3 (should be 4 in beam search)

###### Thadani source data
Max source input - 238 tokens (for full cluster input), 182 (for max 4 sentences)

Max target input - 24 tokens
min target input - 4 (should be 5 in beam search)
