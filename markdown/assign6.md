# Assignment 6
## Ugh gosh....TableViews

Let me start out this assignment by saying TableViews are the absolute worst. Like the worst. You haven't seen the horror that are TableViews. Hell hath no fury like a TableView. If you had a choice between a roundhouse kick to the face by God and a TableView, choose the kick. In his famous theological fantasy, C.S. Lewis almost accurately describes the sensation of hell. He left out the tableViews because of the amount of pain they induce. Thank you, C.S. Lewis.

# THE WOOOOOOOOOOOOOOOOOOOOOOOOOORST

### Okay, I'm done

Say you wanted to create a tableView for your iOS app. You would be forgiven if you thought that it was a simple matter of dragging a tableView object in from the object selecter in interface builder and adding the tableView cells in by typing them in a pretty little item selector thing...

###Dead. Wrong.

Beyond dead. Stomped on by the mighty foot of the protector of virginity himself, His Moranliness III. Quite dead.

TableView objects must be told how many sections they are to have, how many rows are in each section, and what should be displayed in each cell. Yeah. Terrible. Lazy POS.

This is essentially what happens:
* App Starts
* a tableView object, littleTableView, is instantiated
* littleTableView is confused about it's life and knows nothing because it's a whiny, good-for-nothing moron.
* littleTableView asks another object for information about it's existence (such as numberOfSections, numberOfRowsInSection, cellInfo)
* littleTableView, after having everyone else tell it what to do, finally displays what it has been handed on a platter.
Damn you littleTableView. Could you do any less.

The objects that contain the information about littleTableView are called littleTableView's Delegate and DataSource. The Delegate and DataSource of an element contain methods that return information about that element. Those methods are called whenever an element of that type is instantiated. In order to specify a delegate and a datasource for an element, you have to ctrl-drag from the element to the element's datasource and/or delegate. A popup menu should appear allowing you to choose which would you would prefer.

Usually, the controller for the view in which the tableView resides is chosen as the tableView's delegate and datasource. The same 3 step method for interfaces applies (which a few differences)

* Create the tableView element
* create the "identifier" in the code (usually the controller) for the delegate and datasource
* Link the two

Delegates and DataSources are specified by using protocols. If a class "follows" an Objective-C protocol, that means it implements all of the "required" methods (as defined by the protocol) and any "optional" methods that it likes.
You can specify that a class follows a protocol by adding <> to it's interface
```objective-c
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>

@end

```

There are three methods required by the UITableViewDataSource. They are the following:
```objective-c
// sections in row
-(NSInteger)numberOfSectionsInTableView:(UITableView *)tableView

// rows in section
-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section

// cell
-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
```

The implementation of the first two is pretty simple. Usually, the view controller contains the model that stores the data you want, so the number of sections and rows is some function of that. For example, if my ViewController had a property NSArray *names that contained some names and I wanted to display the names in a tableView all in one section, the first two implementations would be like so:

```objective-c
// in ViewController.m

-(NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
	return 1;
}

// rows in section
-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
	return self.names.count;
}
```

The cell implementation is a little different. I will write it and then explain.

```objective-c
-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"cell" forIndexPath:indexPath];

    cell.textLabel.text = self.names[indexPath.row];

    return cell;
    
}
```

### This. This is why the Aztecs fell.

First line:
So, if you had an array with 500,000 elements and tried to instantiate a block of memory for each cell as you scrolled through them, you would crash your phone. the `-dequeueReusableCellWithIdentifier` method deques a cell if it is not in use and reuses its memory. Google it. 

Second line:
indexPath is an object that has a row and section property of the current cell. Use it.

Third line:
return the cell.

If you were paying close attention, you might be wondering "the dequeueblahblahblah" method only works if a cell already exists, but we never created a cell.
Correct you are. We must first create the initial cell. However, we do not do that in our code. We do that in our interface tableView. 

Go back to the storybord and click on the tableView (make sure you have the tableView itself selected and not something else). Click on the attributes inspector in the top right of the screen. You should see available attributes for the tableView. Increase the "Prototype Cells" attribute from 0 to 1. This instantiates our initial cell.
We must give this cell an identifier just in case we have multiple tableViews. Click on the newly created prototype cell. In its attributes, change its identifier to "cell" (to match what you put in the method).

Make sure your ViewController is linked as delegate and DataSource to your tableView. Then you should be done.

Finally. TableViews.
Gosh.

### The actual assignment
Create a tableView that displays 9 names. Make them good names.


### Goals
* Understand the behemoth that is a tableView
* Learn the meaning of true pain
* Further understand interface stuff
