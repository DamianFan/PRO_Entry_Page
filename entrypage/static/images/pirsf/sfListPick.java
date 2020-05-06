///////////////////////////////////////////////////////////////////////////
//      Program Name: sfListPick.java=sfJun2502.java                     //
//      Created Date: 10/22/2001                                         //
//     Modified Date: 08/25/2002                                         //
//          function: display protein supperfamily members and their     //
//                    domains/motif with position in sequence            //
//       Data Source: direct from its parent's web page                  //
//            Author: Jian Zhang                                         //
///////////////////////////////////////////////////////////////////////////
import java.awt.*;
import java.util.*;
import java.applet.*;

public class sfListPick extends Applet {

    public int seqLong, domNum, partsNum, seqBarWidth, domBarWidth, barDist, 
		       lineDist, lastLine, longestId, legendUpY00, farestId, newDomNum,
		        seqBarLong,  seqNum,  y0,  x0, 
				seqBarLong0, seqNum0, y00, x00,
				seqHasOverlayDom[],  domOverlay[][],  dom[][][],  domCol[][],  ddd2[],
				seqHasOverlayDom0[], domOverlay0[][], dom0[][][], domCol0[][], ddd20[],

		        ddd0[], downI0[], downJ0[], downK0[], downX0[], downY0[], seqNameUp0[], legend[][],
				ccc, moveArea, test1, test2, upDown, leftGo, strCmpr,  xPoint, displayPage, keepIdx, charIdx;
	private String sfid, sfname, sfId[], sfId0[], sfName[], sfName0[],
		        seq[],  seqId[],  seqName[],  domId[][],  dName[][], 
	            seq0[], seqId0[], seqName0[], domId0[][], dName0[][],
				domIdTest, domIdDown, test0, seqTest[];
    double dotWidth, dotWidth0;
    Font f1, f2, f3;
	private Image img[],img0[], imgbb, imgMag, leftImg, rightImg, upImg, downImg, imgReload,
		      showMe, qMark, fingerUp, fingerDown, refImg, imgZoomin, imgZoomout;
    private boolean mouseDown, test3[], test3M[];
	 Canvas0 cv0;
	 Canvas1 cv1;
	 Canvas2 cv2;
	 Canvas3 cv3;
    public void init() 
    {
	    f1=new Font ("Courier", Font.BOLD,  14);
	    f2=new Font ("Times", Font.PLAIN, 10);
		f3=new Font ("Courier", Font.PLAIN,  24);

        processHTML();
	    setLayout( null );
        cv0 = new Canvas0();
		cv1 = new Canvas1();
		cv2 = new Canvas2();
		cv3 = new Canvas3();

	    add(cv0);
		add(cv1);
		add(cv2);
		add(cv3);
		cv0.reshape( 85, 52, 755, 518 );
		cv1.reshape( 5, 2, 845, 50 );
		cv2.reshape( 2, 52, 84, 518 );
		cv3.reshape( 844, 52, 10, 518 );
	    setBackground(Color.white);


//		img=new Image [60];
//		for (int i=1; i<=60; i++)
//		{
//             img[i-1]  =getImage (getCodeBase(), "a" + i + ".gif");
//		}


		imgbb =getImage (getCodeBase(), "bb.gif");
		imgMag =getImage (getCodeBase(), "magnify.gif");
		leftImg =getImage (getCodeBase(), "leftArrow.gif");
		rightImg =getImage (getCodeBase(), "rightArrow.gif");
		upImg =getImage (getCodeBase(), "upArrow.gif");
		downImg =getImage (getCodeBase(), "downArrow.gif");
		showMe =getImage (getCodeBase(), "showMe.gif");
		qMark =getImage (getCodeBase(), "pointHand.gif");
		fingerUp =getImage (getCodeBase(), "fingerUp.gif");
		fingerDown =getImage (getCodeBase(), "fingerDown.gif");
		refImg =getImage (getCodeBase(), "refresh.gif");
		imgZoomin =getImage (getCodeBase(), "zoomin.gif");
		imgZoomout =getImage (getCodeBase(), "zoomout.gif");
		imgReload =getImage (getCodeBase(), "reload.gif");

		setBarColor();
	    seqHasOverlayDom=new int [seqNum];
	    seqHasOverlayDom0=new int [seqNum];
	    domOverlay=new int [seqNum][domNum];
	    domOverlay0=new int [seqNum][domNum];
		legend=new int [seqNum][domNum];

		keepIdx=0;
		upDown=0;
		strCmpr=0;
		y00=12;
		x00=0;
		seqBarLong=700;
        y0=y00;
		x0=x00;
		domBarWidth=8;
		seqBarWidth=6;
		barDist=0;
		lineDist=domBarWidth*3+40-30;
		dotWidth=(double)seqBarLong/seqLong;
		dotWidth0=(double)seqBarLong/seqLong;
		drawLegend();

        int ii=0;
		img=new Image [newDomNum+1];
		for (int i=1; i<=newDomNum+1; i++)
		{
			if (ii>=60)
			{
				ii=0;
			}
			ii=ii+1;
            img[i-1]  =getImage (getCodeBase(), "a" + ii + ".gif");
		}

		testOverlay();
	    initCV();
	}
	public void processHTML()
	{
	   sfid=getParameter("sfid");
	   sfname=getParameter("sfname");
	   seqLong=Integer.parseInt(getParameter("seqLong"));
	   seqNum=Integer.parseInt(getParameter("seqNum"));
	   seqNum0=Integer.parseInt(getParameter("seqNum"));
	   seq=new String [seqNum];
	   seq0=new String [seqNum];

	   sfId=new String [seqNum];
	   sfId0=new String [seqNum];
	   sfName=new String [seqNum];
	   sfName0=new String [seqNum];

	   seqTest=new String [seqNum];
	   seqId=new String [seqNum];
	   seqId0=new String [seqNum];
	   seqName=new String [seqNum];
	   seqName0=new String [seqNum];

	   String seqArr, seqIdArr, seqNameArr, domArr, dNameArr, sfIdArr, sfNameArr;

	   domNum=Integer.parseInt(getParameter("largestInSeqDomNum"));
	   partsNum=Integer.parseInt(getParameter("largestInDomParts"));
	   dom = new int [seqNum][domNum][partsNum];
	   dom0 = new int [seqNum][domNum][partsNum];
	   domCol=new int [seqNum][domNum];
	   domCol0=new int [seqNum][domNum];
	   domId=new String [seqNum][domNum];
	   domId0=new String [seqNum][domNum];
	   dName=new String [seqNum][domNum];
	   dName0=new String [seqNum][domNum];
       test3=new boolean [seqNum];
	   ddd0= new int [seqNum];
	   ddd2= new int [seqNum];
	   ddd20= new int [seqNum];
	   downI0= new int [seqNum];
	   downJ0= new int [seqNum];
	   downK0= new int [seqNum];
	   downX0= new int [seqNum];
	   downY0= new int [seqNum];
       String si, dj, pk;
	   for (int i=0; i<seqNum; i++)
	   {
          seqArr="seq";
		  seqIdArr="seqId";
		  seqNameArr="seqName";
	      si=Integer.toString(i);
          seqArr=seqArr.concat(".");
	      seqArr=seqArr.concat(si);
          seqIdArr=seqIdArr.concat(".");
		  seqIdArr=seqIdArr.concat(si);
          seqNameArr=seqNameArr.concat(".");
		  seqNameArr=seqNameArr.concat(si);
		  seq[i]=getParameter(seqArr);

		  seq0[i]=getParameter(seqArr);
		  seqId[i]=getParameter(seqIdArr);
		  seqId0[i]=getParameter(seqIdArr);
		  seqName[i]=getParameter(seqNameArr);
		  seqName0[i]=getParameter(seqNameArr);


		  sfIdArr="sfId";
		  sfIdArr=sfIdArr.concat(".");
		  sfIdArr=sfIdArr.concat(si);
		  sfId[i]=getParameter(sfIdArr);
		  sfId0[i]=getParameter(sfIdArr);

		  sfNameArr="sfName";
		  sfNameArr=sfNameArr.concat(".");
		  sfNameArr=sfNameArr.concat(si);
		  sfName[i]=getParameter(sfNameArr);
		  sfName0[i]=getParameter(sfNameArr);

	      for (int j=0; j<domNum; j++)
	   	    for (int k=0; k<partsNum; k++)
			{
		       domArr="dom";
		       dNameArr="dName";
			   dj=Integer.toString(j);
               pk=Integer.toString(k);
               domArr=domArr.concat(".");
			   domArr=domArr.concat(si);
               domArr=domArr.concat(".");
			   domArr=domArr.concat(dj);
               domArr=domArr.concat(".");
               domArr=domArr.concat(pk);
               dNameArr=dNameArr.concat(".");
			   dNameArr=dNameArr.concat(si);
			   dNameArr=dNameArr.concat(".");
			   dNameArr=dNameArr.concat(dj);
			   if (k==0)
			   {
				  domId[i][j]=getParameter(domArr);
				  domId0[i][j]=getParameter(domArr);
				  dName[i][j]=getParameter(dNameArr);
				  dName0[i][j]=getParameter(dNameArr);
			   }
			   else if (getParameter(domArr)!=null)
			   {
                  dom[i][j][k]=Integer.parseInt(getParameter(domArr));
				  dom0[i][j][k]=Integer.parseInt(getParameter(domArr));
			   }
			   else if (getParameter(domArr)==null && k!=0)
				  k=partsNum;
			}
	   }
	}
    public void paint( Graphics g )
    {
		drawLargeFrame(g);
	}
	public void drawLargeFrame(Graphics g)
	{
		g.setColor(Color.black);
		g.drawLine(1,1,854,1);
		g.drawLine(1,1,1,585);
		g.drawLine(1,585,854,585);
		g.drawLine(854,1,854,585);
	}
    public void initCV()
	{
		 cv0.setValue(seqLong,seqNum,seq,seqId,seqName,domNum,partsNum,dom,domCol,sfId,sfName,
			          domId,dName,img,ddd2,domOverlay,y0,x0,longestId,
				      domBarWidth,seqBarWidth,barDist,lineDist,dotWidth,leftImg,rightImg,upImg,downImg,imgbb);
		 cv1.setValue(seqNum,sfid,sfname,seqLong,dotWidth,imgReload,
			          imgMag,showMe,qMark,fingerUp,fingerDown,refImg, imgZoomin, imgZoomout);
		 cv2.setValue(seqNum,seqId,seqName,ddd2,y0,sfId,domId,domNum,
			          domBarWidth,seqBarWidth,barDist,lineDist,upImg,downImg,leftImg,lastLine);
		 cv3.setValue(seqNum, upImg, downImg, rightImg);
	}

