import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";

@Injectable()
export class TopsearchService{
	constructor(private _http:Http){}

	searchMarketplace(key:string, cur:number): Observable<any[]>{
		return this._http.post("api/home/search/", {'type': 'marketplace', 'key': key, 'cur': cur}).map(responsive => responsive.json());
	}
}