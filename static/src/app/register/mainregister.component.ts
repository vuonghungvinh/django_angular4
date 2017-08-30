import { Component } from "@angular/core";
import { Router } from "@angular/router";

@Component({
	selector: "main-register-component",
	templateUrl: "mainregister.component.html",
	styleUrls: ['../login/login.component.css']
})

export class MainRegisterComponent{
	public type: any=1;

	constructor(private _router:Router){}

	continue() {
		if (this.type == 1){
			this._router.navigate(['register/individual']);
		} else {
			this._router.navigate(['register/business']);
		}
	}
}