    public void drawLegend()
	{
	   for (int i=0; i<seqNum; i++)
	       for (int j=0; j<domNum; j++)
		       legend[i][j]=0;

       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
		       if (domId[i][j] !=null)
			   {
			       if (legend[i][j]!=-1)
				   {
			          for (int a=0; a<seqNum; a++)
					  {
				         for (int b=0; b<domNum; b++)
						 {
		                     if (domId[a][b] !=null && domId[i][j].compareTo(domId[a][b])==0)
							 {
						        if (legend[i][j]!=1)
					                legend[i][j]=1;
					            else
						            legend[a][b]=-1;
							 }
						 }
					  }
				   }
			   }
		   }
	   }
       legend[0][0]=1;
       ///order domId ///
       longestId=0;
	   farestId=0;
       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
		       if (domId[i][j] !=null && legend[i][j]>=1)
			   {
				   if (longestId<domId[i][j].length()+dName[i][j].length())
					   longestId=domId[i][j].length()+dName[i][j].length();
		 	       for (int a=0; a<seqNum; a++)
				   {
				       for (int b=0; b<domNum; b++)
					   {
		                  if (domId[a][b] !=null && domId[i][j].compareTo(domId[a][b])>0 && legend[a][b]>=1)
					      legend[i][j]=legend[i][j]+1;
					   }
				   }
				   if (farestId<legend[i][j])
					   farestId=legend[i][j];
			   }
		   }
	   }

	   legendUpY00=(farestId+1)*15+12;
	   y00=legendUpY00;
	   //y0=y00;


	   //if (newDomNum>0)
       //y00=y00-(-farestId+newDomNum)*15;

       newDomNum=farestId;

	}

    public void setBarColor()
    {
		domCol[0][0]=0;
        for (int i=0; i<seqNum; i++)
		{
			for (int j=0; j<domNum; j++)
			{
			    domIdTest=domId[i][j];
				for (int u=0; u<seqNum; u++)
					for (int v=0; v<domNum; v++)
					    if (domId[u][v]!=null)
						{
							if (domId[u][v].equals(domIdTest))
							{
							    domCol[i][j]=domCol[u][v];
								domCol0[i][j]=domCol[u][v];
								u=seqNum;
								v=domNum;
							}
						    else domCol[i][j]=200;
						} else domCol[u][v]=100;
				if (domCol[i][j]==200 & domId[i][j]!=null)
				{
					domCol[i][j]=ccc+1;
					domCol0[i][j]=ccc+1;
				    ccc++;
				}
			}
		}
	}
	public void testOverlay()
	{
        for (int i=0; i<seqNum; i++)
		{
			test3[i]=false;
			if (domId[i][0]!=null)
			{
				for (int j=0; j<domNum; j++)
				{
					if (domId[i][j]!=null)
                        if ( domId[i][j].startsWith("PCM") )
						    domOverlay[i][j]=-1;
					for (int k=1; k<=(dom[i][j].length-1)/2; k++)
					{
						test1=dom[i][j][k*2-1];  test2=dom[i][j][k*2];
						for (int m=0; m<j; m++)
						{
							for (int n=1; n<=(dom[i][m].length-1)/2; n++)
							{
                                if (   (test1<=dom[i][m][n*2-1] && test2>dom[i][m][n*2-1])
									|| (test1<=dom[i][m][n*2] && test2>dom[i][m][n*2]) 
									|| (test1>dom[i][m][n*2-1] && test2<dom[i][m][n*2]) )
								{
									if ( domId[i][j].startsWith("PF") && domId[i][m].startsWith("PF") )
									{
									    if (domOverlay[i][j]<=domOverlay[i][m])
										{
										    domOverlay[i][j]=domOverlay[i][m]+1;
										    domOverlay0[i][j]=domOverlay[i][j];
										}
									    if (seqHasOverlayDom[i]<=domOverlay[i][j])
										    seqHasOverlayDom[i]=domOverlay[i][j];
										test3[i]=true;
									}
									if ( domId[i][j].startsWith("PC") && domId[i][m].startsWith("PC") )
									{
									 
									    if (domOverlay[i][j]>=domOverlay[i][m])
										{
										    domOverlay[i][j]=domOverlay[i][m]-1;
										    domOverlay0[i][j]=domOverlay[i][j];
										}
										test3[i]=true;
									}
								}
							}
						}
					}
				}
			}
			if (test3[i]==false)
				seqHasOverlayDom[i]=0;
			seqHasOverlayDom0[i]=seqHasOverlayDom[i];
			ddd2[i]=(domBarWidth+barDist)*seqHasOverlayDom[i];
			ddd20[i]=(domBarWidth+barDist)*seqHasOverlayDom[i]-0;
		}
///////////////////////////////////////////////////
		for (int i=0; i<seqNum; i++)
			if (i>0)
				y0+=ddd2[i-1];
		lastLine=(int)(y0+(seqNum-1)*lineDist+seqBarWidth+(ddd2[seqNum-1]+barDist+domBarWidth));
		y0=y00; 
///////////////////////////////////////////////////
	}
    public boolean handleEvent( Event e )
    {
        if ( e.target instanceof Canvas1 )
		{
			if (cv1.mouseDown==true & cv1.legendClick==1)
			{
				seqNum=cv2.seqNum;
				if(cv0.legendUp==true)
				{
					 
					 drawLegend();
					 y00=12;
					 //cv1.legendUp=false;
					 cv0.legendUp=false;
				} else
				{
					drawLegend();
					//cv1.legendUp=true;
					y0=y00;
					cv0.legendUp=true;
					cv0.newDomNum=newDomNum;
				}
				cv1.strCmpr=1;
			    cv1.leftRight=0;
			    cv1.x0=0;
                cv1.clearDetail=1;
			    cv1.legendClick=0;
			}
			if (cv1.mouseDown==true & cv1.reload==1)
			{
				cv1.reload=0;
				cv0.legendUp=true;
				cv1.legendUp=true;
				cv2.legendUp=true;
				cv1.mouseDown=false;
				cv3.leftShow=0;
				cv2.rightShow=0;
				cv2.downShow=0;
				showStatus("Reload");
				cv0.dotWidth=dotWidth0;
				cv1.dotWidth=dotWidth0;
				cv1.leftRight=0;
				seqNum=seqNum0;
				cv0.seqNum=seqNum0;
				cv1.seqNum=seqNum0;
				cv2.seqNum=seqNum0;
				cv0.strCmpr=1;
				upDown=0;

				cv0.x0=x0; 
				cv0.iii=0;
				cv2.iii=0;
				cv0.domIdDown="";
				cv0.displayPage=1;
				for (int i=0; i<seqNum0; i++)
				{
                    cv2.seqNameUp[i]=0;
					cv0.seqNameUp[i]=0;
					cv2.sfNameUp[i]=0;
					cv0.sfNameUp[i]=0;
					cv0.ddd[i]=0;
					cv0.ddd2[i]=ddd20[i];
					cv0.downX[i]=0;
					cv0.downY[i]=0;
					cv0.downI[i]=0;
					cv0.downJ[i]=0;
					cv0.downK[i]=0;
					cv0.start80X[i]=0;
					seq[i]=seq0[i];
					seqId[i]=seqId0[i];
					seqName[i]=seqName0[i];
					sfId[i]=sfId0[i];
					sfName[i]=sfName0[i];
					cv2.leftGoIdx[i]=0;
					seqHasOverlayDom[i]=seqHasOverlayDom0[i];
				//	group[i]=group0[i];
					for (int j=0; j<cv0.domNum; j++)
					{
						domId[i][j]=domId0[i][j];
						dName[i][j]=dName0[i][j];
						domCol[i][j]=domCol0[i][j];
						domOverlay[i][j]=domOverlay0[i][j];
						for (int k=cv0.partsNum-1; k>0; k--)
							dom[i][j][k]=dom0[i][j][k];
					}
				}

				cv0.newDomNum=0;
				drawLegend();
				testOverlay();
				initCV();

				cv0.repaint();
				cv1.repaint();
				cv2.repaint();
				cv3.repaint();

			}
			if (cv1.mouseDown==true & cv1.clearDetail==1)
			{
				cv1.clearDetail=0;
				cv3.leftShow=0;
				cv2.rightShow=0;
				cv2.downShow=0;

				cv1.mouseDown=false;
				showStatus("clean");
				cv0.dotWidth=dotWidth0;
				cv1.dotWidth=dotWidth0;
				cv1.leftRight=0;
			//	cv0.seqNum=seqNum0;
			//	cv2.seqNum=seqNum0;
				cv0.strCmpr=1;
				cv0.y0=y00;
				cv0.y00=y00;
				cv2.y00=y00;
				cv0.x0=x0;

				cv0.iii=0;
				cv2.iii=0;
				cv0.domIdDown="";
				cv0.displayPage=1;
				for (int i=0; i<seqNum0; i++)
				{
					cv0.ddd[i]=0;
				//	cv0.ddd2[i]=ddd20[i];
					cv0.downX[i]=0;
					cv0.downY[i]=0;
					cv0.downI[i]=0;
					cv0.downJ[i]=0;
					cv0.downK[i]=0;
					cv0.start80X[i]=0;

                    cv2.seqNameUp[i]=0;
					cv0.seqNameUp[i]=0;
					cv2.sfNameUp[i]=0;
					cv0.sfNameUp[i]=0;

				}
				upDown=0;
				strCmpr=0;
				cv2.repaint();
				cv0.repaint();
				cv1.repaint();
				cv3.repaint();
			}
			if (cv1.mouseDown==true & cv1.stretch==1) // & (cv0.dotWidth<=2 || cv0.dotWidth<dotWidth0))
			{
				cv1.stretch=0;
				cv1.mouseDown=false;
				showStatus("Sequence Stretched");
				cv0.x0=0;
				cv1.leftRight=0;
				cv0.dotWidth*=2;
				cv1.dotWidth*=2;
				for (int i=0; i<cv0.seqNum; i++)
				{
					cv0.ddd[i]=0;
					cv0.downX[i]=0;
					cv0.start80X[i]=0;
					cv0.downY[i]=0;
				 // cv0.downX[i]=(int)(cv0.downX[i]*2);
				//	cv0.start80X[i]=(int)((cv0.start80X[i]+40*7)*2)-40*7;
				}
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				cv2.rightShow=0;
				cv0.repaint();
				cv1.repaint();
				cv2.repaint();
				cv3.repaint();
			}
			if (cv1.mouseDown==true & cv1.sclBack==1) // & (cv0.dotWidth>=0.2 || cv0.dotWidth>dotWidth0))
			{
				cv1.sclBack=0;
				cv1.mouseDown=false;
				showStatus("Scale Back");
				cv0.x0=0;
				cv1.leftRight=0;
				cv0.dotWidth/=2;
				cv1.dotWidth/=2;
				for (int i=0; i<cv0.seqNum; i++)
				{
					cv0.ddd[i]=0;
					cv0.downX[i]=0;
					cv0.downY[i]=0;
					cv0.start80X[i]=0;
					//cv0.downX[i]=(int)(cv0.downX[i]/2);
					//cv0.start80X[i]=(int)((cv0.start80X[i]+40*7)/2)-40*7;
				}
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				cv2.rightShow=0;
				cv0.repaint();
				cv2.repaint();
				cv1.repaint();
				cv3.repaint();
			}
            cv1.mouseDown=false;
		}
		if ( e.target instanceof Canvas0 )
		{
			if (cv0.singleClick==true & cv0.moveArea==1)
			{
				showStatus("Domain singleClicked");
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]>=140-cv0.x0 & cv0.ddd[i]!=0)
						cv3.leftShow=1;
				if (cv0.x0<0)
					cv2.rightShow=1;
				else
					cv2.rightShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]<10-cv0.x0 & cv0.ddd[i]!=0)
						cv2.rightShow=1;

for (int i=0; i<seqNum; i++)
	if (i>0)
		y0+=cv2.ddd[i-1]+cv2.ddd2[i-1];
cv2.lastLine=(int)(y0+(cv2.seqNum-1)*lineDist+seqBarWidth+(cv0.ddd2[cv2.seqNum-1]+barDist+domBarWidth))+cv2.y00;
y0=y00;
if (cv2.lastLine<505)
	cv2.upShow=0;
else cv2.upShow=1;
				cv2.repaint();
				cv3.repaint();
				cv0.singleClick=false;
			}
			if ((cv0.doubleClick==true & cv0.moveArea==1 ) || cv0. moveArea==3)
			{
				showStatus("Domain doubleClicked");
				cv0.doubleClick=false;
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				if (cv0.x0<0)
					cv2.rightShow=1;
				else
					cv2.rightShow=0;


for (int i=0; i<seqNum; i++)
	if (i>0)
		y0+=cv2.ddd[i-1]+cv2.ddd2[i-1];
cv2.lastLine=(int)(y0+(cv2.seqNum-1)*lineDist+seqBarWidth+(cv0.ddd2[cv2.seqNum-1]+barDist+domBarWidth))+cv2.y00;
y0=y00;
if (cv2.lastLine<505)
	cv2.upShow=0;
else cv2.upShow=1;

				cv2.repaint();
			}
			cv2.leftGoIdx=cv0.leftGoIdx;
			cv2.ddd=cv0.ddd;
			cv0.moveArea=0;
			cv0.mouseDown=false;
		}
		if ( e.target instanceof Canvas2 )
		{
			if (cv2.singleClick==true && cv2.moveArea==2)
			{
				cv0.seqNameUp=cv2.seqNameUp;
				showStatus("Seq. Id singleClicked");
								cv0.repaint();
			//	cv2.repaint();
				cv2.singleClick=false;
				cv2.doubleClick=false;
				cv2.moveArea=0;
			}else if (cv2.singleClick==true && cv2.moveArea==3)
			{
				cv0.sfNameUp=cv2.sfNameUp;
				showStatus("sfId singleClicked");
								cv0.repaint();
			//	cv2.repaint();
				cv2.singleClick=false;
				cv2.doubleClick=false;
				cv2.moveArea=0;
			}else if (cv2.doubleClick==true && cv2.moveArea==2)
			{
				showStatus("Seq. Id doubleClicked");

				cv0.ddd=cv2.ddd;
				cv0.ddd2=cv2.ddd2;
				cv0.leftGoIdx=cv2.leftGoIdx;
				cv0.seqNum=cv2.seqNum;
				cv1.seqNum=cv2.seqNum;
				for (int i=cv2.iii; i<cv0.seqNum; i++)
				{
					cv0.ddd[i]=cv0.ddd[i+1];
					cv0.ddd2[i]=cv0.ddd2[i+1];
					cv0.downX[i]=cv0.downX[i+1];
					cv0.downY[i]=cv0.downY[i+1]-lineDist;
					cv0.downI[i]=cv0.downI[i+1];
					cv0.downJ[i]=cv0.downJ[i+1];
					cv0.downK[i]=cv0.downK[i+1];
					cv0.seq[i]=cv0.seq[i+1];
					cv0.seqId[i]=cv0.seqId[i+1];
					cv0.seqName[i]=cv0.seqName[i+1];
					cv0.seqNameUp[i]=cv0.seqNameUp[i+1];
					cv0.leftGoIdx[i]=cv0.leftGoIdx[i+1];

					cv0.start80X[i]=cv0.start80X[i+1];
					cv0.start80Aa[i]=cv0.start80Aa[i+1];

					for (int j=0; j<domNum; j++)
					{
						cv0.domId[i][j]=cv0.domId[i+1][j];
						cv0.dName[i][j]=cv0.dName[i+1][j];
						cv0.domCol[i][j]=cv0.domCol[i+1][j];
						cv0.domOverlay[i][j]=cv0.domOverlay[i+1][j];
						for (int k=1; k<partsNum; k++)
						{
                            cv0.dom[i][j][k]=cv0.dom[i+1][j][k];
						}
					}

				}
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]>=140-cv0.x0 & cv0.ddd[i]!=0)
						cv3.leftShow=1;
				if (cv0.x0<0)
					cv2.rightShow=1;
				else
					cv2.rightShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]<10-cv0.x0 & cv0.ddd[i]!=0)
						cv2.rightShow=1;

