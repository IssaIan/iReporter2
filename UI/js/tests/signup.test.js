const puppeteer = require('puppeteer');


let browser
let page

beforeAll(async () => {
    // launch browser

    browser = await puppeteer.launch(
        {
            headless: false,
            args:['--no-sandbox'],
            slowMo: 250,
        }
    )
    // creates a new page in the opened browser
    page = await browser.newPage()
})

describe('Sign up', ()=> {
    test('user sign up redirects to user login page', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignup.html');
        await page.waitForSelector('.sign-up');

        await page.click('input[id=first_name]');
        await page.type('input[id=first_name]', 'issa');

        await page.click('input[id=last_name]');
        await page.type('input[id=last_name]', 'mwangi');

        await page.click('input[id=username]');
        await page.type('input[id=username]', 'adminissa');

        await page.click('input[id=email]');
        await page.type('input[id=email]', 'issaadmin@gmail.com');

        await page.click('input[id=phonenumber]');
        await page.type('input[id=phonenumber]', '0712376546');

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'Maina9176');

        await page.click('input[id=confirm_password]');
        await page.type('input[id=confirm_password]', 'Maina9176');
        
        await page.click('input[type=submit]');

        expect(window.alert).toBe("User saved successfully")

    }, 9000000);
    
});