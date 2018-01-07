# Kik Toolset

Kik Toolset is a simple set of tools that allows a programmer to get Kik User information in a way is not intended to

  - Resolve a partial E-Mail Address of any Kik account
  - Display public user information
  - PHP Version of KikLookup.py

This was written by Netkas (Daniel Blood) for Asscake.net where users can learn valuable skills about security research and programming.

# Skid alert
I'm aware, various skids are using this tool and thinking it's some sort of exploit, it's not. stop being dumb and learn to read the source.

# In Development
We are planning to add more tools, and scripts related to Kik when possible, Though some of these scripts are simple, they can be used for various things such as Websites that display Kik Accounts, And request a updated Profile Picture of any Kik Account directly from Kik themselves

### Example Uses

The python scripts require Python 3.+ to run properly, Though this can be Python2 Friendly easily.

`EmailResolver.py`

```
usage: EmailResolver.py [-h] [-u USERNAME] [-e ENDPOINT]

options for Kik Email Resolver

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username to resolve from.
  -e ENDPOINT, --endpoint ENDPOINT
                        The WS2 endpoint Location.
```
```
> python3 EmailResolver.py -u Levenshtein -e ws2.kik.com 
 [+] Making request...
 [+] Request Success!
 [!] No alert messages, Maybe it worked?
 [+] Success: a***e@example.com
```


`KikLookup.py`

```
usage: KikLookup.py [-h] [-u USERNAME] [-e ENDPOINT]

options for Kik Lookup

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username to grab information from
  -e ENDPOINT, --endpoint ENDPOINT
                        The WS2 endpoint Location.

```
```
> python3 KikLookup.py -u Levenshtein -e ws2.kik.com 
 [+] Making request...
 [+] Request Success!
 [+] FirstName: 湖北-涅克斯
 [+] LastName: #nlpfw
 [+] Display Pic Last Modified: 1505525272625
 [+] Display Pic URL: http://profilepics.kik.com/exampleid/orig.jpg
```
`KikHer.php`
```php
<?PHP
	require("KikHer.php"); /* Get the class for KikHer */
	$KikUser = new KikHer('Levenshtein', 'https://ws2.kik.com/user/'); /* Get the User Data */
	/* Print out the user data */
	echo(
		"<h1>"
		. $KikUser->FirstName()
		. " "
		. $KikUser->LastName()
		. "</h1>"
		. "<img src=\"" 
		. $KikUser->displayPicURL()
		. "\" height=\"142\" width=\"142\"><br>" 
		. "Last Modified: "
		. gmdate("y-m-d h:i:s", $KikUser->displayPicLastModified())\
		. "<hr>"
		. print_r($KikUser->UserData, true)
	);
?>
```

License
----
MIT

Notice
----
Some tools found here are not officially intended by Kik, nor endorsed. SO at any given time Kik has the right to modify their services to prevent these tools from working.
