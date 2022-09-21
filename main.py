if __name__ == "__main__":

    import uvicorn
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    HOST= os.environ.get('HOST')
    PORT= os.environ.get('PORT')

    uvicorn.run("app:app", host=0.0.0.0, port=8000)
