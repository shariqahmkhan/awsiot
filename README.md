# awsiot

> this repository is to help you send messages to aws iot core with detailed steps, follow step by step
> this guide assumes you already have aws account

### step 1: configuring aws iot core
1. click on services and select iot core
2. on the left panel it shows monitor, onboard, manage ...
3. click on manage -> things -> create (top right) -> create single new thing -> give suitable name -> Next
4. select create certificate and download all certificatess except public key (which isnt useful for connection)
5. Below you will see root CA for AWS IoT -> click download (it redirects you to secure CA) -> click on Amazon Root CA 1
6. right click and save it by the same name as it displays
7. Go back to from where you downloaded the certificates -> click activate
8. Click attach policy <br>
(if you already have created policy then select one of them and click <b> register thing </b>)<br>
(if you havent done it, then simply click <b> register thing </b>
9. Go to <b> secure</b> tab in left panel -> click policies -> create -> give suitable name 
10. under add statements -> under action -> write iot:* -> under resource arn -> write * -> check allow (under effect)
11. click create.
12. now go back to where you create a thing (i.e., things under manage in side panel) -> select the thing -> go to security -> select the certificate
13. top right click on actions -> <b>attach policy</b> -> select the policy -> click attach

#### Now your aws is ready for getting data

### step 2: Code implementation
<a href = "https://github.com/shariqkhan29/awsiot/blob/master/awsiot.py">Click here </a>

#### Note
: put all certificates to certificates folder and edit their extensions as shown in code above
: the code is present in the same directory as that of certificates or vice versa and hence the path c://users has not been added
#### end for now

