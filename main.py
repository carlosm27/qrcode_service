if __name__ == "__main__":

    import uvicorn
    import os
    from dotenv import load_dotenv

    uvicorn.run("app:app", host=HOST, port=PORT)
