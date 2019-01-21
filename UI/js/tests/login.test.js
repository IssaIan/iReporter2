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

describe('Login', ()=> {
    test('user login redirects to user account', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignin.html');
        await page.waitForSelector('.login');

        await page.click('input[id=username]');
        await page.type('input[id=username]', 'admin');

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'adminuser');
        
        await page.click('input[type=submit]');

        expect(window.alert).toBe("Welcome admin. You are now logged in!")

    }, 9000000);
    
});

describe('Invalid login credentials', ()=> {
    test('Test wrong username returns an error', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignin.html');
        await page.waitForSelector('.login');

        await page.click('input[id=username]');
        await page.type('input[id=username]', 'unnamed');

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'cufubbcinrcur');
        
        await page.click('input[type=submit]')

        expect(window.alert).toBe("No user with that username found!");

    }, 9000000);
    
});

afterAll(() => {
    browser.close()
})