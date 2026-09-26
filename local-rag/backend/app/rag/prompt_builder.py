from unittest import result

from rag.prompt_templates import AIOPS_SYSTEM_PROMPT


class PromptBuilder:

    def filter_retrieved_chunks(self, retrieved_chunks):
        unique_chunks = {}
        for result in retrieved_chunks:
            source = result.payload["source"]
            if source not in unique_chunks:
                unique_chunks[source] = result
        retrieved_chunks = unique_chunks.values()

    def build(self, question, retrieved_chunks):

        context_parts = []

        for result in retrieved_chunks:

            payload = result.payload

            context_parts.append(
                f"""
        Source: {payload['source']}
        Category: {payload['category']}
        Technology: {payload['technology']}

        Content:
        {payload['text']}

        ---------------------------------------------------
        """
            )

        retrieved_context = "\n".join(context_parts)

        instructions = """
Answer using ONLY the supplied knowledge.

Structure your answer as follows:

1. Problem Summary

2. Possible Root Cause

3. Investigation Steps

4. Recommended Commands

5. Suggested Resolution

6. Sources Used

If the retrieved knowledge does not contain the answer, clearly state that.
"""

        final_prompt = f"""
{AIOPS_SYSTEM_PROMPT}

================================================

QUESTION

================================================

{question}

================================================

RETRIEVED KNOWLEDGE

================================================

{retrieved_context}

================================================

TASK

================================================

{instructions}
"""

        return {

            "system_prompt": AIOPS_SYSTEM_PROMPT,

            "user_question": question,

            "retrieved_context": retrieved_context,

            "instructions": instructions,

            "final_prompt": final_prompt

        }