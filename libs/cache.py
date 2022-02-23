from . import rd_client

# 定义hashset
QBUY_KEY = 'qbuy_active'


# 每件商品限购5件
def is_qbuyable():
    return rd_client.hlen(QBUY_KEY) < 5


# 验证用户是否已抢购
def exist_qbuy(user_id):
    return rd_client.hexists(QBUY_KEY, user_id)


# 向hashset中添加一个用户和抢购的商品
def add_qbuy(user_id, goods_id):
    rd_client.hset(QBUY_KEY, user_id, goods_id)


# 根据用户得到商品
def get_qbuy(user_id):
    return rd_client.hget(QBUY_KEY, user_id)

