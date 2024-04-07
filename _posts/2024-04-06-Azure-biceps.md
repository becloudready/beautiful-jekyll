### Process of Creating Azure biceps template of resources created using Portal or other form

### Export template from a resource group

```
az group export --name demoGroup > exportedtemplate.json
```

To export more than one resource, pass the space-separated resource IDs. To export all resources, don't specify this argument or supply "*".

```
az group export --resource-group <resource-group-name> --resource-ids $storageAccountID1 $storageAccountID2
```

To decompile ARM template JSON to Bicep, use:

```
az bicep decompile --file exportedtemplate.json
```

The decompiled bicep template may not be perfect, so need to be validated before actually using

Do a dry run

```
az deployment group what-if --name my-deployment-name --resource-group rg-test --template-file template.bicep --parameters parameters.json 

```

It may throw errors like this
```
Warning no-hardcoded-location: A resource location should not use a hard-coded string or variable value. Please use a parameter value, an expression, or the string 'global'. Found: 'eastus' [https://aka.ms/bicep/linter/no-hardcoded-location]
Warning no-hardcoded-location: A resource location should not use a hard-coded string or variable value. Please use a parameter value, an expression, or the string 'global'. Found: 'eastus' [https://aka.ms/bicep/linter/no-hardcoded-location]
Warning adminusername-should-not-be-literal: Property 'adminUserName' should not use a literal value. Use a param instead. Found literal string value "azureuser" [https://aka.ms/bicep/linter/adminusername-should-not-be-literal]
 Warning no-hardcoded-location: A resource location should not use a hard-coded string or variable value. Please use a parameter value, an expression, or the string 'global'. Found: 'eastus' [https://aka.ms/bicep/linter/no-hardcoded-location]
```
In such case you need to edit the biceps file to include variable parameters

```
param location string = 'eastus'
param azureuser string = 'azureuser'
```
Replace these strings across the template, then try again.

If it throws no error then deploy it

```
az deployment group create --name my-deployment-name --resource-group rg-test --template-file template.bicep --parameters parameters.json 

```
