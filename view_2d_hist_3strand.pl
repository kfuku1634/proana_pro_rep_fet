#! /usr/bin/perl -w

$file            = $ARGV[0];
$n_strand_min    = 1;
$n_strand_max    = 100;
$cutoff_n_loop   = 50;

$switch = 1;

open(IN, "$file");


$sign_hash{"+-+"} = 1;	   $sign_rev[1]="+-+";
$sign_hash{"++-"} = 2;	   $sign_rev[2]="++-";
$sign_hash{"+--"} = 3;	   $sign_rev[3]="+--";
$sign_hash{"+++"} = 4;	   $sign_rev[4]="+++";


$order_hash{"123"} =  1;  $order_rev[ 1] = "123";
$order_hash{"132"} =  2;  $order_rev[ 2] = "132";
$order_hash{"213"} =  3;  $order_rev[ 3] = "213";



for($i=1; $i<=3; $i++){
  for($j=1; $j<=4; $j++){
    $histogram[$i][$j] = 0;
  }
}

while(<IN>){

  chomp($_);
  @words = split(/\s+/, $_);


  $scop_id  = $words[ 0];
  $n_strand = $words[ 1];
  $sign     = $words[ 2];
  $order    = $words[ 3];

  $loop_len[1] = $words[10];
  $loop_len[2] = $words[11];


  $r_weight = $words[16];

#       0    1    2    3      4         5         6     7   8 9   10 11         12       13      14          15  16      17
# d12asa_    8  ++-  123  Motif      Open     b-a-b b-c-b   p a   26 33   166-169, 196-199, 233-240   d.104.1.1  80    0.06

  $weight = 1.0 / $r_weight;

  $loop_max = $loop_len[1];
  for($i=2; $i<=2; $i++){
      if($loop_max < $loop_len[$i]){
	  $loop_max = $loop_len[$i];
      }
  }

  $keyword = $scop_id .  $sign . $order;

  if(     ($n_strand <=  $n_strand_max)
      and ($n_strand >=  $n_strand_min)
      and ($loop_max <= $cutoff_n_loop )){


    if( exists( $hist{$keyword} ) ){
      $hist{$keyword}  += 1;
      $histogram[ $order_hash{$order} ][ $sign_hash{$sign}] += $weight;
    }
    else{
      $hist{$keyword}  = 1;
      $histogram[ $order_hash{$order} ][ $sign_hash{$sign}] += $weight;
    }
  }

#    0      1    2    3          4        5      6          7        8        9         10         11
#d12asa_    +-+  123  Motif      Open     b-c-b  b-c-b      196-199, 233-240, 245-254   d.104.1.1  80

#  print "$_\n";
#  print "$sign ($sign_hash{$sign}) $order ($order_hash{$order}) \n";




}# end of while



####################################
if($switch eq 1){

print "      ";
for($i=1; $i<=3; $i++){
    printf("%6s ",$order_rev[$i]);
}
  print "\n";
printf "--------------------------\n";


for($j=1; $j<=4; $j++){
    printf("%5s ",$sign_rev[$j]);
  for($i=1; $i<=3; $i++){
      printf("%6.1f ", $histogram[$i][$j]);
  }
  print "\n";
}
}

####################################
elsif($switch eq 2){
    print "$n_strand_max ";
for($j=1; $j<=4; $j++){
  for($i=1; $i<=3; $i++){
      printf("%6.1f ", $histogram[$i][$j]);
  }
}
  print "\n";

}

####################################
elsif($switch eq 3){
  $tot = 0;
  for($j=1; $j<=4; $j++){
    for($i=1; $i<=3; $i++){
      $tot+= $histogram[$i][$j];
    }
  }

  print "$n_strand_max ";
  for($j=1; $j<=4; $j++){
    for($i=1; $i<=3; $i++){
      printf("%6.1f ", $histogram[$i][$j]/$tot * 100);
    }
  }
  print "\n";
}


####################################
elsif($switch eq 4){
  print "$n_strand_max ";


  for($j=1; $j<=4; $j++){
    for($i=1; $i<=3; $i++){
	$tot = 1;
	if( ($i eq 2) and ($j eq 1) ){ $tot = $histogram[2][1] + $histogram[3][1]; }
	if( ($i eq 3) and ($j eq 1) ){ $tot = $histogram[3][1] + $histogram[2][1]; }

	if( ($i eq 2) and ($j eq 2) ){ $tot = $histogram[2][2] + $histogram[3][3]; }
        if( ($i eq 3) and ($j eq 3) ){ $tot = $histogram[3][3] + $histogram[2][2]; }

	if( ($i eq 1) and ($j eq 2) ){ $tot = $histogram[1][2] + $histogram[1][3]; }
	if( ($i eq 1) and ($j eq 3) ){ $tot = $histogram[1][3] + $histogram[1][2]; }

	if( ($i eq 2) and ($j eq 4) ){ $tot = $histogram[2][4] + $histogram[3][4]; }
	if( ($i eq 3) and ($j eq 4) ){ $tot = $histogram[3][4] + $histogram[2][4]; }

	if( ($i eq 2) and ($j eq 3) ){ $tot = $histogram[2][3] + $histogram[3][2]; }
        if( ($i eq 3) and ($j eq 2) ){ $tot = $histogram[3][2] + $histogram[2][3]; }

    printf("%6.1f ", $histogram[$i][$j]/$tot * 100);
    }
  }
  print "\n";
}


####################################
if($switch eq 5){
  $tot = 0;
  for($j=1; $j<=4; $j++){
    for($i=1; $i<=3; $i++){
      $tot+= $histogram[$i][$j];
    }
  }

print "      ";
for($i=1; $i<=3; $i++){
    printf("%6s ",$order_rev[$i]);
}
  print "\n";
printf "--------------------------\n";


for($j=1; $j<=4; $j++){
    printf("%5s ",$sign_rev[$j]);
  for($i=1; $i<=3; $i++){
      printf("%6.1f ", $histogram[$i][$j]/$tot*100);
  }
  print "\n";
}
}
