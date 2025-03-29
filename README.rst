🚀 Stern Hackathon Demo
==============================================================================
This repository is part of our deliverables for the `Microsoft Garage presents Stern Hackathon <https://nyustern.campusgroups.com/sta/rsvp_boot?id=1928010>`_. It demonstrates how we built an AI assistant with comprehensive knowledge of any selected repository (using the `Python requests library <https://github.com/psf/requests>`_ as our demonstration example).


🔍 A Before and After Comparison
------------------------------------------------------------------------------
n this demonstration, we followed the installation instructions for our `ESClusive Repo AI <https://github.com/easyscalecloud/stern_hackathon_mvp>`_ product to generate a knowledge base for the `Python request library github repo <https://github.com/psf/requests>`_. Let's simulate being an engineer who wants to familiarize themselves with the repository before contributing. We'll ask several questions ranging from high-level concepts to specific details, comparing results with and without our knowledge base.

**❌ Without Our Knowledge Base**

We directly asked questions in ChatGPT. View the `chat history Requests Library Architecture without Knowledge Base <https://chatgpt.com/share/67e7e55b-1e90-800c-9743-e585e2f7f9e2>`_. We identified several problems:

- **📅 Outdated Information**: The source code structure described doesn't match the current GitHub repository
- **🔗 Broken Hyperlinks**: Links provided are fabricated and return 404 errors
- **❌ Inaccurate Information**: Unable to reference the source code directly, leading to factual errors

**✅ With Our Knowledge Base**

We uploaded our generated ``all_in_one_knowledge_base.txt`` file and asked identical questions. View the `chat history Requests Library Architecture with Knowledge Base <https://chatgpt.com/share/67e7e487-ace4-800c-b14e-78bb590e3b42>`_.

- **📅 Up-to-date Information**: All details reflect the current state of the repository
- **🔗 Accurate Hyperlinks**: All links correctly navigate to the source code on GitHub
- **✅ Source-verified Responses**: Every answer cites original source code with verifiable links

**💬 Questions We Asked**

    I want to get more familiar with this Python requests library source code.

    1. What is the overall architecture of the requests library?
    2. What are the core modules in the requests library, and what role does each play?
    3. How does the Session object work internally to manage request state and connection pooling?
    4. What is the role of adapters in requests, and how are they mounted and used?
    5. How does the library handle redirect logic, and where is that implemented?


🔗 Additional Demonstrations
------------------------------------------------------------------------------
- `GitHub Action Workflow Configuration <https://github.com/easyscalecloud/stern_hackathon_demo/blob/main/.github/workflows/run_esclusive_repo_ai.yml>`_: We simply followed the instructions in the `How to Use <https://github.com/easyscalecloud/stern_hackathon_mvp?tab=readme-ov-file#-how-to-use>`_ section and copied the provided workflow file..
- `Knowledge Base Configuration <https://github.com/easyscalecloud/stern_hackathon_demo/blob/main/.github/workflows/esclusive_repo_ai_config.json>`_: We created a custom configuration to connect to our target repository.
- `Sample Automation Run <https://github.com/easyscalecloud/stern_hackathon_demo/actions/runs/14138804033/job/39616466381>`_: View the CI job automatically generating our knowledge base.
- `Generated all_in_one_knowledge_base.txt file <https://github.com/easyscalecloud/stern_hackathon_demo/releases/download/knowledge-base/all_in_one_knowledge_base.txt>`_: Download the resulting file from our `GitHub Release <https://github.com/easyscalecloud/stern_hackathon_demo/releases/tag/knowledge-base>`_ that can be used with any AI assistant.
