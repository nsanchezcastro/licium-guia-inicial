from app.core.base import Base

class AssetLoanService(Base):
    _name = "asset_lending.asset_loan_service"

    def checkout(self, asset_id, borrower_user_id, **kwargs):
        # Lógica simplificada para no bloquear el sistema
        asset = self.env["asset_lending.asset"].browse(asset_id)
        if asset:
            asset.write({"status": "loaned"})
            return True
        return False
    
    def return_asset(self, asset_id, **kwargs):
        asset = self.env["asset_lending.asset"].browse(asset_id)
        if asset:
            asset.write({"status": "available"})
            return True
        return False
        
    def mark_maintenance(self, asset_id, **kwargs):
        asset = self.env["asset_lending.asset"].browse(asset_id)
        if asset:
            asset.write({"status": "maintenance"})
            return True
        return False

    def release_maintenance(self, asset_id, **kwargs):
        asset = self.env["asset_lending.asset"].browse(asset_id)
        if asset:
            asset.write({"status": "available"})
            return True
        return False 
     