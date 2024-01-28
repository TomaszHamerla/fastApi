from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Package(BaseModel):
    name: str
    elf_assigned: str

class Elf(BaseModel):
    name: str
    status: str

packages_db = []
elves_db = []

@app.post("/packages/")
def create_package(package: Package):
    packages_db.append(package)
    return {"message": "Package added successfully"}

@app.get("/packages/{package_name}")
def get_package(package_name: str):
    for package in packages_db:
        if package.name == package_name:
            return package
    raise HTTPException(status_code=404, detail="Package not found")

@app.post("/elves/")
def create_elf(elf: Elf):
    elves_db.append(elf)
    return {"message": "Elf added successfully"}

@app.get("/elves/{elf_name}")
def get_elf(elf_name: str):
    for elf in elves_db:
        if elf.name == elf_name:
            return elf
    raise HTTPException(status_code=404, detail="Elf not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
