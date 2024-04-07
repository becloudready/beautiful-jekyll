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

If it throws no error then deploy it

```
az deployment group create --name my-deployment-name --resource-group rg-test --template-file template.bicep --parameters parameters.json 

```
