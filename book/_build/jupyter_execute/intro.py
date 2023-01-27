#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from IPython.display import Markdown as md
from IPython.display import display_markdown

todays_date = str(datetime.now().date())
month = datetime.now().strftime("%B")
year = str(datetime.now().year)

display_markdown('''# ESA DHR mothly report for {month} {year}''')
md("# ESA DHR mothly report for {} {}".format(month, year))


# # NBS monthly report
# 
# ## The NBS project
# 
# The European Space Agency (ESA) is in charge for the distribution of data from the Sentinel satellite constellation. In order to maintain a reliable and sustainable data hub, the creation and operation of multiples data hubs is necessary. With the purpose of keeping and maintaining a reliable and online source of data from the ESA Sentinel constellation for an Area Of Interest (AOI) covering Norway, the Norwegian Space Agency (NOSA) funded the National Bakke Segment (NBS) project. 
# 
# Therefore, MET Norway was contracted for the operation of the NBS data. The NBS is implementd as a part of the operational infrastructure at MET Norway. As so it follows the normal procedures for planning, implementation and testing , and operationalisation. User access to the NBS is configured according to NOSA requirements. This includes the use of ESA's DHuS software for synchronization between ESA and user accessibility.
# 
# The present report is part of MET Norway duties to inform about its perfomance as operator of the NBS. Monthly reports will be created mothly to regularly comunicate the status of MET Norway's NBS.  
# 
# ## The Sentinel products
# 
# The NBS project includes the management of the data received from Sentinel-1 (S1), Sentinel-2, Sentinel-3 (S3) and Sentinel-5p (S5p) satellites for the especified AOI. Each of the Sentinels has different operational modes for achieving images with different carachteristics. Those images can have different processing levels. The products included in the DHR are Level-1 images for all the Sentinels except for Sentinel-2. For which Level-1 (S2L1C) and Level-2 (S2L2A) are both included in the NBS.
# 
# ## BackEnds and FrontEnds
# 
# As operator of NBS, the source of Sentinel data is ESA; and ESA spreads the Sentinel data trough the data hub Scihub (scihub.copernicus.eu).Scihub is ESA's FrontEnd (FE) for Sentinel data accesibility. MET Norway uses the DHS software for synchronization and creation of other FrontEnds. During the synchronization process a BackEnd (BE) is created. MET Norway is also running two FEs, colhub.met.no and colhub-archive.met.no. The colhub FE includes or will include all the products mentioned for Sentinel global products plus S3 marine products from Copernicus, S1 products from the Kongsberg Satellite Services (KSAT), and S2 Digital Elevation Model (DEM). The colhub-archive FE includes data from S1, S2L1C, S2L2A, S2DEM, S3, S5p products for the AOI. An important distiction between both FEs is that colhub-archive will allways maintain available online all the products for the AOI.  
#  
# In order to maintain an accountability on products synchronized from ESA's Scihub and available for users at the different FEs, it is necessary to understand the architecture of MET Norway's DHR.
# 
