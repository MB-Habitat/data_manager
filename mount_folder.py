# Databricks notebook source
# MAGIC %md
# MAGIC ---
# MAGIC Author: Mustapha Bouhsen <br>
# MAGIC Email : mustapha.bouhsen@habitat-nature.com <br>
# MAGIC Date: July 31, 2024<br>
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create the mount folder
# MAGIC
# MAGIC In this section, we create a mount folder to get access the data in the blob storage

# COMMAND ----------

# storage_account_name = "datatest42"
# storage_key = "sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-08-31T03:31:55Z&st=2024-07-15T19:31:55Z&spr=https&sig=L3Ly%2Fos9foips1W5CkGiyg0hXZc%2BT2FzPN%2FuHOe%2BY58%3D"
# container_name = "database"

# COMMAND ----------

# mount_point = f"/mnt/{container_name}"

# dbutils.fs.mount(
#   source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/",
#   mount_point = mount_point,
#   extra_configs = {f"fs.azure.sas.{container_name}.{storage_account_name}.blob.core.windows.net":storage_key})
