var styleObj = 
	cytoscape.stylesheet()
	.selector('node')
		.css({
			'border-width':'0',
			'content':'data(Label)',
			'font-family': 'Tahoma, Geneva, sans-serif',
			'font-size': '9',
			'font-weight':'bold',
			'text-halign':'right',
			'text-valign':'center',
			'text-opacity':'0.9',
			'text-outline-color':'#fff',
			'text-outline-width':'2.5',
			'shape':'ellipse',
			'height': '18',
			'width': '18',
			'opacity':'1',
			'background-color':'#a6a6a6'
		})
	.selector('node[Shape="complex"]')
		.css({"shape": "rectangle"})
	.selector('node[Shape="CHEBI"]')
		.css({"shape": "triangle"})
	.selector('node[Category $= "modification"]')
		.css({
			'border-color':'#424242',
			'border-width':'2'
		})
	.selector('node[Category^="organism"]')
		.css({
			'height': '12', 
			'width': '12'
		})
	.selector('edge')
		.css({
			'font-family': 'Arial',
			'font-size': '8',
			'font-weight':'normal',
			'width':'1',
			'opacity':'0.6'
		})
	.selector('edge[Interaction="is_a"]')
		.css({
			'content':'is_a',
			'color':"#000",
			'source-arrow-shape':'triangle',
			'source-arrow-color':'#000',
			'line-color':'#000',
			'line-style':'solid'
		})
	.selector('edge[Interaction="derives_from"]')
		.css({
			'content':'derives_from',
			'color':"#000",
			'source-arrow-shape':'triangle',
			'source-arrow-color':'#000',
			'line-color':'#000',
			'line-style':'solid'
		})	
	.selector('edge[Interaction="has_component"]')
		.css({
			'content':'has_component',
			'color':"#000080",
			'target-arrow-shape':'triangle',
			'target-arrow-color':'#000080',
			'line-color':'#000080',
			'line-style':'dashed'
		})
	.selector('edge[Interaction$="interaction"]')
		.css({
			'content':'+i',
			'color':"#00cb00",
			'target-arrow-shape':'triangle',
			'target-arrow-color':'#00cb00',
			'source-arrow-shape':'triangle',
			'source-arrow-color':'#00cb00',
			'line-color':'#00cb00',
			'line-style':'solid'
		})
	.selector('edge[Interaction="dissociation"]')
		.css({
			'content':'-i',
			'color':"#00cb00",
			'target-arrow-shape':'tee',
			'target-arrow-color':'#00cb00',
			'source-arrow-shape':'tee',
			'source-arrow-color':'#00cb00',
			'line-color':'#00cb00',
			'line-style':'dashed'
		})	
	.selector('edge[Interaction$="phosphorylation"]')
		.css({
			'content':'+p',
			'color':"#ff0073",
			'source-arrow-shape':'triangle',
			'source-arrow-color':'#ff0073',
			'line-color':'#ff0073',
			'line-style':'solid'
		})
	.selector('edge[Interaction="acetylation"]')
		.css({
			'content':'+ac',
			'color':"#ff0073",
			'source-arrow-shape':'triangle',
			'source-arrow-color':'#ff0073',
			'line-color':'#ff0073',
			'line-style':'solid'
		})	
	.selector(':selected')
		.css({
			'background-image':'none',
			'background-color':'#f9ff00',
			'border-color':'#e0e500',
			'text-outline-color':'#f9ff00',
			'text-outline-opacity':'0.1',
			'text-outline-width':'3',
		})	
	.selector('edge:selected')
		.css({
			'background-color':'#f9ff00',
			'line-color':'#f9ff00',
				//'source-arrow-color':'#f9ff00',
				//'target-arrow-color':'#f9ff00',
			'width':'3',
		})	