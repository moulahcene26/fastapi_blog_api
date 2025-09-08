from fastapi import APIRouter, HTTPException
from uuid import uuid4
from model import Post, PostUpdate
from database import db

router = APIRouter()

def post_helper(post) -> dict:
    return {
        "id": str(post["id"]),
        "created_at": str(post["created_at"]),
        "slug": str(post["slug"]),
        "title": str(post["title"]),
        "desc": str(post["desc"]),
        "content": str(post["content"]),
        "img": str(post["img"]),
    }


@router.post("/")
async def create_post(post: Post):
    post_dict = post.dict(by_alias=True)
    post_dict["_id"] = str(uuid4())
    result = await db.post.insert_one(post_dict)
    new_post = await db.post.find_one({"_id": result.inserted_id})
    return{"stat":201, "result":[post_helper(new_post)]}


@router.get("/")
async def list_post():
    posts = await db.posts.find().to_list(100)
    return{"stat":201, "result":[post_helper(post) for post in posts]}

@router.get("/{id}")
async def read_post(id: str):
    post = await db.posts.find_one({"_id": id})
    if post is not None:
        return {"stat": 201, "result": [post_helper(post)]}
    else:
        raise HTTPException(status_code=404, detail="post not found")
    

@router.put("/{id}")
async def update_post(id: str, post: PostUpdate):
    post_dict = {k: v for k, v in post.dict(exclude_none=True).items()}
    update_result = await db.posts.update_one(
        {"_id": id},
        {"$set": post_dict}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="post not found or not updated")
    return {"message": "updated successfully"}


@router.delete("/{id}")
async def delete_post(id:str):
    delete_result = await db.posts.delete_one({"_id":id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="post not found")
    return {"message": "deleted successfully"}