seqNum--;				
if (y00!=12)
{
	drawLegend();
	cv2.y00=cv0.y00-(cv0.farestId-newDomNum)*15;
	cv2.y0=cv2.y00;
	for (int i=0; i<cv0.seqNum; i++)
		cv0.downY[i]=cv0.downY[i]-(cv0.farestId-newDomNum)*15;
}
else
{
	cv2.y00=y00;
	cv2.y0=y00;
}


for (int i=0; i<seqNum; i++)
	if (i>0)
		y0+=cv2.ddd[i-1]+cv2.ddd2[i-1];
cv2.lastLine=(int)(y0+(cv2.seqNum-1)*lineDist+seqBarWidth+(cv0.ddd2[cv2.seqNum-1]+barDist+domBarWidth))+cv2.y00;

				cv0.repaint();
				cv1.repaint();

				cv2.repaint();
				cv3.repaint();
				cv2.singleClick=false;
				cv2.doubleClick=false;
				cv2.moveArea=0;
			}
////////////////
			if (cv2.mouseDown==true & cv2.moveUp==1 & upDown<cv0.seqNum+2+domNum)
			{
				cv2.mouseDown=false;
				cv2.moveUp=0;
				cv2.moveDown=0;
				showStatus("Move Up");
				cv0.y00=cv0.y00-cv0.ddd[upDown]-cv0.ddd2[upDown]-cv0.lineDist;
				cv2.y00=cv0.y00;
			//	upDown=upDown+1;
				cv2.moveUp=0;
				for (int i=0; i<cv0.seqNum; i++)
					cv0.downY[i]=cv0.downY[i]-cv0.ddd[upDown]-cv0.ddd2[upDown]-cv0.lineDist;
				upDown=upDown+1;


				cv2.downShow=1;
for (int i=0; i<seqNum; i++)
	if (i>0)
		y0+=cv2.ddd[i-1]+cv2.ddd2[i-1];
cv2.lastLine=(int)(y0+(cv2.seqNum-1)*lineDist+seqBarWidth+(cv0.ddd2[cv2.seqNum-1]+barDist+domBarWidth))+cv2.y00;
y0=y00;
if (cv2.lastLine<505)
	cv2.upShow=0;


				cv0.repaint();
				cv2.repaint();
			}
			if (cv2.mouseDown==true & cv2.moveDown==1 & upDown>0)
			{
				cv2.mouseDown=false;
				cv2.moveUp=0;
				cv2.moveDown=0;
				showStatus("Move Down");
				cv0.y00=cv0.y00+cv0.ddd[upDown-1]+cv0.ddd2[upDown-1]+cv0.lineDist;
				cv2.y00=cv0.y00;
				for (int i=0; i<cv0.seqNum; i++)
					cv0.downY[i]=cv0.downY[i]+cv0.ddd[upDown-1]+cv0.ddd2[upDown-1]+cv0.lineDist;
				upDown=upDown-1;
				cv2.upShow=1;
				if (upDown<=0)
				cv2.downShow=0;


				cv0.repaint();
				cv2.repaint();
			}
			if (cv2.mouseDown==true && cv2.moveRight==1 && (cv1.leftRight>-cv1.scalerNumBase/2*cv1.strCmpr) | (cv1.strCmpr==1 & cv1.leftRight>-700))
			{
				cv2.mouseDown=false;
				cv3.leftShow=1;
				cv1.moveRight=0;
				cv1.moveLeft=0;
				cv2.moveRight=0;
				cv1.leftRight-=cv1.scalerNumBase/2*cv1.strCmpr;
				showStatus("Move Right");
				cv0.x0+=(int)((cv1.scalerBarLong/2));
if (cv1.scalerBarLong==0)
	cv0.x0+=100;

				for (int i=0; i<cv0.seqNum; i++)
				{
					cv0.downX[i]+=100;
				}
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]>=140-cv0.x0 & cv0.ddd[i]!=0)
						cv3.leftShow=1;
				if (cv0.x0<0)
					cv2.rightShow=1;
				else
					cv2.rightShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]<10-cv0.x0 & cv0.ddd[i]!=0)
						cv2.rightShow=1;
				cv2.repaint();
				cv0.repaint();
				cv1.repaint();
				cv3.repaint();
			}
////////////////
			cv2.mouseDown=false;
		}
		if ( e.target instanceof Canvas3 )
		{
			if (cv3.mouseDown==true && cv3.moveLeft==1 && (cv0.x0+seqLong*cv0.dotWidth>seqBarLong-500) )
			{
				cv3.mouseDown=false;
				cv1.moveLeft=0;
				cv1.moveRight=0;
				showStatus("Move Left");
				cv1.leftRight+=cv1.scalerNumBase/2*cv1.strCmpr;
				cv0.x0-=(int)((cv1.scalerBarLong/2));


if (cv1.scalerBarLong==0)
	cv0.x0-=100;
				for (int i=0; i<cv0.seqNum; i++)
				{
					cv0.downX[i]-=100;
				}
				if (cv0.x0+seqLong*cv0.dotWidth>seqBarLong)
					cv3.leftShow=1;
				else
					cv3.leftShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]>=140-cv0.x0 & cv0.ddd[i]!=0)
						cv3.leftShow=1;
				if (cv0.x0<0)
					cv2.rightShow=1;
				else
					cv2.rightShow=0;
				for (int i=0; i<cv0.seqNum; i++)
					if (cv0.start80X[i]<10-cv0.x0 & cv0.ddd[i]!=0)
						cv2.rightShow=1;


				cv1.repaint();
				cv2.repaint();
				cv0.repaint();
				cv3.repaint();
			}
			cv3.mouseDown=false;
		}
        return super.handleEvent( e );
    }
}


//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
/////////////     0     //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////


class Canvas0 extends Canvas {
    public int seqLong, seqNum, domNum, partsNum, seqBarLong, seqBarWidth, domBarWidth, barDist, barDist0, lineDist, y00,
		test1, test2, leftRight, leftRiteForCV2, upDown, xPoint, displayPage, strCmpr, edgAdjust, sfNameUp[],
		y0, x0, x00, xAt, yAt, ii, jj, kk, iii, moveArea, a, b, domStartIdx, domEndIdx, lowLine, newDomNum, pcmBar,
		domOverlay[][], dom[][][], domCol[][], legend[][], longestId, farestId,
		downI[], downJ[], downK[], downX[], downX0[], downY[], start80X[], start80Aa[],
		seqNameUp[],  dd[][], ddd[], ddd2[], ddd2Tmp[], leftGoIdx[];
    double dotWidth;
    Font f0, f1, f2, f3, f4, f5, f6;
    String seq[],  seqId[],   seqName[],  domId[][],  dName[][], domIdTest, domIdDown, test0, kkkk, sfId[], sfName[];
	long lastDownTime = 0;
	final static long DOUBLE_CLICK_TIME = 300;

	private Image img[], imgbb, leftImg, rightImg, upImg, downImg;
    public boolean mouseMove, mouseDown, mouseUp, firstTime, singleClick, doubleClick, seqRemove, test3[], legendUp;
    public Canvas0()
    {
	    f1=new Font ("Courier", Font.PLAIN, 11);
	    f2=new Font ("Courier", Font.BOLD,  14);
	    f3=new Font ("Courier", Font.BOLD,  12);
	    f4=new Font ("Times", Font.PLAIN, 10);
		f5=new Font ("Times", Font.PLAIN, 12);
		f6=new Font ("Times", Font.PLAIN, 8);
		displayPage=1;
	    setBackground(Color.white);
		strCmpr=1;
		leftRight=0;
        upDown=0;
		iii=0;
		x00=0;
		edgAdjust=0;
		mouseDown=false;
		legendUp=true;
    }
	public void setValue(int sLong,     int sNum,    String s[],  String sId[],     String sName[],
		                 int dNum,      int pNum,    int d[][][], int dCol[][],     String sfi[], String sfn[], String dId[][], 
						 String dN[][], Image ig[],  int d32[],   int dOverlay[][], int y,          int x,
					     int lId,
						 int domBarW,   int seqBarW, int barD,    int lineD,        double dotW,
						 Image leftIm, Image rightIm, Image upIm, Image downIm, Image igbb)
	{
		seqNum=sNum;
        domNum=dNum;
		partsNum=pNum;
	    seq=new String [seqNum];
	    seqId=new String [seqNum];
	    seqName=new String [seqNum];
	    seqNameUp=new int [seqNum];

	    sfId=new String [seqNum];
	    sfName=new String [seqNum];
	    sfNameUp=new int [seqNum];

	    leftGoIdx=new int [seqNum];
		start80X=new int [seqNum];
		start80Aa=new int [seqNum];
	    dom = new int [seqNum][domNum][partsNum];
	    domCol=new int [seqNum][domNum];
	    domId=new String [seqNum][domNum];
	    dName=new String [seqNum][domNum];
	    dd=new int [seqNum][domNum];
	    test3=new boolean [seqNum];
	    domOverlay=new int [seqNum][domNum];

		legend=new int [seqNum][domNum];
		longestId=lId;

	    downI= new int [seqNum];
	    downJ= new int [seqNum];
	    downK= new int [seqNum];
	    downX= new int [seqNum];
		downX0= new int [seqNum];
	    downY= new int [seqNum];
	    ddd= new int [seqNum];
	    ddd2= new int [seqNum];
		ddd2Tmp=new int [seqNum];
		img=new Image [36];
		seqLong=sLong;
		img=ig;
		imgbb=igbb;
		seq=s;
		seqId=sId;
		seqName=sName;
		dom=d;
		domCol=dCol;

		sfId=sfi;
		sfName=sfn;

		domId=dId;
		dName=dN;
	    y00=y;
		x0=x;
	//	legend=lgt;
		domBarWidth=domBarW;
		seqBarWidth=seqBarW;
		barDist=barD;
		barDist0=barD;
		lineDist=lineD;
		dotWidth=dotW;
		ddd2=d32;
		domOverlay=dOverlay;
		leftImg=leftIm;
		rightImg=rightIm;
		upImg=upIm;
		downImg=downIm;

	//	farestId=0;
	//	newDomNum=0;
	}
    public void paint( Graphics g )
    {
		setBackground(Color.white);

 //g.drawString("legendUp=" + y00, x0+675, 12);
        if (legendUp==true)
		{
		  drawLegend(g);

		}

		y0=y00;
			g.setFont(f4);
			for (int i=0; i<seqNum; i++)
				if (i>0)
					y0+=ddd[i-1]+ddd2[i-1];
		g.setFont(f1);
		y0=y00;
		for (int i=0; i<seqNum; i++)
		{
			ii=i;
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];
			if (ddd[i]!=0)
			{
				jj=downJ[i];
				kk=downK[i];
				drawSeqDetail(g);
			}
		}
		drawDomainBars(g);
////////////////
		g.setFont(f1);
		y0=y00;
		for (int i=0; i<seqNum; i++)
		{
			ii=i;
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];
			if (ddd[i]!=0)
			{
				xAt=downX[i];
				yAt=downY[i]+y0-y00;
				drawTriangle(g);
			}
		}
