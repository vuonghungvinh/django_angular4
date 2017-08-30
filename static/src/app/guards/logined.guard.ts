import { Injectable } from "@angular/core";
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, CanDeactivate } from "@angular/router";
import { AlertService }  from "../services/alert.service";

@Injectable()
export class LoginGurad implements CanActivate{
	constructor(private router: Router, private alertService: AlertService){

	}
	canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
		if (localStorage.getItem("currentUser")){
			this.alertService.success("You are logined.", true);
			this.router.navigate(['/']);
			return false;
		}
		return true;
	}
}