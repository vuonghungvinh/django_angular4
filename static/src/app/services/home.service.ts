import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";

@Injectable()
export class HomeService{
	constructor(private _http:Http){}

	BCategories(): Observable<any[]>{
		return this._http.get("api/business/category/").map(response=>response.json());
	}

	AdNames(): Observable<any[]>{
		return this._http.get("api/products/latest/").map(response => response.json());
	}

	getCities(country: any):Observable<any[]>{
		return this._http.post("api/city/list/", {'country': country}).map(response=>response.json());
	}
}