///////////////////
		y0=y00;
		for (int i=0; i<seqNum; i++)
			{
				ii=i;
				if (i>0)
					y0+=ddd[ii-1]+ddd2[i-1];
				if (seqNameUp[ii]==1)
					drawSeqName(g);
				if (sfNameUp[ii]==1)
					drawSfName(g);
			}
			y0=y00;
    }


    public void drawLegend(Graphics g)
	{
	   for (int i=0; i<seqNum; i++)
	       for (int j=0; j<domNum; j++)
		       legend[i][j]=0;

       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
		       if (domId[i][j] !=null)
			   {
			       if (legend[i][j]!=-1)
				   {
			          for (int a=0; a<seqNum; a++)
					  {
				         for (int b=0; b<domNum; b++)
						 {
		                     if (domId[a][b] !=null && domId[i][j].compareTo(domId[a][b])==0)
							 {
						        if (legend[i][j]!=1)
					                legend[i][j]=1;
					            else
						            legend[a][b]=-1;
							 }
						 }
					  }
				   }
			   }
		   }
	   }
       legend[0][0]=1;
       ///order domId ///
       int longestId=0;
	   farestId=0;
       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
		       if (domId[i][j] !=null && legend[i][j]>=1)
			   {
				   if (longestId<domId[i][j].length()+dName[i][j].length())
					   longestId=domId[i][j].length()+dName[i][j].length();
		 	       for (int a=0; a<seqNum; a++)
				   {
				       for (int b=0; b<domNum; b++)
					   {
		                  if (domId[a][b] !=null && domId[i][j].compareTo(domId[a][b])>0 && legend[a][b]>=1)
					      legend[i][j]=legend[i][j]+1;
					   }
				   }
				   if (farestId<legend[i][j])
					   farestId=legend[i][j];
			   }
		   }
	   }
	   if (newDomNum>0)
          y00=y00-(-farestId+newDomNum)*15;

       g.setColor(new Color(240,240,240));
	   g.fillRect(0, y00-farestId*15-23, longestId*5+180, (farestId)*15-8-3+13);
	   g.setColor(Color.black);
	   g.drawRect(0, y00-farestId*15-23, longestId*5+180, (farestId)*15-8-3+13);

       int pcmType=0;
       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
	   	       g.setFont(f4);
               g.setColor(Color.black);
		       if (domId[i][j] !=null && legend[i][j]!=-1)
			   {
				   if (displayPage==2 && domIdDown.equals(domId[i][j]))
				   {
					      g.setColor(Color.white);
	                      g.fillRect(1, y00-farestId*15-23+legend[i][j]*15-2-12, longestId*5+180-2, 15);
						  g.setColor(new Color(220,0,0));
	                      g.drawRect(1, y00-farestId*15-23+legend[i][j]*15-2-12, longestId*5+180-2, 15);
						  g.setColor(Color.black);
				   }
			       if (domId[i][j].startsWith("PCM"))
				   {
			           //g.drawImage(img[35], 12+x0-x0, y00-((domNum+1)*15-4)+legend[i][j]*15-6, 40, seqBarWidth, this);
                       g.drawImage(img[domCol[i][j]], 12+x0+14-x0, y00-farestId*15-23+legend[i][j]*15-10, 15, domBarWidth, this);
				       g.drawString(domId[i][j] + ": " + dName[i][j], 80+x0-x0, y00-farestId*15-23+legend[i][j]*15-3);
				   }
			       else
				   {
                       g.drawImage(img[domCol[i][j]], 12+x0+0-x0, y00-farestId*15-23+legend[i][j]*15-10, 20, domBarWidth, this);
					   g.drawImage(img[domCol[i][j]], 12+x0+20-x0, y00-farestId*15-23+legend[i][j]*15-10, 20, domBarWidth, this);
		               g.drawString(domId[i][j] + ": " + dName[i][j], 80+x0-x0, y00-farestId*15-23+legend[i][j]*15-3);
				   }
			   }
		   }
	   }
	   newDomNum=farestId;
	}



	public void drawDomainBars(Graphics g)
	{
		g.setFont(f4);
		y0=y00;
        for (int i=0; i<seqNum; i++)
		{
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];
			g.drawImage(imgbb, x0, y0+i*lineDist+1, (int)(dotWidth*seq[i].length()), seqBarWidth, this);
			g.setColor(Color.black);
			g.drawString(""+seq[i].length(), (int)(dotWidth*seq[i].length())+x0+12, y0+i*lineDist+8);
			if (domId[i][0]!=null)
			for (int j=0; j<domNum; j++)
			{
				if (domId[i][j].startsWith("HD"))
						dd[i][j]=-(int)(domBarWidth+(domBarWidth-seqBarWidth)/2+barDist);
				else if (domId[i][j].startsWith("PCM"))
						dd[i][j]=-(int)((domBarWidth-seqBarWidth)/2);
				else if (domId[i][j].startsWith("PF"))
						dd[i][j]=+(int)(seqBarWidth+(domBarWidth-seqBarWidth)/2+barDist);
				else
						dd[i][j]=0;
				for (int k=1; k<=(dom[i][j].length-1)/2; k++)
				{
						if ( displayPage==1 )// && ddd2[i]>0)
						{
                            int positionX=(int)(dotWidth*(dom[i][j][k*2-1]))+x0+1;
                            int bw=(int)(dotWidth*dom[i][j][k*2]+x0-positionX+1);
                            int bnum=(int)(bw/20);
                            int bmod=(int)(bw%20);
							int pxIncr;
							
                            if (bw>20)
							{
                                if (bmod>10)
								{
                                   pxIncr=(int)(bw/(bnum+1));
								   bnum++;
								}
                                else
                                   pxIncr=(int)(bw/bnum);
								int testNum=0;
							    while (testNum<bnum)
								{
   							        g.drawImage(img[domCol[i][j]], positionX,
										(y0+(domBarWidth+barDist)*(domOverlay[i][j]+1)+i*lineDist),
								        pxIncr, domBarWidth, this);
                                    positionX=positionX+pxIncr;
									testNum++;
								}
							}
                            else //if (bw>5)
							   g.drawImage(img[domCol[i][j]],positionX,
								   (y0+(domBarWidth+barDist)*(domOverlay[i][j]+1-pcmBar)+i*lineDist),bw,domBarWidth,this);
						}
						if ( (displayPage==2 && domId[i][j].equals(domIdDown) )  ) // || (displayPage==1 && ddd2[i]==0) )
						{
                            int positionX=(int)(dotWidth*(dom[i][j][k*2-1]))+x0+1;
                            int bw=(int)(dotWidth*dom[i][j][k*2]+x0-positionX+1);
                            int bnum=(int)(bw/20);
                            int bmod=(int)(bw%20);
							int pxIncr;
                            if (bw>20)
							{
                                if (bmod>10)
								{
                                   pxIncr=(int)(bw/(bnum+1));
								   bnum++;
								}
                                else
                                   pxIncr=(int)(bw/bnum);
								int testNum=0;
							    while (testNum<bnum)
								{
   							        g.drawImage(img[domCol[i][j]], positionX, y0+dd[i][j]+i*lineDist,
								        pxIncr, domBarWidth, this);
                                    positionX=positionX+pxIncr;
									testNum++;
								}
							}
                            else
                                 g.drawImage(img[domCol[i][j]],positionX,y0+dd[i][j]+i*lineDist,bw,domBarWidth,this);
						}
						if (dom[i][j][k*2]==0)
							k=(dom[i][j].length-1)/2+1;
				}
				if (domId[i][j+1]==null)
						j=domNum;

				g.setColor(new Color(230,230,230));
				g.fillRect(0, (y0+i*lineDist-domBarWidth-barDist-(domBarWidth-seqBarWidth)/2-5), 760, 2 );

			}

			g.setColor(Color.white);
			//if (ddd2[i]==0)
			//	g.drawLine( x0, (int)(y0+i*lineDist-domBarWidth-(domBarWidth-seqBarWidth)/2+barDist), x0,
			//	      (int)(y0+i*lineDist+domBarWidth+seqBarWidth+(domBarWidth-seqBarWidth)/2+barDist));
			//else
	//			g.drawLine( x0, (int)(y0+i*lineDist-domBarWidth-barDist-(domBarWidth-seqBarWidth)/2-3), x0,
	//			      (int)(y0+i*lineDist+seqBarWidth+(ddd2[i]+barDist+domBarWidth)) );
		}
    barDist=barDist0;
	}
    public boolean mouseDown( Event e, int x, int y )
    {
		moveArea=0;
		singleClick=false;
		doubleClick=false;
		xAt = x;
		yAt = y;
		seqLocation(xAt, yAt);
		iii=ii;
		if ( moveArea==1 )
		{
			singleClick=true;
			downI[ii]=ii;
			downJ[ii]=jj;
			downK[ii]=kk;
			downX[ii]=xAt;
			downX0[ii]=xAt;
			start80X[ii]=xAt-40*7-x0;
			start80Aa[ii]=(int)((xAt-x0)/dotWidth)-40;

			y0=y00;
			for (int i=0; i<=ii; i++)
				if (i>0)
					y0+=ddd[i-1]+ddd2[i-1];
			downY[ii]=yAt-(y0-y00);  // the distance between the point and the sequence bar
			y0=y00;
			if (ddd[ii]!=20)
				ddd[ii]=20;
			else
				ddd[ii]=0;
			domIdDown=domId[ii][jj];
			if (e.when-lastDownTime<DOUBLE_CLICK_TIME)
			{
				if (displayPage==2)
					displayPage=1;
				else
					displayPage=2;
				for (int i=0; i<seqNum; i++)
				{
					if (displayPage==2)
					{
						ddd[i]=0;
						ddd2Tmp[i]=ddd2[i];
						ddd2[i]=0;
						downX[i]=0;
						downX0[i]=0;
						downY[i]=0;
						downI[i]=0;
						downJ[i]=0;
						downK[i]=0;
						leftGoIdx[i]=0;
					}
					if (displayPage==1)
						ddd2[i]=ddd2Tmp[i];
				}
				doubleClick=true;
			}
			repaint();
		}
		lastDownTime=e.when;


            if (moveArea==3)
			{
				if (displayPage==2)
					displayPage=1;
				else
					displayPage=2;
				for (int i=0; i<seqNum; i++)
				{
					if (displayPage==2)
					{
						ddd[i]=0;
						ddd2Tmp[i]=ddd2[i];
						ddd2[i]=0;
						downX[i]=0;
						downX0[i]=0;
						downY[i]=0;
						downI[i]=0;
						downJ[i]=0;
						downK[i]=0;
						leftGoIdx[i]=0;
					}
					if (displayPage==1)
						ddd2[i]=ddd2Tmp[i];
				}

				repaint();
			}


		return true;
    }
	public void drawSeqName(Graphics g)
	{
		 g.setColor(Color.white);
		     g.fillRect((x0+20), (y0+ii*lineDist-4-8), seqName[ii].length()*7+20, 15);
		 g.setColor(Color.black);
		     g.drawRect((x0+20), (y0+ii*lineDist-4-8), seqName[ii].length()*7+20, 15);
		 g.drawString(seqName[ii], x0+30, (y0+ii*lineDist)+8-8);
	}
	public void drawSfName(Graphics g)
	{
		 g.setColor(Color.white);
		     g.fillRect((x0+20), (y0+ii*lineDist-4+8), sfName[ii].length()*7+20, 15);
		 g.setColor(Color.black);
		     g.drawRect((x0+20), (y0+ii*lineDist-4+8), sfName[ii].length()*7+20, 15);
		 g.drawString(sfName[ii], x0+30, (y0+ii*lineDist)+8+8);
	}
	public void drawTriangle(Graphics g)
	{
         g.setColor(Color.blue);
		 g.fillArc(x0+start80X[ii]+40*7-13, (yAt-13), 28, 28, 60, 60 );
         g.setColor(Color.white);
		 g.fillArc(x0+start80X[ii]+40*7-6, (yAt-10), 14, 14, 60, 60 );


		 g.setColor(new Color(210,210,210));
		 g.fillRect(x0+start80X[ii]+40*7+15, (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2-28), 48, 12);
		 g.setColor(Color.blue);
		 g.drawRect(x0+start80X[ii]+40*7+15, (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2-28), 48, 12);
		 

		 g.drawString(""+(start80Aa[ii]+41), x0+start80X[ii]+40*7+25,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2-18) );

	}
	public void draw80Seq(Graphics g)
	{
		 a=start80Aa[ii];
		 b=start80Aa[ii]+81;
		 edgAdjust=0;
		 if (start80Aa[ii]<=1)
		 {
			 edgAdjust=(a)*7;
			 a=1;
		 }
		 if (b>=seq[ii].length())
			 b=seq[ii].length();
		     //b=seq[ii].length()-1;

     ////////shade area frame
		 g.setColor(new Color(195,50,0));
		 //top
		 g.drawRect(x0+start80X[ii]+40*7-(int)(dotWidth*41),
			    (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2-18),
			    (int)(81*dotWidth), ddd[ii]+ddd2[ii]+lineDist-18);
         //middle
		 g.drawRect(x0+start80X[ii]+34*7-30-4,
			    (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+5+ddd2[ii]-3),
				  150+1, ddd[ii]+2-8);
         //bottom
		 g.drawRect(x0+start80X[ii]-2*7,
			    (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+5+ddd2[ii]-3+10),
				  84*7, ddd[ii]+2-10);

     ////////shade area fill
		 g.setColor(new Color(240,240,240));
		 //top
		 g.fillRect(x0+start80X[ii]+40*7-(int)(dotWidth*41)+1,
			    (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2-18+1),
			    (int)(81*dotWidth)-1, ddd[ii]+ddd2[ii]+lineDist-18-1);
		 //middle
		 g.fillRect(x0+start80X[ii]+34*7-30+1-4,
			          (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+5+ddd2[ii]-3+1),
					  150-1+1, ddd[ii]+2-8);
		 //bottom
		 g.fillRect(x0+start80X[ii]-2*7+1,
			          (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+5+ddd2[ii]-3+10+1),
					  84*7-1, ddd[ii]+2-10-1);
		 		 g.setColor(Color.black);

     ////////shade area text
		 g.setFont(f1);
		 g.setColor(Color.black);
		 g.drawString(seq[ii].substring( a-1, b ), x0+start80X[ii]-edgAdjust-7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );

		 g.setFont(f4);
         g.setColor(new Color(195,50,0));
		 g.drawString(""+a, x0+start80X[ii]-edgAdjust-7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii])-11 );
		 g.drawString(""+b, x0+start80X[ii]+80*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii])-11 );


