import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";

@Injectable()
export class RegisterService{
	constructor(private _http:Http){}

	registerIndividual(data: any): Observable<any>{
		return this._http.post("api/accounts/registerindividual/", data).map((responsive)=>responsive.json());
	}

	registerBusiness(data: any): Observable<any>{
		return this._http.post("api/accounts/registerbusiness/", data).map(responsive=>responsive.json());
	}                                                                                                     
}