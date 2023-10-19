import openai
import os
from langchain.document_loaders import PyPDFLoader
from openai.embeddings_utils import cosine_similarity, get_embedding
from tqdm import tqdm

# 获取访问open ai的密钥
openai.api_key = "EMPTY"
openai.api_base = "http://182.254.164.88:8000/v1"
# 选择模型
EMBEDDING_MODEL = "vicuna-13b-v1.3"


def vicuna_cos(file1, file2):
    path = "data/cos/"
    loader_first = PyPDFLoader(path+file1)
    pages_first = loader_first.load_and_split()
    loader_second = PyPDFLoader(path+file2)
    pages_second = loader_second.load_and_split()
    pages_min = min(len(pages_first), len(pages_second))
    total_score = 0
    with tqdm(total=pages_min) as pbar:
        pbar.set_description('Processing:')
        for i in range(pages_min):
            pbar.update(1)
            embedding_first = get_embedding(
                pages_first[i].page_content, model=EMBEDDING_MODEL)
            embedding_second = get_embedding(
                pages_second[i].page_content, model=EMBEDDING_MODEL)
            total_score += cosine_similarity(embedding_first, embedding_second)
    return total_score / pages_min


print("相似度：%f" % vicuna_cos("党委理论学习中心组学习材料汇编2023年第16期.pdf", "chatle.pdf"))

# loader_first = PyPDFLoader(
#     "D:\CodePlace\Python\Prompt\engineer\data\cos\党委理论学习中心组学习材料汇编2023年第16期.pdf")
# pages_first = loader_first.load_and_split()
# loader_second = PyPDFLoader(
#     "D:\CodePlace\Python\Prompt\engineer\data\cos\chatle.pdf")
# pages_second = loader_second.load_and_split()
# pages_min = min(len(pages_first), len(pages_second))
# total_score = 0
# with tqdm(total=pages_min) as pbar:
#     pbar.set_description('Processing:')
#     for i in range(pages_min):
#         pbar.update(1)
#         embedding_first = get_embedding(
#             pages_first[i].page_content, model=EMBEDDING_MODEL)
#         embedding_second = get_embedding(
#             pages_second[i].page_content, model=EMBEDDING_MODEL)
#         total_score += cosine_similarity(embedding_first, embedding_second)
# print("相似度：%f" % (total_score / pages_min))


# positive_review = get_embedding("好评", model=EMBEDDING_MODEL)
# negative_review = get_embedding("差评", model=EMBEDDING_MODEL)

# positive_example = get_embedding(
#     "买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质", model=EMBEDDING_MODEL)
# negative_example = get_embedding("降价厉害，保价不合理，不推荐", model=EMBEDDING_MODEL)


# def get_score(sample_embedding):
#     return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)


# positive_score = get_score(positive_example)
# negative_score = get_score(negative_example)

# print("好评例子的评分 : %f" % (positive_score))
# print("差评例子的评分 : %f" % (negative_score))
