from db_chat.chain import chain


def test_chain():
    print(chain.run("Find the top 5 products with the highest total sales revenue"))
