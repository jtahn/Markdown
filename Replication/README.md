# references
- https://deepai.org/definitions
- https://d2l.ai/
- https://www.image-net.org/download-images.php


# replication inspo
(in order)

## courses
- https://course.fast.ai/
- https://fullstackdeeplearning.com/course/
- ug intro
	- cmu 10-301 (ml)
	- cmu 11-785 (deep learning)
	- cmu 11-755 (ml for dsp)

## job postings
- [Job Application for Research Engineer at Anthropic](https://boards.greenhouse.io/anthropic/jobs/4019739008)
	- Strong candidates may also have experience with:
		- High performance, large-scale ML systems
		- GPUs, Kubernetes, Pytorch, or OS internals
		- Language modeling with transformers
		- Reinforcement learning
		- Large-scale ETL
	- Representative projects:
		- Optimizing the throughput of a new attention mechanism
		- Comparing the compute efficiency of two Transformer variants
		- Making a Wikipedia dataset in a format models can easily consume
		- Scaling a distributed training job to thousands of GPUs
		- Writing a design doc for fault tolerance strategies
		- Creating an interactive visualization of attention between tokens in a language model

## career advice posts
- https://80000hours.org/career-reviews/ai-safety-researcher/#basic-machine-learning
	- Online intro courses like [fast.ai](https://course.fast.ai/) (focused on practical applications), [_Full Stack Deep Learning_](https://fullstackdeeplearning.com/), and the various courses at [deeplearning.ai](https://www.deeplearning.ai/courses/).
	- For more detail, see university courses like MIT’s [*Introduction to Machine Learning](https://openlearninglibrary.mit.edu/courses/course-v1:MITx+6.036+1T2019/course/), NYU’s [_Deep Learning_](https://atcold.github.io/pytorch-Deep-Learning/) for even more detail. We’d also recommend Google DeepMind’s [lecture series](https://www.youtube.com/playlist?list=PLqYmG7hTraZCRwoyGxvQkqVrZgDQi4m-5).
	- [PyTorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) is a very common package used for implementing neural networks, and probably worth learning! When I was first learning about ML, my first neural network was a 3-layer [convolutional neural network](https://cs231n.github.io/convolutional-networks/) with [L2 regularisation](https://cs231n.github.io/neural-networks-2/) classifying characters from the [MNIST database](https://en.wikipedia.org/wiki/MNIST_database). This is a pretty common first challenge, and a good way to learn PyTorch.
	- The courses from [AGI Safety Fundamentals](https://www.agisafetyfundamentals.com/), in particular the [_AI Alignment Course_](https://www.agisafetyfundamentals.com/ai-alignment-curriculum), possibly followed by [_Alignment 201_](https://www.agisafetyfundamentals.com/alignment-201-curriculum), which provide an introduction to research on the alignment problem.
	- [_Intro to ML Safety_](https://course.mlsafety.org/about), a course from the [Center for AI Safety](https://www.safe.ai/) focuses on withstanding hazards (“robustness”), identifying hazards (“monitoring”), and reducing systemic hazards (“systemic safety”), as well as alignment.
- https://80000hours.org/career-reviews/ai-safety-researcher/#getting-a-job-empirical-research
	- **Replicating papers.** One great way of getting experience doing ML engineering, is to replicate some papers in whatever sub-field you might want to work in. Richard Ngo, an AI governance researcher at OpenAI, has written some [advice on replicating papers](https://forum.effectivealtruism.org/posts/fRjj6nm9xbW4kFcTZ/advice-on-pursuing-technical-ai-safety-research#2_1__Advice_on_paper_replication). But bear in mind that replicating papers can be quite hard — take a look at [Amid Fish’s blog on what he learned replicating a deep RL paper](http://amid.fish/reproducing-deep-rl). Finally, [Rogers-Smith has some suggestions on papers to replicate](https://forum.effectivealtruism.org/posts/7WXPkpqKGKewAymJf/how-to-pursue-a-career-in-technical-ai-alignment#How_to_pursue_research_contributor__ML_engineering__roles). If you do spend some time replicating papers, remember that when you get to applying for roles, it will be really useful to be able to prove you’ve done the work. So try uploading your work to GitHub, or writing a blog on your progress. And if you’re thinking about spending a long time on this (say, over 100 hours), try to get some feedback on the papers you might replicate before you start — you could even reach out to a company or lab you want to work for.
- [How to pursue a career in technical AI alignment — EA Forum](https://forum.effectivealtruism.org/posts/7WXPkpqKGKewAymJf/how-to-pursue-a-career-in-technical-ai-alignment#How_to_pursue_research_contributor__ML_engineering__roles)
	- Computer vision:
	    - Very easy: train an MLP on MNIST.
	    - Easy: train a [ResNet](https://arxiv.org/abs/1512.03385) or another close-to-state-of-the-art model on ImageNet.
	    - Medium: do some basic adversarial attacks and defences. You might want to play with [this](https://adversarial-ml-tutorial.org/) first. You could try out some attacks and defences from [this](https://course.mlsafety.org/readings/#adversarial-robustness) list of papers.

## lists of papers
- https://paperswithcode.com/methods/area/computer-vision



