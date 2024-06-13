# meta
- this directory will hold writeups of anything could be considered a 'project' (of any size) as i learn ML
- focus is on asap implementing the type of projects valued by interviewers for dream jobs
- order/content of the earlier writeups might be weird to ppl unless they're like a 'math academia coder' that did a lot of linalg + image processing 
	- relatively strong at (aka will gloss over):
		- pure/apma
		- python
		- numpy/scipy/numba
		- image processing
		- leetcode/dsa
	- but relatively weak at (aka might add a lot of prose that seems 'obvious')
		- swe
		- ai/cv/nlp
		- stats
		- c/c++/architecture
		- cuda/parallel


# references
- https://deepai.org/definitions
- https://www.image-net.org/download-images.php


# replication inspo/priority
(in order)

## courses
- https://missing.csail.mit.edu/
	- is there any way i can have some kind of jupyter notebook that demonstrates the ideas in action? just so i always remember what they actually DO...ie not just reading code
		- ie set it up in some kind of folder with some dummy files so i can see what's happening...
- https://course.fast.ai/
- https://fullstackdeeplearning.com/course/
- ug intro
	- cmu 10-301 (ml)
	- cmu 11-785 (deep learning)
	- cmu 11-755 (ml for dsp)

## job postings

### openAI
- (maybe go find/add job postings even tho they don't seem to have any entry positions in nyc...just so i can get a sense of what they expect at the 'entry level', bc likely lots of valuable overlap with entry positions at the other companies)


### arthropic
- [Job Application for Resident at Anthropic](https://boards.greenhouse.io/anthropic/jobs/4019511008)
	- Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe and beneficial for our users and for society as a whole.
	- You might be a fit if you:
		- Are deeply curious about machine learning, especially large models, scaling laws, circuits-style interpretability, and human feedback.
		- Care about how machine learning affects society and about making AI safe.
		- Have a strong understanding of python, linear algebra, and calculus. 
		- Understand fundamental deep learning concepts and be able to implement them. Has likely done significant self-study, side projects, or a course related to deep learning.
		- Are results-oriented, with a bias towards flexibility and impact.
		- Have significant research or software engineering experience.
	- The easiest way to understand our research directions is to read our recent research. This research continues many of the directions our team worked on prior to Anthropic, including: GPT-3, Circuit-Based Interpretability, Multimodal Neurons, Scaling Laws, AI & Compute, Concrete Problems in AI Safety, and Learning from Human Preferences.
- [Job Application for Research Engineer at Anthropic](https://boards.greenhouse.io/anthropic/jobs/4019739008)
	- You want to build large scale ML systems from the ground up. You care about making safe, steerable, trustworthy systems. As a Research Engineer, you'll touch all parts of our code and infrastructure, whether that's making the cluster more reliable for our big jobs, improving throughput and efficiency, running and designing scientific experiments, or improving our dev tooling. You're excited to write code when you understand the research context and more broadly why it's important.
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
- [Job Application for Software Engineer at Anthropic](https://boards.greenhouse.io/anthropic/jobs/4020354008)
	- (all of the above, as well as)
	- Strong candidates may also have experience with:
		- Security and privacy best practice expertise
		- Machine learning infrastructure like GPUs, TPUs, or Trainium, as well as supporting networking infrastructure like NCCL
		- Low level systems, for example linux kernel tuning and eBPF 
		- Technical expertise: Quickly understanding systems design tradeoffs, keeping track of rapidly evolving software systems

### google (deepmind)
- 

### meta (fair/cas/reality labs)
- [Research Scientist - FAIR | Meta Careers](https://www.metacareers.com/jobs/803309161693980)
	- Minimum Qualifications
		Currently has or is in the process of obtaining a PhD degree in the field of Artificial Intelligence, Computer Vision, Speech, Multimodality, Natural Language Processing, a related field, or equivalent practical experience. Degree must be completed prior to joining Meta.
		Experience in deep learning frameworks (such as PyTorch, TensorFlow), C, C++, Python.
		Experience in AI frameworks like Hugging Face or other systems.
		Experience in training and use of language models and Transformers.
	- Preferred Qualifications
		Demonstrated research and software engineering experience via an internship, work experience, coding competitions, or widely used contributions in open source repositories (e.g. GitHub).
		Experience building systems based on machine learning and/or deep learning methods.
		Experience solving complex problems and comparing alternative solutions, tradeoffs, and diverse points of view to determine a path forward.
		Experience working and communicating cross functionally in a team environment.
		Research experience in machine learning, representation learning, optimization, statistics, applied mathematics, or data science.
- [Applied AI Research Scientist - Reinforcement Learning | Meta Careers](https://www.metacareers.com/jobs/1502575260363259/)
	- Minimum Qualifications
		Has obtained a Ph.D. degree in Machine Learning, Artificial Intelligence, Computer Science, Information or Multimedia Retrieval, Reinforcement Learning, Mathematics, or relevant technical field.
		Experience with Python, C++, Java or other related language
		Experience with deep learning frameworks such as Pytorch or Tensorflow
	- Preferred Qualifications
		Experience with reinforcement learning in applied areas beyond simple simulators.
		Demonstrated experience in solving analytical problems using quantitative approaches.
		Experience manipulating and analyzing complex, high-volume, high-dimensionality data from varying sources.
		Experience building systems based on machine learning, reinforcement learning and/or deep learning methods.
		Proven track record of achieving significant results as demonstrated by grants, fellowships, patents, as well as first-authored publications at leading workshops or conferences such as NeurIPS, ICLR, AAAI, RecSys, KDD, IJCAI, CVPR, ECCV, ACL, NAACL, EACL, ICASSP, or similar.
		Demonstrated software engineer experience via an internship, work experience, coding competitions, or widely used contributions in open source repositories (e.g. GitHub).
		Experience working and communicating cross functionally in a team environment.
- [Research Engineer - Reality Labs | Meta Careers](https://www.metacareers.com/jobs/312286434616856/)
	- 
- [Research Scientist - Reality Labs | Meta Careers](https://www.metacareers.com/jobs/1053514518891565/)
	- Research Scientist - Reality Labs Responsibilities
		Adapt standard machine learning methods to best leverage modern parallel environments (e.g. distributed clusters, multicore SMP, and GPU)
	- Minimum Qualifications
		Experience with developing machine learning models at scale from inception to business impact.
		Programming experience in Python and hands-on experience with frameworks such as PyTorch.
		Exposure to architectural patterns of large scale software applications.
	- Preferred Qualifications
		Experience in software engineering in industry.
		Experience bringing machine learning-based products from research to production.

### nvidia
- https://www.nvidia.com/en-us/research/research-scientists/

### apple (ml/cv/ai; vision pro)
- possibly positions in 'apple intelligence' division as well? was just announced 6/11/24, and iirc apple pretty secretive about stuff, so maybe that's why they don't have postings for that group yet

### microsoft (msr nyc)


### other candidates
- funded by dod
	- usa seriously ramping up funding in industry
		- https://time.com/6961317/ai-artificial-intelligence-us-military-spending/
		- https://www.defense.gov/News/News-Stories/Article/Article/3578219/dod-releases-ai-adoption-strategy/
	- https://www.ai.mil/references.html
	- https://qz.com/the-pentagon-is-spending-billions-on-big-tech-and-silic-1851423069
		- actually, so it looks like the biggest contracts are awarded to all the major companies anyways (microsoft, amazon, google, oracle, ibm)
- highest salaries
	- https://www.levels.fyi/blog/ai-engineer-compensation.html
		- netflix
		- amazon
		- uber
	- https://www.levels.fyi/blog/ai-engineer-compensation-q1-2024.html
		- linkedin
		- bytedance
		- airbnb
		- stripe
		- coupang
			- https://en.wikipedia.org/wiki/Coupang
				- korean e-commerce
		- cruise
			- https://en.wikipedia.org/wiki/Cruise_(autonomous_vehicle)
				- self-driving division of GM
			- https://www.levels.fyi/companies/cruise/salaries
- highest funding
	- https://www.forbes.com/lists/ai50/
- random big names
	- oracle
	- ibm
- 'reputable' career guides
	- https://careerservices.fas.harvard.edu/blog/2024/02/13/22-top-ai-companies-to-watch-in-2024/
		- c3
			- https://c3.ai/careers/
				- probly look for engineering wtih AI focus
		- databricks
		- datarobot
		- jasper



## career advice posts
- https://80000hours.org/career-reviews/ai-safety-researcher/#basic-machine-learning
	- Online intro courses like [fast.ai](https://course.fast.ai/) (focused on practical applications), [_Full Stack Deep Learning_](https://fullstackdeeplearning.com/), and the various courses at [deeplearning.ai](https://www.deeplearning.ai/courses/).
	- For more detail, see university courses like MIT’s [*Introduction to Machine Learning](https://openlearninglibrary.mit.edu/courses/course-v1:MITx+6.036+1T2019/course/), NYU’s [_Deep Learning_](https://atcold.github.io/pytorch-Deep-Learning/) for even more detail. We’d also recommend Google DeepMind’s [lecture series](https://www.youtube.com/playlist?list=PLqYmG7hTraZCRwoyGxvQkqVrZgDQi4m-5).
	- [PyTorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) is a very common package used for implementing neural networks, and probably worth learning! When I was first learning about ML, my first neural network was a 3-layer [convolutional neural network](https://cs231n.github.io/convolutional-networks/) with [L2 regularisation](https://cs231n.github.io/neural-networks-2/) classifying characters from the [MNIST database](https://en.wikipedia.org/wiki/MNIST_database). This is a pretty common first challenge, and a good way to learn PyTorch.
	- The courses from [AGI Safety Fundamentals](https://www.agisafetyfundamentals.com/), in particular the [_AI Alignment Course_](https://www.agisafetyfundamentals.com/ai-alignment-curriculum), possibly followed by [_Alignment 201_](https://www.agisafetyfundamentals.com/alignment-201-curriculum), which provide an introduction to research on the alignment problem.
	- [_Intro to ML Safety_](https://course.mlsafety.org/about), a course from the [Center for AI Safety](https://www.safe.ai/) focuses on withstanding hazards (“robustness”), identifying hazards (“monitoring”), and reducing systemic hazards (“systemic safety”), as well as alignment.
- https://80000hours.org/career-reviews/ai-safety-researcher/#getting-a-job-empirical-research
	- Ultimately, the best way of learning to do empirical research — especially in contributor and engineering-focused roles — is to work somewhere that does both high-quality engineering and cutting-edge research.
	- The top three companies are probably Google DeepMind (who offer [internships to students](https://ai-jobs.net/job/28354-research-engineer-intern-2023-london/)), OpenAI (who have a 6-month [residency programme](https://openai.com/blog/openai-residency)) and Anthropic.
	- Whether you want to be a research lead or a contributor, it’s going to help to become a really good software engineer. The best ways of doing this usually involve [getting a job as a software engineer at a big tech company or at a promising startup](https://80000hours.org/career-reviews/software-engineering/). (We’ve written an entire article about [becoming a software engineer](https://80000hours.org/career-reviews/software-engineering/).)
	- Many roles will require you to be a good ML engineer, which means going further than just [the basics](https://80000hours.org/career-reviews/ai-safety-researcher/#basic-machine-learning) we looked at above.
	- **!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! How much experience do you need to get a job? It’s worth reiterating the tests we looked at above for contributor roles:**
		- **In a [blog post about hiring for safety researchers](https://www.alignmentforum.org/posts/nzmCvRvPm4xJuqztv/deepmind-is-hiring-for-the-scalable-alignment-and-alignment), the DeepMind team said “as a rough test for the Research Engineer role, if you can reproduce a typical ML paper in a few hundred hours and your interests align with ours, we’re probably interested in interviewing you.”**
		- **Looking specifically at _software engineering_, one hiring manager at Anthropic said that if you could, with a few weeks’ work, write a new feature or fix a serious bug in a major ML library, they’d want to interview you straight away. ([Read more](https://www.alignmentforum.org/posts/YDF7XhMThhNfHfim9/ai-safety-needs-great-engineers).)**
	- If you’re doing another job, or a degree, or think you need to learn some more before trying to change careers, there are a few good ways of getting more experience doing ML engineering that go beyond the basics we’ve already covered:
		- **Replicating papers.** One great way of getting experience doing ML engineering, is to replicate some papers in whatever sub-field you might want to work in. Richard Ngo, an AI governance researcher at OpenAI, has written some [advice on replicating papers](https://forum.effectivealtruism.org/posts/fRjj6nm9xbW4kFcTZ/advice-on-pursuing-technical-ai-safety-research#2_1__Advice_on_paper_replication). But bear in mind that replicating papers can be quite hard — take a look at [Amid Fish’s blog on what he learned replicating a deep RL paper](http://amid.fish/reproducing-deep-rl). Finally, [Rogers-Smith has some suggestions on papers to replicate](https://forum.effectivealtruism.org/posts/7WXPkpqKGKewAymJf/how-to-pursue-a-career-in-technical-ai-alignment#How_to_pursue_research_contributor__ML_engineering__roles). If you do spend some time replicating papers, remember that when you get to applying for roles, it will be really useful to be able to prove you’ve done the work. So try uploading your work to GitHub, or writing a blog on your progress. And if you’re thinking about spending a long time on this (say, over 100 hours), try to get some feedback on the papers you might replicate before you start — you could even reach out to a company or lab you want to work for.
		- **Taking or following a more in-depth course in empirical AI safety research.** Redwood Research ran the [MLAB](https://www.redwoodresearch.org/mlab) bootcamp, and you can apply for access to their curriculum [here](https://airtable.com/shrOOfZIZC4zZtAIr). You could also take a look at [this Deep Learning Curriculum](https://github.com/jacobhilton/deep_learning_curriculum) by Jacob Hilton, a researcher at the Alignment Research Center — although it’s probably very challenging without mentorship.[4](https://80000hours.org/career-reviews/ai-safety-researcher/#fn-4) The [Alignment Research Engineer Accelerator](https://www.arena.education/) is a program that uses this curriculum. Some mentors on the [SERI ML Alignment Theory Scholars Program](https://www.serimats.org/) focus on empirical research.
		- **Learning about a sub-field of deep learning.** In particular, we’d suggest _natural language processing_ (in particular transformers — see [this lecture](https://www.youtube.com/watch?v=sNfkZFVm_xs) as a starting point) and _reinforcement learning_ (take a look at [_Pong from Pixels_](https://karpathy.github.io/2016/05/31/rl/) by Andrej Karpathy, and OpenAI’s [_Spinning up in Deep RL_](https://spinningup.openai.com/en/latest/index.html)). Try to get to the point where you know about the most important recent advances.
- [How to pursue a career in technical AI alignment — EA Forum](https://forum.effectivealtruism.org/posts/7WXPkpqKGKewAymJf/how-to-pursue-a-career-in-technical-ai-alignment#How_to_pursue_research_contributor__ML_engineering__roles)
	- Computer vision:
	    - Very easy: train an MLP on MNIST.
	    - Easy: train a [ResNet](https://arxiv.org/abs/1512.03385) or another close-to-state-of-the-art model on ImageNet.
	    - Medium: do some basic adversarial attacks and defences. You might want to play with [this](https://adversarial-ml-tutorial.org/) first. You could try out some attacks and defences from [this](https://course.mlsafety.org/readings/#adversarial-robustness) list of papers.

## lists of papers/projects
- company publications
	- https://openai.com/news/research/
	- https://www.anthropic.com/research
		- scroll down to 'Publications' header
	- https://deepmind.google/research/publications/
	- https://research.facebook.com/publications/
		- https://ai.meta.com/results/?content_types%5B0%5D=publication
- https://paperswithcode.com/methods/area/computer-vision
- https://github.com/pytorch/examples


## contributing to pytorch
- https://pytorch.org/docs/master/community/contribution_guide.html
- https://github.com/pytorch/pytorch/blob/main/CONTRIBUTING.md
- https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions
- https://pytorch.org/blog/a-tour-of-pytorch-internals-1/
- https://pytorch.org/blog/a-tour-of-pytorch-internals-2/


## kaggle
- https://www.kaggle.com/docs/competitions#getting-started
	- https://www.kaggle.com/competitions?hostSegmentIdFilter=5
- [Some of the Best Kaggle Competitions for Beginners V2 | Kaggle](https://www.kaggle.com/discussions/getting-started/78482)
- 