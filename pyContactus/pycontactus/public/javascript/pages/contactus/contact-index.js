var app = angular.module('Contactus', ['ui.grid', 'ngTouch', 'ngAnimate', 'ui-listView', 'pascalprecht.translate', 'ngCookies']);
	app.controller('ContactusData', function($scope, $http, $translate, i18nService, $window){
		$window.changLang=function(langKey){
			console.log('changLang');
			$translate.use(langKey);
			$translate.refresh(langKey);
		};	
		
		$scope.init = function(){
			language.init();
		};
		
		
		$("#contactus-form").validate({
			rules:{
				email: {
					required: true,
					minlength: 2
				},
				message: {
					required: true,
					minlength: 2
				}
			},
			messages: {
				email :{
					required: function() { return window.lang.translate('msg_enter_your_email'); } ,
					minlength: function() {return window.lang.translate('Your username must consist of at least 2 characters'); }
				},
				message :{
					required: function() { return window.lang.translate('msg_enter_your_message'); } ,
					minlength: function() {return window.lang.translate('Your username must consist of at least 2 characters'); }
				}
			},
			errorElement: 'em',
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
		});		
		
		
		$scope.saveContactUs = function() {
			console.log("saveContactUs");
	    };
	
		   
	
	    
	});
	
	app.config( function($translateProvider){
		$translateProvider.useUrlLoader('/script/loadLangJquery');	 
		$translateProvider.preferredLanguage('th');	 
		$translateProvider.useCookieStorage();
	});