#!/bin/sh -- perl
eval 'exec /usr/bin/perl -S $0 ${1+"$@"}'
    if 0;

$thisprog=(split /\//,$0)[-1];

require "/www/WWW/html/rps/data/current/rpTree.hash2";

$name{'1'}='root';
$child{'1'}="2157;2;2759";

$dsp_level=2;
get_on_min_max_hash ($child{'1'}, 1);

$on_min{'2157'}=1; $on_min{'2'}=1; $on_min{'2759'}=1;
%on=%on_max;


foreach $x (keys %child) {
	if ( $x=~m/\br\d\dp\d+\b/ ) {
		$rowspan_num=0;
		$rowspan55{$x} = get_rowspan_number55 ($child{$x});
		$rowspan_num=0;
		$rowspan75{$x} = get_rowspan_number75 ($child{$x});
		$rowspan_num=0;
		$rowspan100{$x} = get_rowspan_number100 ($child{$x});
	}
}


$cell_size="<img src='/pirwww/images/empty_line.GIF' width=75 height=1>";

$table_15_head="<tr bgcolor='#dddddd'>
                    <td align=center>$cell_size<br>15</td></tr>";

$table_35_head="<tr bgcolor='#dddddd'>
                    <td align=center>$cell_size<br>15</td>
					<td align=center>$cell_size<br>35</td></tr>";
$table_55_head="<tr bgcolor='#dddddd'>
                    <td align=center>$cell_size<br>15</td>
					<td align=center>$cell_size<br>35</td>
					<td align=center>$cell_size<br>55</td></tr>";
$table_75_head="<tr bgcolor='#dddddd'>
                    <td align=center>$cell_size<br>15</td>
					<td align=center>$cell_size<br>35</td>
					<td align=center>$cell_size<br>55</td>
					<td align=center>$cell_size<br>75</td></tr>";

$table_100_head="<tr bgcolor='#dddddd'>
                    <td align=center>$cell_size<br>15</td>
					<td align=center>$cell_size<br>35</td>
					<td align=center>$cell_size<br>55</td>
					<td align=center>$cell_size<br>75</td>
					<td align=center>$cell_size<br>all</td></tr>";

foreach $x (keys %child) {
	if ( $x=~m/\br15p\d+\b/ ) {

		$nbci_id=$x; $nm_key=$x;
		if ($x=~m/r\d+p(\d+)$/) {
			  $nbci_id=$1;
			  $nm_key='p'.$nbci_id; 
		}
		$link_name0="<A HREF='/cgi-bin/textsearch.pl?field0=TAXID&query0=$nbci_id&field1=REPP&query1=NOT+NULL&search=1'>$name{$nm_key}</a>";
		$short_name=substr($name{$nbci_id},0,100);
		$title='';
		$title="title='$name{$nbci_id}'" if ( length($short_name) < length($name{$nbci_id}) );
		$link_name2="<A HREF=\$link{'TA'}$nbci_id $title>$short_name</a>";
		$ppp15="<tr><td valign=top align=center>$cell_size<br>$link_name0</td><td bgcolor='#ffffff'>PLUS</td></tr>";
		$last15{$x}.="<tr><td nowrap>$link_name2</td></tr>";
		$table_rows15{$x}=$ppp15;

		@ccc=split(/\;/,$child{$x});
		$rowspan15=$#ccc+1;
		$ppp35="<tr><td rowspan=$rowspan15 valign=top align=center>$cell_size<br>$link_name0</td>";
		foreach $c (@ccc) {
			$nbci_id=$c; $nm_key=$c;
			if ($c=~m/r35p(\d+)$/) {
				  $nbci_id=$1;
				  $nm_key='p'.$nbci_id; 
			}
			$link_name="<A HREF='/cgi-bin/textsearch.pl?field0=TAXID&query0=$nbci_id&field1=REPP&query1=NOT+NULL&search=1'>$name{$nm_key}</a>";
			$short_name=substr($name{$nbci_id},0,100);
			$title='';
			$title="title='$name{$nbci_id}'" if ( length($short_name) < length($name{$nbci_id}) );
			$link_name2="<A HREF=\$link{'TA'}$nbci_id $title>$short_name</a>";

			$ppp35.="<td valign=top align=center>$cell_size<br>$link_name</td></tr><tr>";
			$last35{$x}.="<tr><td nowrap>$link_name2</td></tr>";
			$rowspan55{$x}+=$rowspan55{$c};
			$rowspan75{$x}+=$rowspan75{$c};
			$rowspan100{$x}+=$rowspan100{$c};
		}
		$ppp35=~s/\<tr\>$//i;
		$ppp35=~s/\<\/tr\>/\<td rowspan\=$rowspan15 bgcolor='#ffffff'\>PLUSMINUS\<\/td\>\<\/tr\>/i;
		$table_rows35{$x}=$ppp35;

		$ppp55="<tr><td rowspan=$rowspan55{$x} valign=top align=center>$cell_size<br>$link_name0</td>";
		draw_to_55_tbl_row ($child{$x});
		$ppp55=~s/\<tr\>$//i;
		$ppp55=~s/\<\/tr\>/\<td rowspan\=$rowspan55{$x} bgcolor='#ffffff'\>PLUSMINUS\<\/td\>\<\/tr\>/i;
		$table_rows55{$x}=$ppp55;

		$ppp75="<tr><td rowspan=$rowspan75{$x} valign=top align=center>$cell_size<br>$link_name0</td>";
		draw_to_75_tbl_row ($child{$x});
		$ppp75=~s/\<tr\>$//i;
		$ppp75=~s/\<\/tr\>/\<td rowspan\=$rowspan75{$x} bgcolor='#ffffff'\>PLUSMINUS\<\/td\>\<\/tr\>/i;
		$table_rows75{$x}=$ppp75;

		$ppp100="<tr><td rowspan=$rowspan100{$x} valign=top align=center>$cell_size<br>$link_name0</td>";
		draw_to_100_tbl_row ($child{$x});
		$ppp100=~s/\<tr\>$//i;
		$ppp100=~s/\<\/tr\>/\<td rowspan\=$rowspan100{$x} bgcolor='#ffffff'\>MINUS\<\/td\>\<\/tr\>/i;
		$table_rows100{$x}=$ppp100;
	}
}



open (OUT,"> rps_web_12345.hash") || die "fail to write";
  print OUT "\%child=( \n"; foreach $x (keys %child) { print OUT "$x => \"$child{$x}\", \n" if ($child{$x}); } print OUT "); \n";
  print OUT "\%name=( \n"; foreach $x (keys %name) { print OUT "$x => \"$name{$x}\", \n" if ($name{$x}); } print OUT "); \n";
  print OUT "\%on=( \n"; foreach $x (keys %on) { print OUT "$x => $on{$x}, \n" if ($on{$x}); } print OUT "); \n";
  print OUT "\%on_min=( \n"; foreach $x (keys %on_min) { print OUT "$x => $on_min{$x}, \n" if ($on_min{$x}); } print OUT "); \n";

  print OUT "\%on_min2=( \n"; foreach $x (keys %on_min2) { print OUT "$x => $on_min2{$x}, \n" if ($on_min2{$x}); } print OUT "); \n";
  print OUT "\%on_min3=( \n"; foreach $x (keys %on_min3) { print OUT "$x => $on_min3{$x}, \n" if ($on_min3{$x}); } print OUT "); \n";

  print OUT "\%on_max=( \n"; foreach $x (keys %on_max) { print OUT "$x => $on_max{$x}, \n" if ($on_max{$x}); } print OUT "); \n";

  print OUT "\%on100_max=( \n"; foreach $x (keys %on100_max) { print OUT "$x => $on100_max{$x}, \n" if ($on100_max{$x}); } print OUT "); \n";
  print OUT "\%on75_max=( \n"; foreach $x (keys %on75_max) { print OUT "$x => $on75_max{$x}, \n" if ($on75_max{$x}); } print OUT "); \n";
  print OUT "\%on55_max=( \n"; foreach $x (keys %on55_max) { print OUT "$x => $on55_max{$x}, \n" if ($on55_max{$x}); } print OUT "); \n";
  print OUT "\%on35_max=( \n"; foreach $x (keys %on35_max) { print OUT "$x => $on35_max{$x}, \n" if ($on35_max{$x}); } print OUT "); \n";
  print OUT "\%on15_max=( \n"; foreach $x (keys %on15_max) { print OUT "$x => $on15_max{$x}, \n" if ($on15_max{$x}); } print OUT "); \n";

  print OUT "\%table_rows15=( \n"; foreach $x (keys %table_rows15) { print OUT "$x => \"$table_rows15{$x}\", \n" if ($table_rows15{$x}); } print OUT "); \n";
  print OUT "\%table_rows35=( \n"; foreach $x (keys %table_rows35) { print OUT "$x => \"$table_rows35{$x}\", \n" if ($table_rows35{$x}); } print OUT "); \n";
  print OUT "\%table_rows55=( \n"; foreach $x (keys %table_rows55) { print OUT "$x => \"$table_rows55{$x}\", \n" if ($table_rows55{$x}); } print OUT "); \n";
  print OUT "\%table_rows75=( \n"; foreach $x (keys %table_rows75) { print OUT "$x => \"$table_rows75{$x}\", \n" if ($table_rows75{$x}); } print OUT "); \n";
  print OUT "\%table_rows100=( \n"; foreach $x (keys %table_rows100) { print OUT "$x => \"$table_rows100{$x}\", \n" if ($table_rows100{$x}); } print OUT "); \n";


  print OUT "\%last15=( \n"; foreach $x (keys %last15) { print OUT "$x => \"$last15{$x}\", \n" if ($last15{$x}); } print OUT "); \n";
  print OUT "\%last35=( \n"; foreach $x (keys %last35) { print OUT "$x => \"$last35{$x}\", \n" if ($last35{$x}); } print OUT "); \n";
  print OUT "\%last55=( \n"; foreach $x (keys %last55) { print OUT "$x => \"$last55{$x}\", \n" if ($last55{$x}); } print OUT "); \n";
  print OUT "\%last75=( \n"; foreach $x (keys %last75) { print OUT "$x => \"$last75{$x}\", \n" if ($last75{$x}); } print OUT "); \n";
  print OUT "\%last100=( \n"; foreach $x (keys %last100) { print OUT "$x => \"$last100{$x}\", \n" if ($last100{$x}); } print OUT "); \n";


  print OUT "\$table_15_head=\"$table_15_head\"; \n";
  print OUT "\$table_35_head=\"$table_35_head\"; \n";
  print OUT "\$table_55_head=\"$table_55_head\"; \n";
  print OUT "\$table_75_head=\"$table_75_head\"; \n";
  print OUT "\$table_100_head=\"$table_100_head\"; \n";

  print OUT "1; \n";
close OUT;

exit;

##########################
sub draw_to_55_tbl_row {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		$rowspan='';
		$rowspan="rowspan=$rowspan55{$_}" if ($rowspan55{$_}>1);
		$cell_data='&nbsp;';
		$cell_data=$_ if ($_);

		$nbci_id=$_; $nm_key=$_;
		if ($_=~m/r\d+p(\d+)$/) {
			  $nbci_id=$1;
			  $nm_key='p'.$nbci_id; 
		}
		$link_name="<A HREF='/cgi-bin/textsearch.pl?field0=TAXID&query0=$nbci_id&field1=REPP&query1=NOT+NULL&search=1'>$name{$nm_key}</a>";
		$short_name=substr($name{$nbci_id},0,100);
		$title='';
		$title="title='$name{$nbci_id}'" if ( length($short_name) < length($name{$nbci_id}) );
		$link_name2="<A HREF=\$link{'TA'}$nbci_id $title>$short_name</a>";
		$ppp55.="<td $rowspan valign=top align=center>$cell_size<br>$link_name</td>";
		if ($_=~/\br55p\d+\b/) {
			$last55{$x}.="<tr><td nowrap>$link_name2</td></tr>";
			$ppp55.="</tr><tr>";
		} elsif ($child{$_}=~/\br55p\d+\b/ || $child{$_}=~/\br35p\d+\b/) {
			draw_to_55_tbl_row ($child{$_});
		}
	}
}
##########################
sub draw_to_75_tbl_row {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		$rowspan='';
		$rowspan="rowspan=$rowspan75{$_}" if ($rowspan75{$_}>1);
		$cell_data='&nbsp;';
		$cell_data=$_ if ($_);
		$nbci_id=$_; $nm_key=$_;
		if ($_=~m/r\d+p(\d+)$/) {
			  $nbci_id=$1;
			  $nm_key='p'.$nbci_id; 
		}
		$link_name="<A HREF='/cgi-bin/textsearch.pl?field0=TAXID&query0=$nbci_id&field1=REPP&query1=NOT+NULL&search=1'>$name{$nm_key}</a>";
		$short_name=substr($name{$nbci_id},0,100);
		$title='';
		$title="title='$name{$nbci_id}'" if ( length($short_name) < length($name{$nbci_id}) );
		$link_name2="<A HREF=\$link{'TA'}$nbci_id $title>$short_name</a>";
		$ppp75.="<td $rowspan valign=top align=center>$cell_size<br>$link_name</td>";
		if ($_=~/\br75p\d+\b/) {
			$last75{$x}.="<tr><td nowrap>$link_name2</td></tr>";
			$ppp75.="</tr><tr>";
		} elsif ($child{$_}=~/\br\d\dp\d+\b/) {
			draw_to_75_tbl_row ($child{$_});
		}
	}
}
##########################
sub draw_to_100_tbl_row {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		$rowspan='';
		$rowspan="rowspan=$rowspan100{$_}" if ($rowspan100{$_}>1);
		$cell_data='&nbsp;';
		$cell_data=$_ if ($_);


		$nbci_id=$_; $nm_key=$_;
		if ($_=~m/^\d+$/) {
			$nm_key='p'.$nbci_id;
		}elsif ($_=~m/r\d+p(\d+)$/) {
			  $nbci_id=$1;
			  $nm_key='p'.$nbci_id; 
		}
		$link_name="<A HREF='/cgi-bin/textsearch.pl?field0=TAXID&query0=$nbci_id&field1=REPP&query1=NOT+NULL&search=1'>$name{$nm_key}</a>";
		$short_name=substr($name{$nbci_id},0,100);
		$title='';
		$title="title='$name{$nbci_id}'" if ( length($short_name) < length($name{$nbci_id}) );
		$link_name2="<A HREF=\$link{'TA'}$nbci_id $title>$short_name</a>";
		$ppp100.="<td $rowspan valign=top align=center>$cell_size<br>$link_name</td>";
		if (!$child{$_}) {
			$last100{$x}.="<tr><td nowrap>$link_name2</td></tr>";
			$ppp100.="</tr><tr>";
		} else {
			draw_to_100_tbl_row ($child{$_});
		}
	}
}
#######################
sub get_rowspan_number55 {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		if ($_=~/\br55p\d+\b/) {
			$rowspan_num++ ;
		} elsif ($child{$_}=~/\br55p\d+\b/) {
			get_rowspan_number55 ($child{$_});
		}
	}
	return $rowspan_num;
}
#######################
sub get_rowspan_number75 {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		if ($_=~/\br75p\d+\b/) {
			$rowspan_num++ ;
		} elsif ($child{$_}=~/\br75p\d+\b/) {
			get_rowspan_number75 ($child{$_});
		}
	}
	return $rowspan_num;
}
#######################
sub get_rowspan_number100 {
	my @abc=split(/\;/,$_[0]);
	foreach (@abc) {
		if (!$child{$_}) {
			$rowspan_num++ ;
		} else {
			get_rowspan_number100 ($child{$_});
		}
	}
	return $rowspan_num;
}


#######################
sub get_on_min_max_hash {
	my @abc=split(/\;/,$_[0]);
	my $branch=$_[1];
	foreach (@abc) {
		undef $on_min{$_};
		$on_min{$_}=1 if ($branch<$dsp_level);

		$on_min2{$_}=1 if ($branch<2);
		$on_min3{$_}=1 if ($branch<3);

		$on_max{$_}=1;

		$on15_max{$_}=1  if ($_=~/^r15p\d+/);
		$on35_max{$_}=1  if ($_=~/^r15p\d+/);
		$on55_max{$_}=1  if ($_=~/^r15p\d+/);
		$on75_max{$_}=1  if ($_=~/^r15p\d+/);
		$on100_max{$_}=1 if ($_=~/^r15p\d+/);
		get_on_min_max_hash ($child{$_}, $branch+1);
	}
}



