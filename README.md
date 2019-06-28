# MigrateToAndroidX
Python Script to automatically migrate old imports in a React-Native project to AndroidX imports

## What does it do? 
* Uses the bindings file provided by [Android](https://developer.android.com/jetpack/androidx/migrate)
* Looks at all the `node_modules` java files and searches for the old bindings (Usually of the form `android.support.*`) and replaces with the new AndroidX imports(Of the form `androidx.*`)
* Currently, I'm only looking for a sublist of imports (that is used by most react-native libraries) and replacing them. 
The sublist of imports are below:-
1. `android.support.annotation.**`
2. `android.support.annotation.RequiresPermission.**`
3. `android.support.design.**` 
4. `android.support.v4.**`

## Usage
```python3 migrateToAndroidX.py --node_modules <path>```

### Example 
If your path is ~/projects/rnProject/node_modules/
```python3 migrateToAndroidX.py --node_modules ~/projects/rnProject/node_modules/```

