from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True


class VendorBase(BaseModel):
    name: str
    contact_info: str

class VendorCreate(VendorBase):
    pass

class OrderBase(BaseModel):
    item_id: int
    vendor_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        orm_mode = True
