import { Component, ViewContainerRef } from "@angular/core";
import { RegisterService } from "../services/register.service";
import { ToastsManager } from "ng2-toastr/ng2-toastr";
import { AlertService } from "../services/alert.service";
import { Router } from "@angular/router";

@Component({
	selector: "individual-component",
	templateUrl: "individual.component.html",
	styleUrls: ['../login/login.component.css'],
	providers: [RegisterService]
})

export class IndividualComponent{
	public validate_password: boolean = true;
	public meesage_password: string = 'here';

	constructor(
		private registerService: RegisterService, 
		private toastr: ToastsManager, 
		private vRef: ViewContainerRef,
		private alert: AlertService,
		private _router: Router){
		this.toastr.setRootViewContainerRef(vRef);
	}

	registerForm(f:any){
		let self = this;
		this.registerService.registerIndividual(f).subscribe(data=>{
			this.alert.success("Register Individual success.", true);
			this._router.navigate(['login']);
		},error=>{
			let errors = error.json();
			let error_msg = '';
			if (errors.email){
				for (let i=0; i<errors.email.length; i++){
					if (error_msg == ''){
						error_msg = errors.email[i];
					} else {
						error_msg += "</br>"+ errors.email[i];
					}
				}
			}
			if (errors.username){
				for (let i=0; i<errors.username.length; i++){
					if (error_msg == ''){
						error_msg = errors.username[i];
					} else {
						error_msg += "</br>"+ errors.username[i];
					}
				}
			}
			if (errors.password){
				for (let i=0; i<errors.password.length; i++){
					if (error_msg == ''){
						error_msg = errors.password[i];
					} else {
						error_msg += "</br>"+ errors.password[i];
					}
				}
			}
			self.toastr.error(error_msg, "Error", {enableHTML: true});
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