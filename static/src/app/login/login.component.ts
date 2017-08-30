import { Component, ViewContainerRef, OnInit, AfterViewInit } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";
import { AlertService } from "../services/alert.service";
import { AuthenticationService } from "../services/authentication.service";
import { ToastsManager } from "ng2-toastr/ng2-toastr";
import { FacebookService, InitParams, LoginResponse } from "ngx-facebook";

declare const gapi: any;
@Component({
	selector: "login-component",
	templateUrl: "login.component.html",
	styleUrls: ['login.component.css'],
})

export class LoginComponent implements OnInit, AfterViewInit{
	returnUrl: string;
	public validate_password: boolean = true;
	public meesage_password: string = '';
	public auth2: any;
	public result: any;
	
	constructor(
		private route: ActivatedRoute,
		private router: Router,
		private authenticate: AuthenticationService,
		private alertService: AlertService,
		private toast: ToastsManager,
		private vRef: ViewContainerRef,
		private fb: FacebookService,
		){
		this.toast.setRootViewContainerRef(vRef);
	}

	ngAfterViewInit(){
		let that = this;
		setTimeout(function() {
		    gapi.load('auth2', function () {
		      that.auth2 = gapi.auth2.init({
		        client_id: '989166669078-3jetaeidl05o31hutbkalrvislqqt5ee.apps.googleusercontent.com',
		        cookiepolicy: 'single_host_origin',
		        scope: 'profile email'
		      });
		      that.attachSignin(document.getElementById('googleBtn'));
		    });

		    let initParams: InitParams = {
				appId: '129381297646323',
			    xfbml: true,
			    version: 'v2.9'
			};
			that.fb.init(initParams);
		}, 1500);
	}

	public attachSignin(element) {
	    let that = this;
	    this.auth2.attachClickHandler(element, {},
	      function (googleUser) {
	        // let profile = googleUser.getBasicProfile();
	        // console.log('access_token || ' + googleUser.getAuthResponse().access_token);
	        // console.log('Token || ' + googleUser.getAuthResponse().id_token);
	        // console.log('ID: ' + profile.getId());
	        // console.log('Name: ' + profile.getName());
	        // console.log('Image URL: ' + profile.getImageUrl());
	        // console.log('Email: ' + profile.getEmail());
	        //YOUR CODE HERE
	        that.authenticate.loginWithGoogle(googleUser.getAuthResponse().access_token).subscribe(data=>{
	        	that.authenticate.loginWithSocial(data.key, 'google').subscribe(data=>{
	        		that.alertService.success("Login success.", true);
					that.router.navigate([that.returnUrl]);
	        	}, errors=>{
					that.toast.error("Can not login with google. PLease try again!");
	        	});
	        }, errors=>{
	        	// console.log(errors);
	        	that.toast.error("Can not login with google. PLease try again!");
	        });

	      }, function (error) {
	        // alert(JSON.stringify(error, undefined, 2));
	    });
	}

	loginTwitter(){
		window.location.href = 'accounts/twitter/login/';
	}

	loginFB(){
		this.fb.login().then((response: LoginResponse) => {
			this.authenticate.loginWithFacebook(response.authResponse.accessToken).subscribe(data=>{
				this.authenticate.loginWithSocial(data.key, 'facebook').subscribe(data=>{
					this.alertService.success("Login success.", true);
					this.router.navigate([this.returnUrl]);
				}, errors=>{
					console.error(errors);
					this.toast.error("Can not login with facebook. PLease try again!");
				});
			}, errors=>{
				console.error(errors);
				this.toast.error("Can not login with facebook. PLease try again!");
			});
		})
		.catch((error: any) => {
			console.error(error);
			this.toast.error("Can not login with facebook. PLease try again!");
		});
	}

	ngOnInit() {
		this.authenticate.logout();
		this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
	}
	login(value:any) {
		this.authenticate.login(value).subscribe(data=>{
			this.alertService.success("Login success.", true);
			this.router.navigate([this.returnUrl]);
		}, error=>{
			this.toast.error("Username or password incorrect!", "Login fail!");
		});
	}

	changepassword(f:any, password:any){
		this.validate_password = true;
		this.meesage_password = '';
		if (f.username == password){
			this.validate_password = false;
			this.meesage_password = 'Password must be different from Username! Try again.';
			return ;
		}
		if (password.length < 8){
			this.validate_password = false;
			this.meesage_password = '';
			return ;
		}
		let re = /[0-9]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one number (0-9)!';
			return;
		}
		re = /[a-z]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one lowercase letter (a-z)!';
			return ;
		}
		re = /[A-Z]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one uppercase letter (A-Z)!';
			return;
		}
	}
}