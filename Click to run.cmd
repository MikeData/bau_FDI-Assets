:: Set filenames and extensions

:: FDI  Inward
SET FDIinwards="annualfdi2014inwarddirectionalv3_tcm77-426424"
SET FDIinwardsEXT=".xls"

:: FDI Outward
SET FDIoutwards="annualfdi2014outwarddirectionalv3_tcm77-426426"
SET FDIoutwardsEXT=".xls"

:: Assets
SET Assets="FDIassets"
SET AssetsEXT=".xls"

:: Liabilities
SET Liabilities="Liability"
SET LiabilitiesEXT=".xls"

:: ---------------------------------------------------------------------------------------
:: DONT alter anything past this point - unless altering which datasets we want to process
:: ---------------------------------------------------------------------------------------

:: Get rid of all in-text quotes so we can drop into command lines
SET inEXT=%FDIinwards%%FDIinwardsEXT%
SET inEXT=%inEXT:"=%
SET FDIinwards=%FDIinwards:"=%

SET outEXT=%FDIoutwards%%FDIoutwardsEXT%
SET outEXT=%outEXT:"=%
SET FDIoutwards=%FDIoutwards:"=%

SET AssEXT=%Assets%%AssetsEXT%
SET AssEXT=%AssEXT:"=%
SET Assets=%Assets:"=%

SET LiabEXT=%Liabilities%%LiabilitiesEXT%
SET LiabEXT=%LiabEXT:"=%
SET Liabilities=%Liabilities:"=%


:: <<<<<<<<<<<<<<<<<<<<<<<<<<<< Datasets 1-3, FDI - 2.2, 3.2, 4.2 (outward and inward combined for each)  >>>>>>>>>>>>>>>>>>>>>>>>>
:: <- Inwards and Outwards Flows for Direct Investment. Dataset1 ->
bake --preview FDI_Dataset1through3_recipe.py %inEXT% "2.2" "Flow" "Inwards" "E6"
bake --preview FDI_Dataset1through3_recipe.py %outEXT% "2.2" "Flow" "Outwards" "E7"
python FDI_Dataset_transform.py "data-"%FDIinwards%"-FDI_Dataset1through3_recipe-2.2,Flow,Inwards,E6.csv" "data-"%FDIoutwards%"-FDI_Dataset1through3_recipe-2.2,Flow,Outwards,E7.csv" "Transform_Dataset1"

:: <- Inwards and Outwards Flows for Investment Position. Dataset2 ->
bake --preview FDI_Dataset1through3_recipe.py %inEXT% "3.2" "Flow" "Inwards" "E6"
bake --preview FDI_Dataset1through3_recipe.py %outEXT% "3.2" "Flow" "Outwards" "E5"
python FDI_Dataset_transform.py "data-"%FDIinwards%"-FDI_Dataset1through3_recipe-3.2,Flow,Inwards,E6.csv" "data-"%FDIoutwards%"-FDI_Dataset1through3_recipe-3.2,Flow,Outwards,E5.csv" "Transform_Dataset2"

:: <- Inwards and Outwards Flows for Earnings. Dataset3 ->
bake --preview FDI_Dataset1through3_recipe.py %inEXT% "4.2" "Flow" "Inwards" "E6"
bake --preview FDI_Dataset1through3_recipe.py %outEXT% "4.2" "Flow" "Outwards" "E6"
python FDI_Dataset_transform.py "data-"%FDIinwards%"-FDI_Dataset1through3_recipe-4.2,Flow,Inwards,E6.csv" "data-"%FDIoutwards%"-FDI_Dataset1through3_recipe-4.2,Flow,Outwards,E6.csv" "Transform_Dataset3"


:: <<<<<<<<<<<<<<<<<<<<<<<<<<<< Datasets 4-6, Assets and Liabilties - 2.2, 3.2, 4.2 (outward and inward combined for each)  >>>>>>>>>>>>>>>>>>>>>>>>>
:: <- Assets and Liabilities for Direct Investment. Dataset4 ->
bake --preview FDI_Dataset4through6_recipe.py %AssEXT% "2.2 (SD)" "Ownership" "Assets" "E6"
bake --preview FDI_Dataset4through6_recipe.py %LiabEXT% "2.2 (SD)" "Ownership" "Liabilities" "E6"
python FDI_Dataset_transform.py "data-"%Assets%"-FDI_Dataset4through6_recipe-2.2 (SD),Ownership,Assets,E6.csv" "data-"%Liabilities%"-FDI_Dataset4through6_recipe-2.2 (SD),Ownership,Liabilities,E6.csv" "Transform_Dataset4"

