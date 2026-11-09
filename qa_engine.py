from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class RAGChain:
    """Wrapper class for RAG chain with retriever"""
    def __init__(self, chain, retriever):
        self.chain = chain
        self.retriever = retriever
    
    def invoke(self, question: str) -> str:
        """Invoke the chain with a question"""
        return self.chain.invoke(question)


def create_qa_chain(vector_store):
    """Create QA chain using OpenAI API"""
    
    # Use OpenAI's GPT model
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7
    )
    
    # Custom prompt template
    template = """Use the following retrieved information to answer the question.
    If you don't know the answer, say "I don't know", don't make up an answer.
    Answer in Traditional Chinese.

    Document excerpts:
    {context}

    Question: {question}
    
    Detailed answer:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    
    # Create the RAG chain
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Return wrapped chain with retriever
    return RAGChain(chain, retriever)


def answer_question(qa_chain, question: str) -> dict:
    """Answer question and return result with source documents"""
    # Get the answer
    answer = qa_chain.invoke(question)
    
    # Retrieve source documents
    source_documents = qa_chain.retriever.invoke(question)
    
    return {
        "answer": answer,
        "source_documents": source_documents
    }
