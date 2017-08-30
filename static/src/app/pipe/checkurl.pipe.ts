import { Pipe, PipeTransform } from "@angular/core";

@Pipe({name: "checkurl"})
export class CheckurlPipe implements PipeTransform{
	transform(value:string):string{
		if (value.indexOf("http") >= 0){
			value = value.substr(value.indexOf("http"), value.length);
		}
		value = value.replace(/%3A/g, ':/').replace(/%3F/g,'?').replace(/%3D/g,'=').replace(/%26/g,'&');
		return value;
	}
}