# Generating and adding certificates to trust store

0. Rather than following steps 1-2, you can use the following one-liner to generate the key and certificate:

```bash
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
  -keyout server.key -out server.crt -subj "/CN=nanosexample.com" \
  -addext "subjectAltName=DNS:nanosexample.com,DNS:*.nanosexample.com"
```
This command generates a new RSA key and a self-signed certificate with a validity of 365 days. The `-nodes` option means that the private key will not be encrypted (it won't ask  you for a 4-char password, that's my understanding). The `-subj` option specifies the subject name for the certificate, and the `-addext` option adds the Subject Alternative Name (SAN) extension to the certificate.

Got the approach from [here](https://stackoverflow.com/questions/10175812/how-can-i-generate-a-self-signed-ssl-certificate-using-openssl/41366949#41366949)

1. Generate the server.key file using

```bash
openssl genrsa -out server.key 2048
```

2. Generate the server.crt file using (this is for self-signed certificate)

```bash
openssl req -x509 -new -key server.key -out server.crt -days 365
```

Note: You can also rather generate a certificate signing request (CSR) and get it signed by a trusted CA. This is the recommended approach for production environments.

Example command for generating a CSR:

```bash
(venv) nano@DESKTOP-TEN39M0:~/k8splayground/ui-auth/ui-service$ openssl req -x509 -new -key server.key -out server.crt -days 365
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:IN
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:NanosOrg
Organizational Unit Name (eg, section) []:NanosApp
Common Name (e.g. server FQDN or YOUR name) []:nanosexample.com
Email Address []:.
```

3. Copy the certificate into windows

```bash
cp server.crt /mnt/c/Users/Ubaid/Desktop/cert
```

4. Now open your certificate in windows explorer, right click and select install certificate. Use the option of installing it in personal store. Then press `windows + R` and type `certmgr.msc` to open the certificate manager. You should see your certificate in the personal store. Now you need to right click copy and paste it in the trusted root certification authorities store. This will make your certificate trusted by the system.

5. Now, you also need to define your domain in the hosts file. Open the hosts file in `C:\Windows\System32\drivers\etc\hosts` and add the following line:

```bash
# Custom entries
127.0.0.1 nanosexample.com
```

You will need to run powershell as administrator, cd to the above mentioned directory and run the following command to edit the hosts file:

```bash
notepad hosts
```

6. Now you can run your server using the following command:

```bash
python main.py
```

7. Open `https://nanosexample.com:5000` in your browser. You should see the server running with the self-signed certificate. You should see the certificate as trusted in the browser.
