from fastapi import FastAPI
#create a application instance.It represents a web application
app = FastAPI()

#Create API end point
@app.get("/shipment")
def get_shipment():
    return{
        "content" : "chair",
        "status"  : "Out for delivery"
    }