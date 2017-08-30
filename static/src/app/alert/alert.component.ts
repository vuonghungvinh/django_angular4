import { Component, OnInit } from '@angular/core';
 
import { AlertService } from '../services/alert.service';
 
@Component({
    selector: 'alert',
    templateUrl: 'alert.component.html',
    styleUrls: ['alert.component.css']
})
 
export class AlertComponent {
    message: any;
 
    constructor(private alertService: AlertService) { }
 
    ngOnInit() {
        this.alertService.getMessage().subscribe(message => { this.message = message; });
    }
    closeAlert() {
    	this.message = null;
    }
}