/*     ////////shade area text
		 g.setFont(f1);
		 g.setColor(Color.black);
		 g.drawString(seq[ii].substring( a-1, b ), x0+start80X[ii]-edgAdjust-7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );

		 g.setFont(f4);
         g.setColor(new Color(195,50,0));
		 g.drawString(""+a, x0+start80X[ii]-edgAdjust-7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii])-11 );
		 g.drawString(""+b, x0+start80X[ii]+80*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii])-11 );

*/


/*
      /////// draw dom seq (red)
		 g.setFont(f1);
		 domStartIdx=dom[ii][jj][kk]-1;
         domEndIdx=dom[ii][jj][kk+1]-1;
		 
         if (domStartIdx<a-1)
			 domStartIdx=a-1;
		 if (domEndIdx>b)
		     domEndIdx=b;
		 g.setFont(f1);
		 if (a>1)
		 {
			 //////// droaw red domain content
			 g.setColor(Color.red);
             g.drawString(seq[ii].substring( domStartIdx, domEndIdx+1 ), x0+start80X[ii]+(domStartIdx-(start80Aa[ii]))*7, 
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
	         /////// draw blue point a.a.
		     g.setColor(Color.blue);
		     g.drawString(seq[ii].substring( start80Aa[ii]+40, start80Aa[ii]+41 ), x0+start80X[ii]+40*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
		 }
		 else
		 {
			 //////// droaw red domain content
			 g.drawString(seq[ii].substring( domStartIdx, domEndIdx+1 ), x0+start80X[ii]+(domStartIdx-(start80Aa[ii])-1)*7, 
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
	         /////// draw blue point a.a.
		     g.setColor(Color.blue);
		     g.drawString(seq[ii].substring( start80Aa[ii]+40, start80Aa[ii]+41 ), x0+start80X[ii]+(40-1)*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
         }

	  /////// draw domId
		 g.setFont(f4);
		 g.setColor(Color.black);
		     g.drawString(domId[ii][jj]+" ["+dom[ii][jj][kk]+"-"+dom[ii][jj][kk+1]+"]",
			              x0+start80X[ii]+34*7, (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+10+ddd2[ii]+2));


*/


      /////// draw dom seq (red)
		 g.setFont(f1);
		 domStartIdx=dom[ii][jj][kk]-1;
         domEndIdx=dom[ii][jj][kk+1]-1;
		 
         if (domStartIdx<a-1)
			 domStartIdx=a-1;
		 if (domEndIdx>b)
		     domEndIdx=b;
		 g.setFont(f1);
		 if (a>1)
		 {
			 //////// draw red domain content
			 g.setColor(Color.red);
             g.drawString(seq[ii].substring( domStartIdx, domEndIdx+1 ), x0+start80X[ii]+(domStartIdx-(start80Aa[ii]))*7, 
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
	         /////// draw blue point a.a.
		     g.setColor(Color.blue);
		     g.drawString(seq[ii].substring( start80Aa[ii]+40, start80Aa[ii]+41 ), x0+start80X[ii]+40*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );

		 }
		 else
		 {
			 //////// draw red domain content
			 g.drawString(seq[ii].substring( domStartIdx, domEndIdx+1 ), x0+start80X[ii]+(domStartIdx-(start80Aa[ii])-1)*7, 
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
	         /////// draw blue point a.a.
		     g.setColor(Color.blue);
		     g.drawString(seq[ii].substring( start80Aa[ii]+40, start80Aa[ii]+41 ), x0+start80X[ii]+(40-1)*7,
			         (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );

         }

	  /////// draw domId
		 g.setFont(f4);
		 g.setColor(Color.black);
		     g.drawString(domId[ii][jj]+" ["+dom[ii][jj][kk]+"-"+dom[ii][jj][kk+1]+"]",
			              x0+start80X[ii]+34*7-20, (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+10+ddd2[ii]+2));

	  ////// remove any extra a.a. after 80 a.a.
		 g.setColor(new Color(240,240,240));
		 g.fillRect(x0+start80X[ii]+80*7+7,
			 (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii])-11+3, 7, 9 );








	}
/*	public void drawPointCav(Graphics g)
	{
		//g.setColor(new Color(200,200,200));
		g.setColor(new Color(240,240,240));
		g.fillRect(680, (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+12+ddd2[ii]), 45, 14);
		g.setColor(Color.blue);
		g.setFont(f4);
		g.drawString("["+xPoint+"]", 288,
			 (y0+ii*lineDist+seqBarWidth+domBarWidth+barDist+(domBarWidth-seqBarWidth)/2+22+ddd2[ii]) );
	}*/
	public void drawSeqDetail(Graphics g)
	{
		draw80Seq(g);
	}
    public void seqLocation (int x, int y)
    {
		y0=y00;
  		for (int i=0; i<seq.length; i++)
		{
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];
			for (int j=0; j<domNum; j++)
			{
				if (dom[i][j]==null)
					break;
				else
				{
					if ( displayPage==1 )
					{
						for (int k=1; k<dom[i][j].length; k=k+2)
						{
							if ( (xAt>=x0+(int)(dotWidth*(dom[i][j][k])-1.3))
									& (xAt<x0+(int)(dotWidth*(dom[i][j][k+1])))
									& (yAt>=(y0+i*lineDist-domBarWidth-barDist-(domBarWidth-seqBarWidth)/2-5))
									& (yAt<=y0+(i)*lineDist+domBarWidth+(int)((domBarWidth-seqBarWidth)/2)+ddd2[i]+domBarWidth) )
								{
								if ( yAt>(domOverlay[i][j]-pcmBar)*(domBarWidth+barDist)+y0+(i)*lineDist+domBarWidth-(int)((domBarWidth-seqBarWidth)/2)
									&& yAt<(domOverlay[i][j]+1-pcmBar)*(domBarWidth+barDist)+y0+(i)*lineDist+domBarWidth-(int)((domBarWidth-seqBarWidth)/2) )
								{
									if ((xAt-x0)/dotWidth>=dom[i][j][k] && (xAt-x0)/dotWidth<=dom[i][j][k+1])
									{
										ii=i;
										jj=j;
										kk=k;
										moveArea=1;

										break;
									}
								}
							}
						}
						if ((xAt>x0-80 & xAt<x0-12) & (yAt>y0+(i)*lineDist-5 & yAt<y0+(i)*lineDist+10))
						{
							ii=i;
							moveArea=2;  
						}

					}
					else
					{
						for (int k=1; k<dom[i][j].length; k=k+2)
						{
							if ( (xAt>=x0+(int)(dotWidth*(dom[i][j][k])+1))
								& (xAt<x0+(int)(dotWidth*(dom[i][j][k+1])))
								& (yAt>=y0+(i)*lineDist-(domBarWidth-(domBarWidth-seqBarWidth)/2+barDist))
								& (yAt<=y0+(i)*lineDist+seqBarWidth+(domBarWidth-seqBarWidth)/2+barDist+domBarWidth) )
							{
								if ( (domId[i][j].startsWith("PCM") & yAt>y0+i*lineDist-(domBarWidth-seqBarWidth)/2 & yAt<y0+i*lineDist+(domBarWidth-seqBarWidth)/2+seqBarWidth)
									| (domId[i][j].startsWith("PF") & yAt>y0+i*lineDist+seqBarWidth+(domBarWidth-seqBarWidth)/2) )
								{
									if ( domId[i][j].equals(domIdDown) )
									{
										if ((xAt-x0)/dotWidth>=dom[i][j][k] && (xAt-x0)/dotWidth<=dom[i][j][k+1])
										{
										    ii=i;
										    jj=j;
										    kk=k;
										    moveArea=1;
											
										    break;
										}
									}
								}
							}
						}
						if ((xAt>x0-80 & xAt<x0-12) & (yAt>y0+(i)*lineDist-5 & yAt<y0+(i)*lineDist+10))
						{
							ii=i;
							moveArea=2;  
						}
					}
				}
			}
	  }

//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
 int pcmType=0;
       for (int i=0; i<seqNum; i++)
	   {
	       for (int j=0; j<domNum; j++)
		   {
		       if (domId[i][j] !=null && legend[i][j]!=-1)
			   {
			       if (xAt>=25 && xAt<=40 &&
					   yAt>=y00-farestId*15-23+legend[i][j]*15-10 && yAt<=y00-farestId*15-23+legend[i][j]*15-10+domBarWidth &&
					   domId[i][j].startsWith("PCM"))
				   {
                        domIdDown=domId[i][j];
						moveArea=3;
				   }
			       if (xAt>=12 && xAt<=52 &&
					   yAt>=y00-farestId*15-23+legend[i][j]*15-10 && yAt<=y00-farestId*15-23+legend[i][j]*15-10+domBarWidth &&
					   domId[i][j].startsWith("PF"))
				   {
					   domIdDown=domId[i][j];
					   moveArea=3;
				   }
			   }
		   }
	   }
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////

	  return;
    }
}

