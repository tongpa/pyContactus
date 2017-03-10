var app = angular.module('Contactus', ['ngTouch', 'ngAnimate',  'pascalprecht.translate', 'ngCookies', 'ngAnimate', 'ngValidate']);

	app.controller('ContactusData', function($scope, $http, $translate, $window){
		$window.changLang=function(langKey){
			console.log('changLang');
			$translate.use(langKey);
			$translate.refresh(langKey);
		};	
		
		$scope.url = '';
		$scope.formData = {
				reporter: '',
				email:'',
				optionProject:'',
				message:'',
				telephone:''
		};
		
		$scope.resetFormData = function(){
			$scope.formData = {
					reporter: '',
					email:'',
					optionProject:'',
					message:'',
					telephone:''
			};
		}
		
		$scope.init = function(url){
			$scope.url = url;
			
		};
		
		$scope.validationOptions = {
				rules:{
					reporter:{
						required: true
					},
					email: {
						required: true,
						email: true
					},
					message: {
						required: true,
						//alphanumeric: true,
						minlength: 2
					}
				},
				messages: {
					reporter:{
						required: function() { return window.langData.translate('msg_enter_your_name'); }
					},
					email :{
						required: function() { return window.langData.translate('msg_enter_your_email'); } ,
						email: function() { return window.langData.translate('msg_valid_email');} 
						 
					},
					message :{
						required: function() { return window.langData.translate('msg_enter_your_message'); } ,
						minlength: function() {return window.langData.translate('Your username must consist of at least 2 characters'); }
					}
				}
				,errorElement: 'em',
				errorPlacement: function ( error, element ) {
					error.addClass( "help-block" );
					if ( element.prop( "type" ) === "checkbox" ) {
						error.insertAfter( element.parent( "label" ) );
					} else {
						error.insertAfter( element );
					}
				},
				highlight: function (element, errorClass, validClass) {
					$( element ).parents( ".form-group" ).addClass( "has-error" ).removeClass( "has-success" );
	            },
				unhighlight: function (element, errorClass, validClass) {
					$( element ).parents( ".form-group" ).addClass( "has-success" ).removeClass( "has-error" );
				}
			};
		
		 
		
		var classheader=function(ch){
			if(ch.toLowerCase()=='warning'){
				return'header-warning';}
			else{if(ch.toLowerCase()=='error'){
					return 'header-error';}
				else{return 'header-info';}
				}
			};
		
			var textheader=function(th){ 
				if(th!=null){return th;}
				else{return "Inforamation";}
			};
			
		$scope.addTextModal = function(g, status, header, message){
			var param = {
					status : status,
					header : header,
					message : message
			};
			
			if (!param){ 
			return false;}
			var j=document;
			var divDialog = j.getElementById(g);
			var n=j.createElement("div");
			n.id = "myModal";
			n.setAttribute("class","modal fade");
			n.setAttribute("role","dialog");
			n.setAttribute("tabindex","-1");
			
			var dialog=j.createElement("div");
			dialog.setAttribute("role","document");
			dialog.setAttribute("class","modal-dialog");
			n.appendChild(dialog);
			divDialog.appendChild(n); 
			
			
			var content=j.createElement("div");
			content.setAttribute("class","modal-content");
			dialog.appendChild(content);
			
			var header= j.createElement("div");
			header.setAttribute("class","modal-header "+classheader(param.status));
			content.appendChild(header); 
			
			var buttonclose =j.createElement("BUTTON");
			buttonclose.setAttribute("class","close");
			buttonclose.setAttribute("data-dismiss","modal");
			
			var t= document.createTextNode("x");
			buttonclose.appendChild(t);
			
			var h4=j.createElement("h4");
			h4.setAttribute("class","modal-title");
			var theader = document.createTextNode(textheader(param.header));
			h4.appendChild(theader);
			
			header.appendChild(buttonclose);
			header.appendChild(h4);
			
			var body=j.createElement("div");
			body.setAttribute("class","modal-body");content.appendChild(body); 
			
			var body_p=j.createElement("p");
			body_p.setAttribute("class","p-body");
			body.appendChild(body_p); 
			
			var t_body=j.createTextNode(param.message);
			body_p.appendChild(t_body); 
			
			var footer=j.createElement("div");
			footer.setAttribute("class","modal-footer");
			content.appendChild(footer); 
			
			var buttonclose1=j.createElement("BUTTON");
			buttonclose1.setAttribute("class","btn btn-default");
			buttonclose1.setAttribute("data-dismiss","modal");
			
			var tbuttonclose1=j.createTextNode("Close");
			buttonclose1.appendChild(tbuttonclose1);
			footer.appendChild(buttonclose1);
	}   
		
		$scope.saveContactUs = function(form) {			
			if(form.validate()) {				
				$http.post($scope.url,$scope.formData).then(
					function(response){
						if (response.status == 200 && response.data.status == true){
							console.log(response.data.message);							
							$scope.resetFormData();
							$scope.addTextModal("flash", "info", response.data.header, response.data.message);
							var webflash = window.webflash({"id": "flash", "name": "webflash"});
						    webflash.render(); $('#myModal').modal('toggle');
						}						
					},
					function(response){
						
						$scope.addTextModal("flash","error", "error", "Error Connection");
						var webflash = window.webflash({"id": "flash", "name": "webflash"});
					    webflash.render(); $('#myModal').modal('toggle');
					}
				);
			}
	    };
	});
	
	app.config( function($translateProvider){
		$translateProvider.useUrlLoader('/script/loadLangJquery');	 
		$translateProvider.preferredLanguage('th');	 
		$translateProvider.useCookieStorage();
	});
	/*
	app.config(function ($validatorProvider) {
        $validatorProvider.setDefaults({
            errorElement: 'span',
            errorClass: 'help-block'
        });
    });*/