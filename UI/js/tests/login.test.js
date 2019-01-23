const puppeteer = require('puppeteer');


let browser
let page

beforeEach(async () => {
    // launch browser

    browser = await puppeteer.launch()
    // creates a new page in the opened browser
    page = await browser.newPage()
})

describe('Login', ()=> {
    it('user login redirects to user account', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignin.html');
        await page.waitForSelector('.login');

        await page.click('input[id=username]');
        await page.type('input[id=username]', 'admin');

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'adminuser');
        
        await page.click('input[type=submit]');

        page.on('dialog', dialog => {
            expect(dialog.message()).toBe('Welcome admin. You are now logged in!')
            dialog.accept();})

    }, 9000000);
    
});

describe('Invalid login credentials', ()=> {
    it('Test wrong username returns an error', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/usignin.html');

        page.on('dialog', dialog => {
            expect(dialog.message()).toBe('No user with that username found!')
            dialog.accept();});
            
        await page.waitForSelector('.login');

        await page.click('input[id=username]');
        await page.type('input[id=username]', 'unnamed');

        await page.click('input[id=password]');
        await page.type('input[id=password]', 'cufubbcinrcur');
        
        await page.click('input[type=submit]');

    }, 9000000);
    
});

afterEach(async () => {
    await browser.close()
})