/*

//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
///////////// 1 w/ sfn  //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////


class Canvas1 extends Canvas {
    private int yAt, xAt;
	int moreInfo, reload, stretch, sclBack, moveLeft, moveRight, moveUp, moveDown, showMeNum,
		colPick, x0, scalerBarLong, scalerNumBase, seqNum, seqNum0, seqLong, strCmpr, clearDetail,
		btnX0,btnY0,btnWidth,btnHight,
		btnStx,btnSty, btnCpx,btnCpy, btnSCx,btnSCy,
		btnRfx,btnRfy, btnMrx,btnMry,
		btnUpx,btnUpy, btnDnx,btnDny, btnLfx,btnLfy, btnRtx,btnRty, btnMvx,btnMvy, btnLgtx, btnLgty,
		leftRight, sizeCase, legendClick, notMe;
    private Font f0, f1, f2, f3, f4, f5, f6, f7, f8, f9;
	double dotWidth;
    private String sfid, sfname;
	boolean mouseDown, mouseUp, legendUp;
	private Image imgMag, showMe, qMark, fingerUp, fingerDown, refImg, imgZoomin, imgZoomout, imgReload;
    public Canvas1()
    {
	     f1=new Font ("Times", Font.BOLD, 12);
	     f2=new Font ("Times", Font.PLAIN, 10);
	     f3=new Font ("MS Sans Serif (Western)", Font.PLAIN,  10);
	     f4=new Font ("Verdana", Font.PLAIN, 12);
		 f5=new Font ("Verdana", Font.PLAIN, 10);
		 f6=new Font ("Verdana", Font.PLAIN, 3);
		 f7=new Font ("Times", Font.PLAIN, 12);
		 f8=new Font ("Courier", Font.BOLD, 14);
		 f9=new Font ("Courier", Font.BOLD, 20);

		btnX0=705;
		btnY0=4;
		btnWidth=38;
		btnHight=12;
		leftRight=0;
		colPick=0;
		x0=0;
		showMeNum=0;
		legendUp=true;

		btnMvx=600;			btnMvy=32;
        btnLgtx=650;        btnLgty=32;

		btnStx=520;						btnSty=31;
		btnCpx=btnStx-40;				btnCpy=btnSty;
        btnRfx=btnX0+btnWidth*5-30;		btnRfy=btnY0+btnHight-3;
		btnMrx=800;		btnMry=30;

    }
	public void setValue(int sNum, String s1, String s2, int sLong, double dotW, Image imgRld,
		                 Image imgM, Image sMe, Image qM, Image fUp, Image fDown, Image refIm, Image zIn, Image zOut)
	{
		seqNum=sNum;
		seqNum0=sNum;
		sfid=s1;
		sfname=s2;
		seqLong=sLong;
		dotWidth=dotW;
		imgReload=imgRld;
		imgMag=imgM;
		showMe=sMe;
		qMark=qM;
		fingerUp=fUp;
		fingerDown=fDown;
		refImg=refIm;
		imgZoomin=zIn;
		imgZoomout=zOut;

	    setBackground(new Color(250,250,250));
		moreInfo=0;
		reload=0;
		moveLeft=0;
		moveRight=0;
		moveUp=0;
		moveDown=0;
		sclBack=0;
		stretch=0;
		strCmpr=1;
		clearDetail=0;
		legendClick=0;
		mouseDown=false;
	}
    public void paint( Graphics g )
    {
		g.drawImage(qMark,btnMrx-45, btnMry-17, this);
		g.setFont(f1);
		g.drawRoundRect(btnMrx-2, btnMry-13, 34, 16, 2, 2);
		g.drawString("HELP",btnMrx, btnMry);
	//	g.drawImage(refImg,btnMvx, btnMvy, 20,20,this);
		g.drawRoundRect(btnMvx, btnMvy, 34, 12, 2, 2);
		g.setFont(f2);
		g.drawString(" clean ",btnMvx+2, btnMvy+10);
		g.drawRoundRect(btnLgtx, btnLgty, 65, 12, 2, 2);
		if (legendUp==true)
		    g.drawString("hide legend",btnLgtx+5, btnLgty+10);
		else
            g.drawString("show legend",btnLgtx+4, btnLgty+10);
		g.drawRoundRect(16, btnMvy, 40, 12, 2, 2);
		g.drawString(" reload ",16+2, btnMvy+10);

	//	g.drawImage(imgReload,5, 12, this);
	//	g.setColor(Color.black);
		g.setColor(new Color(0,0,150));
		g.setFont(f1);
		g.drawString(sfid+"", 20, 18 );
		g.setFont(f8);
		g.drawString(sfname+" FAMILY MEMBERS", 100, 18 );
      //  g.setFont(f3);
	//	if (seqNum==seqNum0)
	//		g.drawString("( "+seqNum+" sequences )", ((sfname.length()+15)*8+120), 18 );
	//	else
	//		g.drawString("( "+seqNum+" / "+seqNum0+" sequences here )", ((sfname.length()+15)*8+120), 18 );
	//	g.setColor(Color.red);

        g.setFont(f3);
		if (seqNum0==1)
		{
			if (seqNum0==1)
			   g.drawString("( "+seqNum+" sequence )", ((sfname.length()+15)*8+120), 18 );
			if (seqNum==0)
			   g.drawString("( 1/1 sequence removed )", ((sfname.length()+15)*8+120), 18 );
		}
		else if (seqNum0>1)
		{
			if (seqNum0==seqNum)
			   g.drawString("( "+seqNum+" sequences )", ((sfname.length()+15)*8+120), 18 );
			else if (seqNum==seqNum0-1)
			   g.drawString("( "+ (seqNum0-seqNum) +" / "+seqNum0+" sequence removed )", ((sfname.length()+15)*8+120), 18 );
			else
			   g.drawString("( "+ (seqNum0-seqNum) +" / "+seqNum0+" sequences removed )", ((sfname.length()+15)*8+120), 18 );
		}

		g.setColor(new Color(0,0,150));
		g.setFont(f8);



if (seqLong>400)
{
		scaler(g);
		g.setColor(Color.black);
		//g.drawImage(imgMag, btnStx-25, btnSty-8, 20, 20, this);
		if (strCmpr<4)
		{
			//g.draw3DRect(btnStx, btnSty, 10, 10, true);
			//g.drawString("+", btnStx+2, btnSty+10);
			g.drawImage(imgZoomin, btnStx+2, btnSty, this);
		}
		if (strCmpr>1)
		{
			//g.draw3DRect(btnCpx, btnCpy, 10, 10, true);
			//g.drawString("_", btnCpx+2, btnCpy+4);
			g.drawImage(imgZoomout, btnCpx+2, btnCpy, this);
		}
}
		if (mouseDown==true && moreInfo==1)
		{


g.setColor(Color.black);
g.drawImage(showMe, 345, 3, 450, 40, this);
g.setFont(f4);
g.drawRect(736, 3, 16, 16);
g.drawString("X", 741, 16);

if (notMe==1)
{
    g.setColor(Color.white);
	g.fillRect(btnMrx-40, btnMry-17, 25, 12);
	g.drawString("Not me. That >>>", btnMrx-40, btnMry-17+8);
	g.setColor(Color.black);
	g.drawRect(btnMrx-40, btnMry-17, 25, 12);
}

if (showMeNum!=0)
	g.drawImage(fingerUp,360, 3, 13,13,this);
if (showMeNum!=5)
	g.drawImage(fingerDown,360, 22, 13,13,this);
if (showMeNum==0)
{
	g.drawString("* To remove a sequence from the displaying set", 385, 18);
	g.drawString("                      ------ double click on the sequence ID;",385, 33);
}
if (showMeNum==1)
{
	g.drawString("* To turn on/off a sequence name", 385, 18);
	g.drawString("                      ------ single click on its sequence ID;",385, 33);
}
if (showMeNum==2)
{
	g.drawString("* To turn on/off a domain/motif name and its context", 385, 18);
	g.drawString("                      ------ single click on its bar in a sequence;",385, 33);
} 
if (showMeNum==3)
{
	g.drawString("* To turn on/off only identical domains/motifs displaying (a)", 385, 18);
	g.drawString("                      ------ single click on the bar in the legend;",385, 33);
}
if (showMeNum==4)
{
	g.drawString("* To turn on/off only identical domains/motifs displaying (b)", 385, 18);
	g.drawString("                      ------ double click on a bar in a sequence;",385, 33);
}
if (showMeNum==5)
{
	g.drawString("* For best print out, use Internet Explorer", 385, 18);
	g.drawString("       or Netscape 6.0 or higher with Window 2000.",385, 33);
}
//if (showMeNum==6)
//{
//	g.drawString("* To start over again,        ------ click on", 385, 25);
//    g.drawImage(imgReload,580, -5, this);
//}

		}
		g.setColor(new Color(150,150,150));
		g.fillRect(0, 48, 850, 2);
	}
	public void scaler (Graphics g)
	{
			for (int i=200; i<30000; i+=200)
			{
				if (seqLong<i & seqLong>i-200)
				{
					//scalerBarLong=(int)((i-1)/dotWidth/2);
					scalerBarLong=(int)((i-200)*dotWidth/2);
					scalerNumBase=(i-200)/2;
					i>30000;
				}
			}
			for (int i=0; i<4; i++)
			{
				g.setColor(new Color(250,250,250));
				if (colPick==0)
				{
					colPick=1;
					g.setColor(new Color(220,220,220));
				}
				else
					colPick=0;

				g.fillRect(80+(int)(i*scalerBarLong/4/strCmpr),
					39, (int)(scalerBarLong/4/strCmpr), 5);
				g.setColor(Color.black);
				g.drawRect(80+(int)(i*scalerBarLong/4/strCmpr),
					39, (int)(scalerBarLong/4/strCmpr), 5);

			}
			g.setColor(Color.black);
            g.setFont(f5);
			if ((1+leftRight/strCmpr)>=0)
				g.drawString(""+(1+leftRight/strCmpr), 76, 38);
			if (((scalerNumBase+leftRight)/strCmpr)>=0)
			g.drawString(""+(scalerNumBase+leftRight)/strCmpr, 76+scalerBarLong/strCmpr, 38);
			g.setFont(f4);

	}

    public boolean mouseEnter( Event e, int x, int y )
    {
		xAt = x;
        yAt = y;
        if ( xAt>=btnMrx-45 & xAt<=btnMry-28 & yAt>=btnMry-17 & yAt<=btnMry-5 )
		{
			notMe=1;
			repaint();
		}
		return true;
    }
    public boolean mouseExit( Event e, int x, int y )
    {
		xAt = x;
        yAt = y;
        if ( xAt>=btnMrx-45 & xAt<=btnMry-28 & yAt>=btnMry-17 & yAt<=btnMry-5 )
		{
			mouseDown=true;
			notMe=0;
			repaint();
		}
		return true;
    }
    public boolean mouseDown( Event e, int x, int y )
    {
		mouseDown=false;
		reload=0;
        xAt = x;
        yAt = y;

	    if ( xAt>=btnLgtx & xAt<=btnLgtx+65 & yAt>=btnLgty & yAt<=btnLgty+12)
		{
			mouseDown=true;
			if (legendUp==true)
			    legendUp=false;
			else
				legendUp=true;
			legendClick=1;
			repaint();
		}
	    if ( xAt>=736 & xAt<=752 & yAt>=3 & yAt<=19 & moreInfo==1)
		{
			mouseDown=true;
			moreInfo=0;
			repaint();
		}
	    if ( xAt>=btnMrx-2 & xAt<=btnMrx+34 & yAt>=btnMry-13 & yAt<=btnMry+7)
		{
			mouseDown=true;
			moreInfo=1;
			repaint();
		}
	    if ( xAt>=16 & xAt<=56 & yAt>=btnMvy & yAt<=btnMvy+12)
		{
			mouseDown=true;
			reload=1;
			strCmpr=1;
			leftRight=0;
			x0=0;
		//repaint();
		}
	    if ( xAt>=btnMvx & xAt<=btnMvx+34 & yAt>=btnMvy & yAt<=btnMvy+12)
		{
			mouseDown=true;
			clearDetail=1;
			strCmpr=1;
			leftRight=0;
			x0=0;
		//repaint();
		}
	    if ( xAt>=btnStx & xAt<=btnStx+20 & yAt>=btnSty & yAt<=btnSty+15 & strCmpr<4 & seqLong>400)
		{
			mouseDown=true;
			stretch=1;
			strCmpr*=2;
		//	repaint();
		}
	    if ( xAt>=btnCpx & xAt<=btnCpx+20 & yAt>=btnCpy & yAt<=btnCpy+15 & strCmpr>1 & seqLong>400)
		{
			mouseDown=true;
			sclBack=1;
			strCmpr/=2;
		//	repaint();
		}
/////////
	    if ( xAt>=360 & xAt<=373 & yAt>=3 & yAt<=16 & moreInfo==1 & showMeNum!=0)
		{
			mouseDown=true;
			showMeNum-=1;
			repaint();
		}
	    if ( xAt>=360 & xAt<=373 & yAt>=22 & yAt<=35 & moreInfo==1 & showMeNum!=5)
		{
			mouseDown=true;
			showMeNum+=1;
			repaint();
		}
        return true;
    }
}


//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
///////////// 2 w/o sfn //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////



class Canvas2 extends Canvas {
    public int seqNum, domNum, y00, y0, x0, domBarWidth, seqBarWidth, barDist, lineDist, lastLine, newDomNum,
		ddd[], ddd2[], downX[], leftGoIdx[], seqNameUp[], legend[][], legendShrink, sfNameUp[], lessDoman,
		xAt, yAt, ii, iii, moveArea, upDown, moveDown, moveUp, moveRight, rightShow, upShow, downShow;
    Font f1, f2, f3, f4, f5;
    String seqId[],   seqName[],  domIdTest, domIdDown, domId[][], sfId[];
	long lastDownTime = 0;
	final static long DOUBLE_CLICK_TIME = 250;
    boolean mouseDown, mouseUp, singleClick, doubleClick, seqRemove, test3[], legendUp;
	private Image upImg, downImg, leftImg;

    public Canvas2()
    {
	     f1=new Font ("Courier", Font.PLAIN, 11);
	     f2=new Font ("Courier", Font.BOLD,  14);
	     f3=new Font ("Courier", Font.BOLD,  12);
	     f4=new Font ("Times", Font.PLAIN, 10);
	     f5=new Font ("Times", Font.PLAIN, 10);
    }

	public void setValue(int sNum, String sId[], String sName[], int d32[], int y, String sf[],
		                 int domBarW, int seqBarW, int barD, int lineD, Image upIm, Image downIm, Image leftIm, int lastL)
	{
	    seqNum=sNum;
	    seqId=new String [seqNum];
	    seqName=new String [seqNum];

		sfId=new String [seqNum];

		seqNameUp=new int [seqNum];
	    ddd=new int [seqNum];
	    ddd2=new int [seqNum];
        leftGoIdx=new int [seqNum];
		seqId=sId;
		seqName=sName;

		ddd2=d32;
		y00=y;

		sfId=sf;
        sfNameUp=new int [seqNum];

		domBarWidth=domBarW;
		seqBarWidth=seqBarW;
		barDist=barD;
		lineDist=lineD;
		upImg=upIm;
		downImg=downIm;
		leftImg=leftIm;
		lastLine=lastL;
		if (lastLine>400)
			upShow=1;
		else upShow=0;
		iii=0;
		x0=23;
        setBackground(Color.white);


	//	lessDoman=0;
	}
    public void paint( Graphics g )
    {
		y0=y00;
		g.setFont(f4);
        for (int i=0; i<seqNum; i++)
		{
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];

			g.setColor(Color.black);
			g.drawString(seqId[i], x0, y0+i*lineDist+8);

        //    g.drawString("(" + sfId[i] + ")", x0-7, y0+i*lineDist+14);

			g.setColor(new Color(230,230,230));
			g.fillRect(10, (y0+i*lineDist-domBarWidth-barDist-(domBarWidth-seqBarWidth)/2-5), 120, 2 );
			if (y0+i*lineDist+8>480)
				upShow=1;
			else upShow=0;
		}
		if (downShow==1)
		{
            g.setColor(Color.white);
			g.fillRect(10, 0, 100, 20);
			g.drawImage(upImg, 25,0,30,10, this);
		}
		if (upShow==1)
		{
			g.setColor(Color.white);
			g.fillRect(10, 500, 100, 40);
			g.drawImage(downImg, 25,508,30,10, this);
		}
		if (rightShow==1)
			g.drawImage(leftImg, 0,160,10,30, this);
	}
    public boolean mouseDown( Event e, int x, int y )
    {
		moveArea=0;
		singleClick=false;
		doubleClick=false;
		xAt = x;
		yAt = y;
		seqLocation(xAt, yAt);
		iii=ii;
		if ( moveArea==2 )
		{
			if (seqNameUp[ii]<1)
				seqNameUp[ii]=1;
			else
				seqNameUp[ii]=0;
			singleClick=true;
			if (e.when-lastDownTime<DOUBLE_CLICK_TIME)
			{
				doubleClick=true;
				singleClick=false;
				seqNum--;
			}
		}
		if ( moveArea==3 )
		{
			if (sfNameUp[ii]<1)
				sfNameUp[ii]=1;
			else
				sfNameUp[ii]=0;
			singleClick=true;
		}
		lastDownTime=e.when;
		return true;
    }
    public void seqLocation (int x, int y)
    {
		y0=y00;
  	  for (int i=0; i<seqNum; i++)
	  {
		 if (i>0)
			y0+=ddd[i-1]+ddd2[i-1];
		 if ((xAt>x0 & xAt<90) & (yAt>y0+(i)*lineDist-6 & yAt<y0+(i)*lineDist+8) & yAt>12 & yAt<506)
		 {
			ii=i;
			moveArea=2;  
		 }

	//	 if ((xAt>x0 & xAt<90) & (yAt>y0+(i)*lineDist+6 & yAt<y0+(i)*lineDist+12) & yAt>8 & yAt<506)
	//	 {
	//		ii=i;
	//		moveArea=3;  
	//	 }
	  }
	  if (xAt>25 & xAt<55 & yAt>0 & yAt<8 & downShow==1)
	  {
		  	mouseDown=true;
			moveDown=1;
		//	repaint();
	  }
	  if (xAt>25 & xAt<55 & yAt>508 & yAt<518 & upShow==1)
	  {
		  	mouseDown=true;
			moveUp=1;
		//	repaint();
	  }
	  if (xAt>0 & xAt<10 & yAt>160 & yAt<190 & rightShow==1)
	  {
		  	mouseDown=true;
			moveRight=1;
		//	repaint();
	  }
	  return;
    }
}

*/
///*

