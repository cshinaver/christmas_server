# Assignment 7
## Storyboards ie. Multiple View Apps

Well team, this is it (more or less).
After you understand storyboards, most everything builds from that.
Everything else in iOS can be understood with a few lookups in the documentation, a few browsethroughs of example code files, and some tears...  
**BUT GOOD SIRS AND MESDAMES** , there are much fewer tears than before, for now you have the **WARHAMMER OF DESTINY**. Well, currently you have the Craftsman © Nail Hammer of Mediocre Crafsmanship, but if you continue in your mobile app learnings and what the Good Lord has given you (ie. de Google) your Mediocre Hammer will grow into a **WARHAMMER OF DESTINY**.
### MAY SHE FOREVER REIGN TO SLAY THINE ENEMIES (eg. Windows Phone)

Enough of that now. On to Storyboards.

Storyboards are the foundation for any Multiview iOS app. Not only do you create paths between your different views in your Storyboard, but you also see a visual representation of how your app will flow. This visual representation can be very helpful when showing future clients how your app behaves as well as working with others that might help in the design process (eg. graphic design artists, business people, etc). 

## Scenes and Segues
Scenes and segues are the words used to refer to the different views and transitions in your app. The iPhone has only one window. That window does not change when different apps are opened. That window also doesn't change when different scenes in an app come up. A scene is merely a view controller hooked up to a custom class. In a single view application (like all the apps that we have created), there is only one scene. If you created an app that had a tableview and clickable rows that would transition to another view when selected, that app would have two scenes, one with the tableview and one with the content displayed when a row was selected in the tableview. Segues are another word for transitions between scenes. 

Let's create a basic storyboard to demo right now.

1. Open up a new Single View Application in Xcode. Your app should have one storyboard with one custom View Controller (these are created automatically when you choose the Single View Application template). 

2. Open up the storyboard. We are going to create a second view controller so we can transition to that from the first view controller. To create a new view controller, drag a new "View Controller" from the objects palette in Interface Builder.

3. Create a new class called SecondViewController (Command+N, new Cocoa Touch Class (make sure to have iOS selected on the left hand side)).  
Adding view controllers in interface builder is very similar to adding regular objects. If you do not add them to your code, you will not be able to do anything with them programmatically. 
However, unlike other elements in Interface Builder, you do not just add the View Controller to your code as a property of a class. Rather, you create a new class file for that View Controller. Normally, our class named will be more descriptive, but this will work for now.
Now we must make our new View Controller be an instance of the SecondViewController class we just created. 

4. Go to the Identity Inspector of the View Controller in IB (interface builder) and make the class SecondViewController (the Identity Inspector is the little ID card on the top right when you have the view controller element selected in IB)
Make sure you are changing the second view controller's class and not the first one.
The first one has a little arrow pointing to it (which means it is the first view controller initialized by the app). We now have our two view controllers and have successfully "added" (created a class for) them in code. 

5. Now we must create a segue between them. Add a button to the first view controller. Don't worry about adding this button to your code.

6. Ctrl-drag from the button to the second view controller and choose "Show" (you will almost always choose this). Change the background color of the second view controller in its properties so that you can see the transition from the first view controller to the second. 

7. Run the application and see your transition. 

### AWW YEAH, LET THE CHILDREN RUN FREE

Congratz. You've created your first transition! Transitions are pretty much that. 

###SUPER IMPORTANT POINT
You probably realized that once you press the button to transition from the first view controller to the second, you have no way to get back to the first view controller. You also might be tempted to create a button on the second view controller and add a segue from that button back to the first. 

#### DO. NOT. DO. THIS.
When you transition from one view to another view, the first view is not deallocated. Rather, the second view is merely "pushed" on top of the first view.  
So, if you created a button to segue back to the first view, you would be stacking more and more views on top of your application until it finally crashed.  
Which is [bad](http://youtu.be/31j7HK0g1MU?t=25s).  
The proper way to transition back to the first view is by "dismissing" the current view.

In the app you created, add a button to the **second** view controller and add that button as a property to your SecondViewController class. 

In the method for that button, add the following
```objective-c
[self dismissViewControllerAnimated:YES completion:nil];
```

Try running your app and using the button.  
This method will now take the second view controller off the stack so that the first view controller's memory is used, as opposed to allocating new memory for another first view controller. 

There are other methods of transitioning (specifically Nav controllers, which are super important. You can google them or ask me about them if your curious).  

## SUPER REVIEW TIME!!!

We've gone through a lot of different concepts, so this assignment will cover a combination of all those. We've done the following topics.
* String manipulation in Objetctive-C
* Understanding Objective-C data types and primitives (C-types)
* Object Orientation and Classes in Objective-C
* The Model-View-Controller programming paradigm
* Data sources and Delegates (tableViews)
* Creating and linking interfaces in Interface Builder
* Custom class creation for Controllers
* Storyboards and transitions

Now we are ready to create a multifaceted application.

### The actual assignment

We are going to create a photo app. This app will display a list of the names of four images that are stored within the app. When an image name is selected, the image itself will be shown. At the bottom of the image, there will be a toolbar with one button that says "Notes". Pressing the "Notes" button will bring up a description of the image. 

I will not explicitly tell you how to do this in these instructions, but I will break it into 5 steps. You can ask me for help if you get stuck.

###Step 1: Create storyboard with scenes, segues, and IB elements
Create all the interface builder stuff. There should be 3 view controllers in total: one for the initial tableview, one for the image display, and one for the description display. The first view controller should store all the image names in a tableview. The second view controller should have a "Image View" object and a toolbar at the bottom with one button (The toolbar object already has one button on it. Use it). The third view controller should have a label where the description of the image can be stored as well as a button to dismiss the view controller itself. Create a segue from the first view controller to the second one (ctrl-drag from the prototype cell in the tableview in the first view controller to the second view controller). Then create a segue from the button in the second view controller to the third view controller. 

**AFTER ALL OF STEP 1 IS COMPLETED**, click on the first view controller. Go up to the "Editor" part of the top menu and choose "Embed In > Navigation Controller". This adds a navigation controller which gives you little buttons at the top of your view that will go to the previous view. They're nice. Use them. 

###Step 2: Add necessary code
Create a custom Photo class for use in your app. Give the photo 3 properties: a name, a filename, and a description. Create custom classes for your three view controllers and make sure that the view controllers themselves are instances of those classes in IB. Then, in the viewDidLoad method of the first view controller, create 4 objects of class Photo. Give them each a name (eg. "Frolicking Joe"), their filename that matches the filename they have without the extension (eg. "frolickingJoe"), and a description "Ah Joe. He frolicks so majestically." Add all these photos to an array for your table view (a property of your tableview class). Then, add a property of class Photo to your two other view controller classes (you will need to pass the selected photo between the view controllers).  
You can add the [photos](http://christmas-server.herokuapp.com/static/images/joePhotos.zip) by selecting the 4 photos and dragging them into the .xcassets in your Xcode project file navigator on the left hand side of the screen. You can store the photos in variables like so:
```objective-c
UIImage *image = [UIImage imageNamed:@"joeFrolicking"];
```

Note: Do not save the photos in the tableview's array. Save the name of the photos (stored within your Photo objects) and then access the image when they are selected (in your second view controller's class).

###Step 3: Add properties
Some of these you might already have.  

* tableview view controller
	- Photos array

* first view controller
	- single photo object

* second view controller
	- single photo object
	- details label

###Step 4: add the Photo objects to the tableview's array
'Nuff said

###Step 5: pass the Photo object between the view controllers
Try to figure this one out on your own. Ze Google is merciful. Ask if you get stuck

So that's it. Good luck!

