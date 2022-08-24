from itertools import chain
import fastapi
import Blockchain

blockchain = Blockchain.Blockchain()
app = fastapi.FastAPI()


# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return fastapi.HTTPException(status_code=400,detail="the blockchain is invalid")
    
    block = blockchain.mine_block(data=data)

    return block

# endpoint to return the entire blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return fastapi.HTTPException(status_code=400,detail="the blockchain is invalid")

    chain = blockchain.chain
    return chain
