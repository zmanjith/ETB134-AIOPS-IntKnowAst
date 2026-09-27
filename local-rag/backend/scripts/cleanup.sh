mkdir app/legacy
git mv app/rag.py app/legacy/rag.py
git mv app/search.py app/legacy/search.py
git mv app/prompt_generator.py app/legacy/prompt_generator.py
git mv app/operational_inputs/log_parser.py app/legacy/log_parser.py
git mv app/test_llm.py app/legacy/test_llm.py
git rm app/embedding.py app/utils.py
git commit -m "Archive superseded RAG chain and empty stubs after retargeting main.py/api.py to RagService"
git push

## delete the files below

git rm app/rag.py app/search.py app/prompt_generator.py app/operational_inputs/log_parser.py app/test_llm.py app/embedding.py app/utils.py
git commit -m "Remove superseded RAG chain and unused files"
git push