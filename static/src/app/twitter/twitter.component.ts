import { Component, AfterViewInit } from "@angular/core";
import { Router, NavigationCancel } from '@angular/router';
import { URLSearchParams, } from '@angular/http';
import { AuthenticationService } from "../services/authentication.service";
import { AlertService } from "../services/alert.service";

@Component({
	selector: "twitter-component",
	template: "<h1>Proccessing...",
	providers: [AuthenticationService]
})

export class TwitterComponent implements AfterViewInit{

	constructor(
		public router: Router,
		private auth: AuthenticationService,
		private alertService: AlertService) {
	    
	}

	ngAfterViewInit(){
		this.router.events.subscribe(s => {
	        let params = new URLSearchParams(s['url'].split("?")[1]);
	        let oauth_token = params.get('oauth_token');
	        let oauth_token_secret = params.get('oauth_token_secret');

	        if (oauth_token && oauth_token_secret){
	        	this.auth.loginWithTwitter(oauth_token, oauth_token_secret).subscribe(data=>{
		        	this.auth.loginWithSocial(data.key, 'twitter').subscribe(data=>{
						this.alertService.success("Login success.", true);
						this.router.navigate(['/']);
					}, errors=>{
						// console.error(errors);
						this.alertService.error("Can not login with twitter. PLease try again!", true);
						this.router.navigate(['/login']);
					});
		        }, errors=>{
		        	// console.log(errors);
		        	this.alertService.error("Can not login with twitter. PLease try again!", true);
					this.router.navigate(['/login']);
		        });
	        }
	    });
	}

}