:: <- Assets and Liabilities for Investment Position. Dataset5 ->
bake --preview FDI_Dataset4through6_recipe.py %AssEXT% "3.2 (SD)" "Ownership" "Assets" "E5"
bake --preview FDI_Dataset4through6_recipe.py %LiabEXT% "3.2 (SD)" "Ownership" "Liabilities" "E5"
python FDI_Dataset_transform.py "data-"%Assets%"FDIassets-FDI_Dataset4through6_recipe-3.2 (SD),Ownership,Assets,E5.csv" "data-"%Liabilities%"-FDI_Dataset4through6_recipe-3.2 (SD),Ownership,Liabilities,E5.csv" "Transform_Dataset5"

:: <- Assets and Liabilities for Earnings. Dataset6 -> 
bake --preview FDI_Dataset4through6_recipe.py %AssEXT% "4.2 (SD)" "Ownership" "Assets" "E5"
bake --preview FDI_Dataset4through6_recipe.py %LiabEXT% "4.2 (SD)" "Ownership" "Liabilities" "E5"
python FDI_Dataset_transform.py "data-"%Assets%"-FDI_Dataset4through6_recipe-4.2 (SD),Ownership,Assets,E5.csv" "data-"%Liabilities%"-FDI_Dataset4through6_recipe-4.2 (SD),Ownership,Liabilities,E5.csv" "Transform_Dataset6"



:: <<<<<<<<<<<<<<<<<<<<<<<<<<<< Tables 7 & 8. Table 7 = 2.3, 3.3, 4.3 for FDI. Table 8 = same thing for assets >>>>>>>>>>>>>>>>>>>>>>>>>
:: <- Area by SIC, Inwards and Outwards Flows, Dataset 8 ->
bake --preview FDI_Dataset7_recipe.py %inEXT% "Flow" "Inward"
bake --preview FDI_Dataset7_recipe.py %outEXT% "Flow" "Outward"
python FDI_Dataset_transform_7.py "data-"%FDIinwards%"-FDI_Dataset7_recipe-Flow,Inward.csv" "data-"%FDIoutwards%"-FDI_Dataset7_recipe-Flow,Outward.csv" "Transform_Dataset7"

:: <- Area by SIC, Inwards and Outwards Flows, Dataset 8 ->
bake --preview FDI_Dataset8_recipe.py %AssEXT% "Flow" "Inward"
bake --preview FDI_Dataset7_recipe.py %LiabEXT% "Flow" "Outward"
python FDI_Dataset_transform_8.py "data-"%Assets%"-FDI_Dataset8_recipe-Flow,Inward.csv" "data-"%Liabilities%"-FDI_Dataset8_recipe-Flow,Outward.csv" "Transform_Dataset7"



:: <<<<<<<<<<<<<<<<<<<<<<<<<<<< FDI only Tables >>>>>>>>>>>>>>>>>>>>>>>>>
:: <- Area by SIC, Inwards and Outwards Flows, Dataset 9 
bake --preview FDI_Dataset_recipe_9.py %inEXT% "Flow" "Inward"
bake --preview FDI_Dataset_recipe_9.py %outEXT% "Flow" "Outward"
python FDI_Dataset_transform_9.py "data-"%FDIoutwards%"-FDI_Dataset_recipe_9-Flow,Outward.csv" "data-"%FDIinwards%"-FDI_Dataset_recipe_9-Flow,Inward.csv" "Transform_Dataset9"

:: <- Area by SIC, Inwards and Outwards Flows, Dataset Xpoint / Summary ->
bake --preview FDI_Dataset_recipe_10.py %inEXT% Inward
bake --preview FDI_Dataset_recipe_10.py %outEXT% Outward
python FDI_Dataset_transform_10.py "data-"%FDIoutwards%"-FDI_Dataset_recipe_10-Outward.csv" "data-"%FDIinwards%"-FDI_Dataset_recipe_10-Inward.csv" "Transform_Dataset10.csv"


:: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
:: VALIDATION



