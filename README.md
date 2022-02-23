# jenkins_testing
This is a demo of tests running selenium that will run on jenkins

Things to note: 
A .env file will need to be added when running locally to run wordpress tests, under the tests folder
Ex:
```
WORDPRESSUSERNAME=tester
WORDPRESSPASSWORD=Password123
```

# Setup:
To run tests with pytest, you can run them through the command line
ex:
`pytest -m "wordpress" --options headless`

or you can run in parallel adding the `-n auto` tag. If running tests using logins, distint logins will need to be used to avoid test collisions
