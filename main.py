from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from object_class.KNNG import KNNG_Builder
from object_class.retriever import Retriever
if __name__ == "__main__":
    # loading embedding model
    model_name = "mixedbread-ai/mxbai-embed-large-v1"
    hf_embeddings = HuggingFaceEmbeddings( model_name=model_name )

    # load document
    loader   = PyPDFLoader("Efficient K-Nearest Neighbor Graph Construction for Generic Similarity Measures.pdf")
    documrnt  = loader.load()

    #splitter
    text_splitter = RecursiveCharacterTextSplitter( chunk_size = 250 , chunk_overlap = 20 )

    # do split
    document = text_splitter.split_documents(documrnt)

    # build Graph
    KNNG = KNNG_Builder( document = document , embedding_model = hf_embeddings )
    KNNG.build_KNNG()

    # build retriever
    pool_max = 20
    retriever = Retriever(KNNG.B , hf_embeddings , pool_max )

    #test KNNG
    k = 20
    result     , _ = retriever.InVoke( "What is KNNG ?" , k = k )
    result_all     = retriever.Compare_with_all( "What is KNNG ?" , k = k )
    print(retriever.recall( KNNG_result = result , truth_result = result_all ,k = k ))

