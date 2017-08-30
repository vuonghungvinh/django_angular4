import { Injectable } from "@angular/core";
import { Router } from "@angular/router";
import { RequestOptions, Headers } from "@angular/http";
@Injectable()
export class CommonService{
	constructor(private router: Router){

	}

	getUrl(){
		return this.router.url;
	}

	public jwt() {
        let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
            let headers = new Headers({ 'Authorization': 'Token ' + currentUser.api_token });
            return new RequestOptions({ headers: headers });
        }
    }

    public jwt_social(token: any) {
        if (token) {
            let headers = new Headers({ 'Authorization': 'Token ' + token });
            return new RequestOptions({ headers: headers });
        }
    }
}