//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
///////////// 1 w/o sfn //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////


class Canvas1 extends Canvas {
    private int yAt, xAt;
	int moreInfo, reload, stretch, sclBack, moveLeft, moveRight, moveUp, moveDown, showMeNum,
		colPick, x0, scalerBarLong, scalerNumBase, seqNum, seqNum0, seqLong, strCmpr, clearDetail,
		btnX0,btnY0,btnWidth,btnHight,
		btnStx,btnSty, btnCpx,btnCpy, btnSCx,btnSCy,
		btnRfx,btnRfy, btnMrx,btnMry,
		btnUpx,btnUpy, btnDnx,btnDny, btnLfx,btnLfy, btnRtx,btnRty, btnMvx,btnMvy, btnLgtx, btnLgty,
		leftRight, sizeCase, legendClick, notMe;
    private Font f0, f1, f2, f3, f4, f5, f6, f7, f8, f9;
	double dotWidth;
    private String sfid, sfname;
	boolean mouseDown, mouseUp, legendUp;
	private Image imgMag, showMe, qMark, fingerUp, fingerDown, refImg, imgZoomin, imgZoomout, imgReload;
    public Canvas1()
    {
	     f1=new Font ("Times", Font.BOLD, 12);
	     f2=new Font ("Times", Font.PLAIN, 10);
	     f3=new Font ("MS Sans Serif (Western)", Font.PLAIN,  10);
	     f4=new Font ("Verdana", Font.PLAIN, 12);
		 f5=new Font ("Verdana", Font.PLAIN, 10);
		 f6=new Font ("Verdana", Font.PLAIN, 3);
		 f7=new Font ("Times", Font.PLAIN, 12);
		 f8=new Font ("Courier", Font.BOLD, 14);
		 f9=new Font ("Courier", Font.BOLD, 20);

		btnX0=705;
		btnY0=4;
		btnWidth=38;
		btnHight=12;
		leftRight=0;
		colPick=0;
		x0=0;
		showMeNum=0;
		legendUp=true;

		btnMvx=600;			btnMvy=32;
        btnLgtx=650;        btnLgty=32;

		btnStx=520;						btnSty=31;
		btnCpx=btnStx-40;				btnCpy=btnSty;
        btnRfx=btnX0+btnWidth*5-30;		btnRfy=btnY0+btnHight-3;
		btnMrx=800;		btnMry=30;

    }
	public void setValue(int sNum, String s1, String s2, int sLong, double dotW, Image imgRld,
		                 Image imgM, Image sMe, Image qM, Image fUp, Image fDown, Image refIm, Image zIn, Image zOut)
	{
		seqNum=sNum;
		seqNum0=sNum;
		sfid=s1;
		sfname=s2;
		seqLong=sLong;
		dotWidth=dotW;
		imgReload=imgRld;
		imgMag=imgM;
		showMe=sMe;
		qMark=qM;
		fingerUp=fUp;
		fingerDown=fDown;
		refImg=refIm;
		imgZoomin=zIn;
		imgZoomout=zOut;

	    setBackground(new Color(250,250,250));
		moreInfo=0;
		reload=0;
		moveLeft=0;
		moveRight=0;
		moveUp=0;
		moveDown=0;
		sclBack=0;
		stretch=0;
		strCmpr=1;
		clearDetail=0;
		legendClick=0;
		mouseDown=false;
	}
    public void paint( Graphics g )
    {
		g.drawImage(qMark,btnMrx-45, btnMry-17, this);
		g.setFont(f1);
		g.drawRoundRect(btnMrx-2, btnMry-13, 34, 16, 2, 2);
		g.drawString("HELP",btnMrx, btnMry);
	//	g.drawImage(refImg,btnMvx, btnMvy, 20,20,this);
		g.drawRoundRect(btnMvx, btnMvy, 34, 12, 2, 2);
		g.setFont(f2);
		g.drawString(" clean ",btnMvx+2, btnMvy+10);
		g.drawRoundRect(btnLgtx, btnLgty, 65, 12, 2, 2);
		if (legendUp==true)
		    g.drawString("hide legend",btnLgtx+5, btnLgty+10);
		else
            g.drawString("show legend",btnLgtx+4, btnLgty+10);
		g.drawRoundRect(16, btnMvy, 40, 12, 2, 2);
		g.drawString(" reload ",16+2, btnMvy+10);

	//	g.drawImage(imgReload,5, 12, this);
		g.setColor(new Color(0,0,150));
		g.setFont(f1);
		g.drawString(sfid+"", 20, 18 );
		g.setFont(f8);
	//	g.drawString(sfname+" FAMILY MEMBERS", 100, 18 );
		g.drawString(sfname+"", 80, 18 );
   //   g.setFont(f3);
	//	if (seqNum==seqNum0)
	//		g.drawString("( "+seqNum+" sequences )", ((sfname.length()+15)*8+120), 18 );
	//	else
	//		g.drawString("( "+seqNum+" / "+seqNum0+" sequences here )", ((sfname.length()+15)*8+120), 18 );
	//	g.setColor(Color.red);

        g.setFont(f3);
		if (seqNum0==1)
		{
			if (seqNum0==1)
			   g.drawString("( "+seqNum+" sequence )", ((sfname.length()+15)*8+40), 18 );
			if (seqNum==0)
			   g.drawString("( 1/1 sequence removed )", ((sfname.length()+15)*8+40), 18 );
		}
		else if (seqNum0>1)
		{
			if (seqNum0==seqNum)
			   g.drawString("( "+seqNum+" sequences )", ((sfname.length()+15)*8+40), 18 );
			else if (seqNum==seqNum0-1)
			   g.drawString("( "+ (seqNum0-seqNum) +" / "+seqNum0+" sequence removed )", ((sfname.length()+15)*8+40), 18 );
			else
			   g.drawString("( "+ (seqNum0-seqNum) +" / "+seqNum0+" sequences removed )", ((sfname.length()+15)*8+40), 18 );
		}

		g.setColor(new Color(0,0,150));
		g.setFont(f8);

if (seqLong>400)
{
		scaler(g);
		g.setColor(Color.black);
		//g.drawImage(imgMag, btnStx-25, btnSty-8, 20, 20, this);
		if (strCmpr<4)
		{
			//g.draw3DRect(btnStx, btnSty, 10, 10, true);
			//g.drawString("+", btnStx+2, btnSty+10);
			g.drawImage(imgZoomin, btnStx+2, btnSty, this);
		}
		if (strCmpr>1)
		{
			//g.draw3DRect(btnCpx, btnCpy, 10, 10, true);
			//g.drawString("_", btnCpx+2, btnCpy+4);
			g.drawImage(imgZoomout, btnCpx+2, btnCpy, this);
		}
}
		if (mouseDown==true && moreInfo==1)
		{


g.setColor(Color.black);
g.drawImage(showMe, 345, 3, 450, 40, this);
g.setFont(f4);
g.drawRect(736, 3, 16, 16);
g.drawString("X", 741, 16);

if (notMe==1)
{
    g.setColor(Color.white);
	g.fillRect(btnMrx-40, btnMry-17, 25, 12);
	g.drawString("Not me. That >>>", btnMrx-40, btnMry-17+8);
	g.setColor(Color.black);
	g.drawRect(btnMrx-40, btnMry-17, 25, 12);
}

if (showMeNum!=0)
	g.drawImage(fingerUp,360, 3, 13,13,this);
if (showMeNum!=6)
	g.drawImage(fingerDown,360, 22, 13,13,this);
if (showMeNum==0)
{
	g.drawString("* To remove a sequence from the displaying set", 385, 18);
	g.drawString("                      ------ double click on the sequence ID;",385, 33);
}
if (showMeNum==1)
{
	g.drawString("* To turn on/off a sequence name", 385, 18);
	g.drawString("                      ------ single click on its sequence ID;",385, 33);
}
if (showMeNum==2)
{
	g.drawString("* To turn on/off a superfamily name", 385, 18);
	g.drawString("                      ------ single click on the superfamily ID;",385, 33);
} 
if (showMeNum==3)
{
	g.drawString("* To turn on/off a domain/motif name and its context", 385, 18);
	g.drawString("                      ------ single click on its bar in a sequence;",385, 33);
} 
if (showMeNum==4)
{
	g.drawString("* To turn on/off only identical domains/motifs displaying (a)", 385, 18);
	g.drawString("                      ------ single click on the bar in the legend;",385, 33);
}
if (showMeNum==5)
{
	g.drawString("* To turn on/off only identical domains/motifs displaying (b)", 385, 18);
	g.drawString("                      ------ double click on a bar in a sequence;",385, 33);
}
if (showMeNum==6)
{
	g.drawString("* For best print out, use Internet Explorer", 385, 18);
	g.drawString("       or Netscape 6.0 or higher with Window 2000.",385, 33);
}
//if (showMeNum==6)
//{
//	g.drawString("* To start over again,        ------ click on", 385, 25);
//    g.drawImage(imgReload,580, -5, this);
//}

		}
		g.setColor(new Color(150,150,150));
		g.fillRect(0, 48, 850, 2);
	}
	public void scaler (Graphics g)
	{
			for (int i=200; i<30000; i+=200)
			{
				if (seqLong<i & seqLong>i-200)
				{
					//scalerBarLong=(int)((i-1)/dotWidth/2);
					scalerBarLong=(int)((i-200)*dotWidth/2);
					scalerNumBase=(i-200)/2;
					i>30000;
				}
			}
			for (int i=0; i<4; i++)
			{
				g.setColor(new Color(250,250,250));
				if (colPick==0)
				{
					colPick=1;
					g.setColor(new Color(220,220,220));
				}
				else
					colPick=0;

				g.fillRect(80+(int)(i*scalerBarLong/4/strCmpr),
					39, (int)(scalerBarLong/4/strCmpr), 5);
				g.setColor(Color.black);
				g.drawRect(80+(int)(i*scalerBarLong/4/strCmpr),
					39, (int)(scalerBarLong/4/strCmpr), 5);

			}
			g.setColor(Color.black);
            g.setFont(f5);
			if ((1+leftRight/strCmpr)>=0)
				g.drawString(""+(1+leftRight/strCmpr), 76, 38);
			if (((scalerNumBase+leftRight)/strCmpr)>=0)
			g.drawString(""+(scalerNumBase+leftRight)/strCmpr, 76+scalerBarLong/strCmpr, 38);
			g.setFont(f4);

	}

