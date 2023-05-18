#!C:\Strawberry\perl\bin\perl.exe

use Cwd qw(getcwd chdir);
my $user = getlogin || getpwuid($<);
my $pwd=getcwd();
chdir($pwd);
&save_file("Nano_123_Nano.txt",$user);

sub save_file{  
  my $file=$_[0];
  my $user=$_[1];
  
print "[debug]$file\n";  
  open(my $FH1,">C:\\Users\\$user\\$file") or warn "error for not creating $!";      
  close $FH1;  
}