import { Component, AfterViewInit } from "@angular/core";

declare var jQuery: any;

@Component({
	selector: 'slider-location',
	templateUrl: "./sliderlocation.component.html"
})

export class SliderlocationComponent implements AfterViewInit{
	constructor(){
		
	}

	ngAfterViewInit(){
		let self = this;
		setTimeout(function(){
			self.loadScript('/static/js/sliderlocation.js');
		}, 1500);
	}

	loadScript(url:any) {
	    jQuery('script[src="' + url + '"]').remove();
    	jQuery('<script>').attr('src', url).appendTo('body');
	}
}