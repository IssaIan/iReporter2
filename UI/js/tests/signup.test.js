const puppeteer = require('puppeteer');
const faker = require('faker');
const assert = require('assert');



let browser
let page


const user = {
    firstname:faker.name.firstName(),
    lastname:faker.name.lastName(),
    phonenumber:faker.phone.phoneNumber(), 
    email:faker.internet.email(),
    username:faker.name.firstName()
  };

beforeEach(async () => {
    // launch browser

    browser = await puppeteer.launch()
    // creates a new page in the opened browser
    page = await browser.newPage()
})

describe('Sign up', ()=> {
    it('user can register', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignup.html');
        await page.waitForSelector('.sign-up');

        await page.click('input[id=first_name]');
        await page.type('input[id=first_name]', user.firstname);

        await page.click('input[id=last_name]');
        await page.type('input[id=last_name]', user.lastname);

        await page.click('input[id=username]');
        await page.type('input[id=username]', user.username);

        await page.click('input[id=email]');
        await page.type('input[id=email]', user.email);

        await page.click('input[id=phonenumber]');
        await page.type('input[id=phonenumber]', user.phonenumber);

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'Maina9176');

        await page.click('input[id=confirm_password]');
        await page.type('input[id=confirm_password]', 'Maina9176');

        await page.click('input[type=submit]');

        page.on('dialog', dialog => {
            assert.equal(dialog.message(), 'User successfully saved')
            dialog.accept();
        })
    }, 9000000);
    
});

afterEach( async () => {
    await browser.close();
  });