import { Injectable } from "@angular/core";
import { Http, Headers, Response, RequestOptions } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";
import { CommonService } from "./common.service";

@Injectable()
export class AuthenticationService {
	constructor(
		private _http: Http,
		private cmservice: CommonService){

	}
	login (data: any) {
		return this._http.post('api/accounts/api-token-auth/', data).map((response: Response)=>{
			let user = response.json();
			user['type']="normal";
			if (user && user.api_token) {
				localStorage.setItem('currentUser', JSON.stringify(user));
			}
		});
	}

	loginWithFacebook(access_token: any):Observable<any>{
		return this._http.post("api/accounts/rest-auth/facebook/", {'access_token': access_token}).map(response => response.json());
	}

	loginWithGoogle(access_token: any):Observable<any>{
		return this._http.post("api/accounts/rest-auth/google/", {'access_token': access_token}).map(response => response.json());
	}

	loginWithTwitter(access_token: any, token_secret: any):Observable<any>{
		return this._http.post("api/accounts/rest-auth/twitter/", {'access_token': access_token, 'token_secret': token_secret}).map(responsive=>responsive.json());
	}

	loginWithSocial(token:any, type:any):Observable<any>{
		return this._http.post('api/accounts/login-with-social/', {}, this.cmservice.jwt_social(token)).map((response: Response)=>{
			let user = response.json();
			user['type']=type;
			if (user.user && user.user.individual_user){
				let avatar_url = user.user.individual_user.avatar.replace(/%3A/g, ":/").replace(/%3F/g, "?").replace(/%3D/g, "=").replace(/%26/g, '&');
				user.user.individual_user.avatar = avatar_url.substring(avatar_url.indexOf("http"), avatar_url.length);
			}
			if (user && user.api_token) {
				localStorage.setItem('currentUser', JSON.stringify(user));
			}
		});
	}

	logout() {
	 	localStorage.removeItem("currentUser");
	}

	checkLogin() {
		let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
        	return true;
        } else {
        	return false;
        }
	}

	getUser() {
		let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
        	return currentUser;
        } else {
        	return {};
        }
	}
}