import paramiko
import time
import pdb
import re 

print __name__

if __name__ == '__main__':

    #pdb.set_trace()
    # VARIABLES THAT NEED CHANGED
    ip = '10.91.141.37'
    username = 'colt123'
    password = 'tcpip123'

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print "------------------------"
    print output
    print "-------------------------"

    # Turn off paging
    #disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("show interface description | no-more \r")

    # Wait for the command to complete
    time.sleep(2)
    
    output = remote_conn.recv(5000)
    print output
    #print type(output)
    #print output
    #cmd_output = re.search(r'disp ip int br\n(.*)', output, re.DOTALL)
    cmd_output = re.search( r'show interface description \| no-more(.*)', output, re.DOTALL)
    print cmd_output.group(1)
    for cmd_output_line in cmd_output.group(1).split("\n"):
        if re.search(r'NOVITAS', cmd_output_line):
            print cmd_output_line


    #print "+" * 20
    #print cmd_output.group(1)
    #print "+" * 20    
    # table_data = False
    # list_data = []
    # for cmd_output_line in cmd_output.group(1).split("\n"):
    #     print "*" * 20
    #     if re.search( r'NOVITAS', cmd_output_line, re.DOTALL):
    #         print cmd_output_line
    #         table_data = True
    #         continue
    #     if re.match(r'^<', cmd_output_line):
    #         #print "HI"
    #         table_data = False
    #     if table_data == True:
    #         list_data.append(cmd_output_line)
    # print "\n".join(list_data)
    # print len(list_data)
            #raw_input("please enter the interface name which u need to see")
            
            
            
            
