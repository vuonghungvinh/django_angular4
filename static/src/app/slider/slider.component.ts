import { Component, Input, OnInit, AfterViewInit, AfterContentChecked, ViewChildren, QueryList } from "@angular/core";

import * as $ from 'jquery';

@Component({
	selector: "slider-component",
	templateUrl: "./slider.component.html"
})

export class SliderComponent implements OnInit, AfterViewInit{
	@Input('adnames') adnames: any[];
	@Input('text1') text1: String;
	@Input('text2') text2: String;

	@ViewChildren('allTheseThings') things: QueryList<any>;

	ngOnInit(){
		
	}

	ngAfterViewInit(){
		this.things.changes.subscribe(t => {
	      this.renderComplete();
	    })	
	}

	renderComplete(){
	}
}