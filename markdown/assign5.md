# Assignment 5....now with better formatting...

## BEFORE YOU DO ANYTHING
Currently, some people don't have their local git settings set properly, so it's not registering them as making changes (ask me personally if you're curious).
To fix this, type this in bash (terminal or whatever you use)
`git config --global user.name "your full name"`
`git config --global user.email "your github email address"`

Be sure to type in the email address you use for github. This will make life a lot easier.

## Hello World Interfaces

Well people, we've finally gotten there. Time to fire up Xcode (which you might have already used with Assignment 4) and begin our first foray into interfaces. But before we jump too far, I'd like to try to explain how interfaces in Xcode work. I will try to explain them using the best analogy of which I can think (yeah grammar).

Say you had a hippogriff named Bessie and you wanted to control Bessie with a Lego NXT Brick (you sick, sick being). You want to make Bessie goForward, flyUp, pooOnCommand, and hippogriffScreech.
You start off by writing your 4 functions in your NXT brick. But how will the brick know where and on what to run your functions? Well, as you had to do with the previous Chimera that you programmed, you have to hook up your brick to Bessie's outlets.
Let's say Bessie had outlets wings, leftLeg1, and leftLeg2 (sadly Bessie suffered a tragic accident resulting in the loss of her right side legs). If you wanted to write a goForward function for Bessie, you would have to tell her leftLeg1 and leftLeg2 to move back in forth (and do a good amount of fancy physics to get her to actually progress forward......poor, poor Bessie). However, if you do not PHYSICALLY CONNECT the leftLeg1 and leftLeg2 to the NXT brick, they will not work AT ALL. You can write all the functions you want, but if you don't actually connect the outlet on Bessie to the input on the NXT brick, nothing will work.

This very accessible and simple to understand example is a very unsurprisingly apt description how Xcode works with interfaces and code. When creating an iOS app, you build the interface and write code in separate files. The interface file is a GUI that lets you build your....GUI. You can drag and drop elements onto the screen and see them created on your iOS app. But how do you connect your interface with your code? 

### Connecting interface with code
#### Ride on Bessie, Ride on

The difference between the analogy given and Xcode is that, instead of having "Output 1", "Output 2", etc on an NXT brick, your code can have unlimited connections.
Likewise, your interface can have unlimited outlets. Therefore, you must add and name the outlets in your interface. YOU ALSO MUST ADD THE OUTLETS TO YOUR CODE. Then you must link the two together. Simply adding the outlets to the interface or the code will not link them. You must physically drag the connection from the interface outlet to your code. Luckily, Xcode makes this pretty easy.

Create an Single View Application (under iOS) in Xcode (Organization Identifiers and stuff don't matter. Just make sure the Language is Objective-C and Core Data is unchecked). Xcode will open up to the Project Settings file (this can be accessed by clicking on the file at the top of the Project Navigator located on the left hand side of the screen). 
The files you should be concerned about currently are the ViewController.h, ViewController.m, and Main.stroyboard (if you don't have these three files, you created the wrong kind of project. Do it again...).

### MVC in a nutshell
Objective-C works using the Model View Controller Paradigm (google it for more info). Basically, the Model is what stores your data, the view is what displays your data (or whatever), and the controller is what facilitates the connection between the two. In Objective-C, the controller is a class that you create. The model is some data that is usually a property of the controller. The view is your interface. 
Since we created a "Single View Application", Xcode has created our single view (stored in Main.storyboard), our controller class (ViewController.h and .m), and our "main" function (stored in AppDelegate). We must create the model ourselves.

Note: You almost never need to modify the AppDelegate. Always modify your existing classes or create new ones. 

As a starter in interfaces, we are going to create an app that "displays" some text.
First, let's create our model. Add an `NSString *textToDisplay` property to our ViewController class

```objective-c
// In ViewController.h

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property NSString *textToDisplay;

@end
```

This will store our desired string to display. Now we have to have an outlet in which to display it.
Click on the Main.storyboard file. 
You will see a "scene" that contains an object title "View Controller". This is our view controller. (you can click on the buttons in the top right of Xcode to show and hide panels).

Note: This View Controller in our storyboard is an "instance" of the ViewController class we created. Usually, we would have to set the class of any storyboard element we create by going to it's properties and setting it's class. More on that in a different assignment.
Note++: The square on screen is not the ViewController. That is the view, which is a property of the view controller (you can see the hierarchy in the left column under "View Controller Scene"). 

Let's add a label to our scene. In the bottom right corner, you should be able to scroll through available objects. Scroll to the "Label" and drag it onto our view.
Now, we must recognize what we have done.
All we did was add an element into the view (we could also say that this is adding an outlet). We have NOT added the identification of the outlet into our code, and we have NOT linked the two together. It is **very important** to understand this distinction as not understanding this concept is why many problems arise when designing interfaces. 

We have created our outlet. We must now identify it in our code (our controller).
To identify an outlet to our controller, we use the following syntax
`@property (weak, nonatomic) IBOutlet typeOfElement *myElementName;`
For our label example, it would be
`@property (weak, nonatomic) IBOutlet UILabel *mainLabel;`
You can name the element whatever you would like. Don't worry about the (weak, nonatomic). They deal with memory management. Google for more info. 

Now we have added our outlet to our interface and we have identified it in code. However, we have not linked the element to the code (you gotta plug Bessie into the brick!). In order to connect our storyboard outlet to our identifier, we must drag a connection line between them. 
Open the storyboard and click on the Butler looking icon in the top right of the screen. This opens the Assistant editor. Make sure the file selected in the assistant editor is the ViewController.h file. You can click on the file name at the top of the assistant editor to change the file selected. 
If you wrote your method name properly, there should be a little empty circle next to your IBOutlet property. In order to connect the identifier to the element, simply click and drag inside the empty circle to the element in the view. If connected properly, the empty circle should become filled in. You have now successfully created an outlet, an identifier, and linked them.

#### TL;DR for Interface building
* Create outlet (drag element) in storyboard
* Create identifier in controller class
* Link the two 

#### Shortcuts
Xcode actually makes life easier by adding a quicker way for adding interface elements. After you've added a new element to storyboard, open the Assistant editor (making sure the header file of the view controller is selected). You can ctrl-drag from the element to the header file (inbetween the @interface and @end tags) and a little popup menu will appear. Make sure to choose Outlet from the Connection menu and name it something that is useful. Leave everything else the same. When you press connect, Xcode will add the required identifier to your code AND link them together (note the filled in circle next to the identifier). This is what I always use, but it is still imperative to understand what it is actually doing so that you can troubleshoot later. 

### Finally......the actual assignment
The way to add an "action" is the same way as adding an outlet with a few differences. When you ctrl-drag from an element (if the element can recieve an action, like a button), change the Connection from Outlet to Action. Then, give the method a name (not like buttonPressed, but rather something indicating what the button press actually does).
Note: when you add an action with ctrl-drag, it adds the method in the header file AND the template method implementation in the implementation file. Neat?

Add a button that, when pressed, changes the text of the text label to the text stored in our textToDisplay string. That's it. Just do it. 

#### Do it for Bessie

### Goals
* Fully understand how adding and linking elements works in interface builder
* Give Bessie wings
* Be able to add elements and actions as well as code to make them do stuff
* Understand the basic MVC model
* Be more awesome.

Alright. That was long. Time to cry a little.