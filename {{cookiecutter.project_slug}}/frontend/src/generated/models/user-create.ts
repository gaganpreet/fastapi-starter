/* tslint:disable */
/* eslint-disable */
/**
 * {{cookiecutter.project_name}}
 * {{cookiecutter.project_name}} API
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */



/**
 * 
 * @export
 * @interface UserCreate
 */
export interface UserCreate {
    /**
     * 
     * @type {string}
     * @memberof UserCreate
     */
    'email': string;
    /**
     * 
     * @type {string}
     * @memberof UserCreate
     */
    'password': string;
    /**
     * 
     * @type {boolean}
     * @memberof UserCreate
     */
    'is_active'?: boolean | null;
    /**
     * 
     * @type {boolean}
     * @memberof UserCreate
     */
    'is_superuser'?: boolean | null;
    /**
     * 
     * @type {boolean}
     * @memberof UserCreate
     */
    'is_verified'?: boolean | null;
}

