const puppeteer = require('puppeteer');
const faker = require('faker');



let browser
let page

const user = {
    first_name:faker.name.firstName(),
    last_name:faker.name.lastName(),
    username:faker.name.lastName(),
    email:faker.internet.email(),
    phonenumber:faker.phone.phoneNumber()
  };

beforeAll(async () => {
    // launch browser

    browser = await puppeteer.launch()
    // creates a new page in the opened browser
    page = await browser.newPage()
})

describe('Sign up', ()=> {
    test('user sign up redirects to user login page', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignup.html');
        await page.waitForSelector('.sign-up');

        await page.click('input[id=first_name]');
        await page.type('input[id=first_name]', user.first_name);

        await page.click('input[id=last_name]');
        await page.type('input[id=last_name]', user.last_name);

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
            expect(dialog.message()).toBe('User saved successfully')
            dialog.accept();})

    }, 9000000);
    
});

afterEach(async () => {
    await browser.close()
})