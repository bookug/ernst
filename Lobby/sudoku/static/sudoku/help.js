/*=============================================================================
# Filename: help.js
# Author: syzz
# Mail: 1181955272@qq.com
# Last Modified: 2015-07-02 21:24
# Description: just for sudoku game 
=============================================================================*/

function form_check_submit()
{
	//alert("sbsbs");
	$("#form_check").submit();
}

function form_answer_submit()
{
	$("#form_answer").submit();
}

var intervalId = 0;    //time counter
var xy = "";
$(document).ready(
		function () 
		{
			$(document).mousemove(
					function (e) 
					{
						xy = e.screenX + ":" + e.screenY;
					});
			intervalId=window.setInterval("TimeGo()", "1000");
			var resizeTimer = null;
			$(window).resize(
					function() 
					{
						if($(window).height()>500)
						{
							if (intervalId) clearInterval(intervalId);
							intervalId=window.setInterval("TimeGo()", "1000");
						}
						else
						{
							if(intervalId) clearInterval(intervalId);
						}
					});
		});
function isMinStatus() 
{
	var isMin = false;
	if (window.outerWidth != undefined) 
	{
		isMin = window.outerWidth <= 160 && window.outerHeight <= 27;
	}
	else 
	{
		isMin = window.screenTop < -30000 && window.screenLeft < -30000;
	}
	return isMin;
}
var ss=0, mm=0, hh=0;	//initialize
var studyTime=0;
var locations = "";
var Pre_Time = 1800;
var time = 0;
var _time = Pre_Time;
function TimeGo() 
{
	if(isMinStatus())
	{

	}
	else
	{
		if (locations == xy) 
		{
			time++;
			_time--;
			if (time > Pre_Time) 
			{
				// alert("离开时间:" + time);
				// clearInterval(intervalId);
			}
			else 
			{
				TimeAdd();               
			}
		}
		else
		{
			if (time > Pre_Time) 
			{
				alert("leave time:" + time+"s");
			}
			time = 0;
			locations = xy;
			_time = Pre_Time;
			TimeAdd();
		}
	}
}
function TimeAdd()
{
	ss++; 
	if(ss>=60) 
	{ 
		mm+=1; 
		ss=0; 
	}   
	if(mm>=60) 
	{
		hh+=1; 
		mm=0; 
	}
	ss_str = (ss < 10 ? "0" + ss : ss); 
	mm_str = (mm < 10 ? "0" + mm : mm); 
	tMsg = hh + ":" + mm_str + ":" + ss_str; 
	document.getElementById("usetime").value = tMsg; 
	setTimeout( "TimeGo()",1000); //call self every second
}

