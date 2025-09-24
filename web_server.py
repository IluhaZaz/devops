from fastapi import FastAPI, Request, Response
import subprocess
import os

PATH="/home/ilie/Documents/devops/DonJulioPub"

app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    target_branch = None
    
    payload = await request.json()
    ref = payload.get('ref', '')
    if ref.startswith('refs/heads/'):
        target_branch = ref.replace('refs/heads/', '')

    os.chdir(PATH)
    subprocess.run(["git", "fetch"])
    print(f"Switching to {target_branch}")
    subprocess.run(["git", "checkout", target_branch])
    subprocess.run(["git", "pull"])
    subprocess.run(["pip", "install", "-r", os.path.join(PATH, "requirements.txt")])
    print("Run migrations")
    subprocess.run(["sudo", "-u",  "ilie", "python", "don_julio_pub/manage.py", "migrate"])
    print("Run app")
    subprocess.run(["systemctl", "restart", "donjulio"])
    return Response(status_code=200)

@app.get("/")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