    public boolean mouseEnter( Event e, int x, int y )
    {
		xAt = x;
        yAt = y;
        if ( xAt>=btnMrx-45 & xAt<=btnMry-28 & yAt>=btnMry-17 & yAt<=btnMry-5 )
		{
			notMe=1;
			repaint();
		}
		return true;
    }
    public boolean mouseExit( Event e, int x, int y )
    {
		xAt = x;
        yAt = y;
        if ( xAt>=btnMrx-45 & xAt<=btnMry-28 & yAt>=btnMry-17 & yAt<=btnMry-5 )
		{
			mouseDown=true;
			notMe=0;
			repaint();
		}
		return true;
    }
    public boolean mouseDown( Event e, int x, int y )
    {
		mouseDown=false;
		reload=0;
        xAt = x;
        yAt = y;

	    if ( xAt>=btnLgtx & xAt<=btnLgtx+60 & yAt>=btnLgty & yAt<=btnLgty+12)
		{
			mouseDown=true;
			if (legendUp==true)
			    legendUp=false;
			else
				legendUp=true;
			legendClick=1;
			repaint();
		}
	    if ( xAt>=736 & xAt<=752 & yAt>=3 & yAt<=19 & moreInfo==1)
		{
			mouseDown=true;
			moreInfo=0;
			repaint();
		}
	    if ( xAt>=btnMrx-2 & xAt<=btnMrx+34 & yAt>=btnMry-13 & yAt<=btnMry+7)
		{
			mouseDown=true;
			moreInfo=1;
			repaint();
		}
	    if ( xAt>=20 & xAt<=40 & yAt>=28 & yAt<=44)
		{
			mouseDown=true;
			reload=1;
			strCmpr=1;
			leftRight=0;
			x0=0;
		//repaint();
		}
	    if ( xAt>=btnMvx & xAt<=btnMvx+34 & yAt>=btnMvy & yAt<=btnMvy+12)
		{
			mouseDown=true;
			clearDetail=1;
			strCmpr=1;
			leftRight=0;
			x0=0;
		//repaint();
		}
	    if ( xAt>=btnStx & xAt<=btnStx+20 & yAt>=btnSty & yAt<=btnSty+15 & strCmpr<4 & seqLong>400)
		{
			mouseDown=true;
			stretch=1;
			strCmpr*=2;
		//	repaint();
		}
	    if ( xAt>=btnCpx & xAt<=btnCpx+20 & yAt>=btnCpy & yAt<=btnCpy+15 & strCmpr>1 & seqLong>400)
		{
			mouseDown=true;
			sclBack=1;
			strCmpr/=2;
		//	repaint();
		}
/////////
	    if ( xAt>=360 & xAt<=373 & yAt>=3 & yAt<=16 & moreInfo==1 & showMeNum!=0)
		{
			mouseDown=true;
			showMeNum-=1;
			repaint();
		}
	    if ( xAt>=360 & xAt<=373 & yAt>=22 & yAt<=35 & moreInfo==1 & showMeNum!=6)
		{
			mouseDown=true;
			showMeNum+=1;
			repaint();
		}
        return true;
    }
}


//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
/////////////  2 w/ sfn //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////



class Canvas2 extends Canvas {
    public int seqNum, domNum, y00, y0, x0, domBarWidth, seqBarWidth, barDist, lineDist, lastLine, newDomNum,
		ddd[], ddd2[], downX[], leftGoIdx[], seqNameUp[], legend[][], legendShrink, sfNameUp[], lessDoman,
		xAt, yAt, ii, iii, moveArea, upDown, moveDown, moveUp, moveRight, rightShow, upShow, downShow;
    Font f1, f2, f3, f4, f5;
    String seqId[],   seqName[],  domIdTest, domIdDown, domId[][], sfId[];
	long lastDownTime = 0;
	final static long DOUBLE_CLICK_TIME = 250;
    boolean mouseDown, mouseUp, singleClick, doubleClick, seqRemove, test3[], legendUp;
	private Image upImg, downImg, leftImg;
int numOfSeqWithDomains;
    public Canvas2()
    {
	     f1=new Font ("Courier", Font.PLAIN, 11);
	     f2=new Font ("Courier", Font.BOLD,  14);
	     f3=new Font ("Courier", Font.BOLD,  12);
	     f4=new Font ("Times", Font.PLAIN, 10);
	     f5=new Font ("Times", Font.PLAIN, 8);
    }

	public void setValue(int sNum, String sId[], String sName[], int d32[], int y, String sf[], String dId[][], int dNum,
		                 int domBarW, int seqBarW, int barD, int lineD, Image upIm, Image downIm, Image leftIm, int lastL)
	{
	    seqNum=sNum;
	    seqId=new String [seqNum];
	    seqName=new String [seqNum];

		sfId=new String [seqNum];

		seqNameUp=new int [seqNum];
	    ddd=new int [seqNum];
	    ddd2=new int [seqNum];
        leftGoIdx=new int [seqNum];
		seqId=sId;
		seqName=sName;

		ddd2=d32;
		y00=y;

		sfId=sf;
        sfNameUp=new int [seqNum];

		domId=dId;
		domNum=dNum;

		domBarWidth=domBarW;
		seqBarWidth=seqBarW;
		barDist=barD;
		lineDist=lineD;
		upImg=upIm;
		downImg=downIm;
		leftImg=leftIm;
		lastLine=lastL;
		if (lastLine>400)
			upShow=1;
		else upShow=0;
		iii=0;
		x0=15;
        setBackground(Color.white);


	//	lessDoman=0;
	}
    public void paint( Graphics g )
    {
		y0=y00;
		g.setFont(f4);
        for (int i=0; i<seqNum; i++)
		{
			if (i>0)
				y0+=ddd[i-1]+ddd2[i-1];

			g.setColor(Color.black);
		//	if (seqId[i].length()>8)
		//	{
	    //        g.drawString(seqId[i].toLowerCase(), x0, y0+i*lineDist+4);
		//	} else
			    g.drawString(seqId[i], x0-3, y0+i*lineDist+4);

            if (!sfId[i].equals("SF------") && !sfId[i].equals(""))
                g.drawString("[" + sfId[i] + "]", x0, y0+i*lineDist+14);

			g.setColor(new Color(230,230,230));
			g.fillRect(10, (y0+i*lineDist-domBarWidth-barDist-(domBarWidth-seqBarWidth)/2-5), 120, 2 );
			if (y0+i*lineDist+8>480)
				upShow=1;
			else upShow=0;
		}
		if (downShow==1)
		{
            g.setColor(Color.white);
			g.fillRect(10, 0, 100, 20);
			g.drawImage(upImg, 25,0,30,10, this);
		}
		if (upShow==1)
		{
			g.setColor(Color.white);
			g.fillRect(10, 500, 100, 40);
			g.drawImage(downImg, 25,508,30,10, this);
		}
		if (rightShow==1)
			g.drawImage(leftImg, 0,160,10,30, this);
	}
    public boolean mouseDown( Event e, int x, int y )
    {
		moveArea=0;
		singleClick=false;
	//	doubleClick=false;
		xAt = x;
		yAt = y;
		seqLocation(xAt, yAt);
		iii=ii;
		if ( moveArea==2 && doubleClick==false )
		{
			if (seqNameUp[ii]<1)
				seqNameUp[ii]=1;
			else
				seqNameUp[ii]=0;
			singleClick=true;
			if (e.when-lastDownTime<DOUBLE_CLICK_TIME)
			{
				numOfSeqWithDomains=0;
				int domainExist;
				int aa=-1;
				doubleClick=false;
				for (int a=0; a<seqNum; a++)
				{
					domainExist=0;
					for (int b=0; b<domNum; b++)
					{
                        if (domId[a][b]!=null)
						{
							domainExist=1;
							aa=a;
						}
					}
					if (domainExist==1)
					{
						numOfSeqWithDomains++;
					}

				}
				if (numOfSeqWithDomains>1 || iii!=aa)
				{
					doubleClick=true;
					singleClick=false;
					seqNum--;
				}
			}
		}
		if ( moveArea==3 & !sfId[ii].equals("") & !sfId[ii].equals("SF------") )
		{
			if (sfNameUp[ii]<1)
				sfNameUp[ii]=1;
			else
				sfNameUp[ii]=0;
			singleClick=true;
		}
		lastDownTime=e.when;
		return true;
    }
    public void seqLocation (int x, int y)
    {
		y0=y00;
  	  for (int i=0; i<seqNum; i++)
	  {
		 if (i>0)
			y0+=ddd[i-1]+ddd2[i-1];
		 if ((xAt>x0 & xAt<seqId[i].length()*7+x0 & xAt<75) & (yAt>y0+(i)*lineDist-6 & yAt<y0+(i)*lineDist+4) & yAt>8 & yAt<506)
		 {
			ii=i;
			moveArea=2;  
		 }

		 if ((xAt>x0 & xAt<5+sfId[i].length()*7+x0 & xAt<70) & (yAt>y0+(i)*lineDist+6 & yAt<y0+(i)*lineDist+12) & yAt>8 & yAt<506)
		 {
			ii=i;
			moveArea=3;  
		 }
	  }
	  if (xAt>25 & xAt<55 & yAt>0 & yAt<8 & downShow==1)
	  {
		  	mouseDown=true;
			moveDown=1;
		//	repaint();
	  }
	  if (xAt>25 & xAt<55 & yAt>508 & yAt<518 & upShow==1)
	  {
		  	mouseDown=true;
			moveUp=1;
		//	repaint();
	  }
	  if (xAt>0 & xAt<10 & yAt>160 & yAt<190 & rightShow==1)
	  {
		  	mouseDown=true;
			moveRight=1;
		//	repaint();
	  }
	  return;
    }
}

//*/

//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////           //////////////
/////////////           //////////////
/////////////     3     //////////////
/////////////           //////////////
/////////////           //////////////
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////

class Canvas3 extends Canvas {
    int seqNum, xAt, yAt, moveLeft, leftShow;
    boolean mouseDown;
	private Image rightImg, upImg, downImg;

    public Canvas3()
    {
        setBackground(Color.white);
    }
	public void setValue(int sNum, Image upIm, Image downIm, Image rightIm)
	{
	    seqNum=sNum;
        rightImg=rightIm;
		upImg=upIm;
		downImg=downIm;
	}
    public void paint( Graphics g )
    {
		if (leftShow==1)
			g.drawImage(rightImg, 0,160,10,30, this);
	}
    public boolean mouseDown( Event e, int x, int y )
    {
		xAt = x;
		yAt = y;
		if (xAt>0 & xAt<10 & yAt>160 & yAt<190 & leftShow==1)
		{
		  	mouseDown=true;
			moveLeft=1;
			repaint();
		}
		return true;
    }
}

