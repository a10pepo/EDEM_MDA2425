from metaflow import FlowSpec, Parameter, step

class TrainingFlow(FlowSpec):
    # Define the parameters for the flow
    max_depth = Parameter('max_depth', default=2, help='Max depth of the random forest classifier')
    n_estimators = Parameter('n_estimators', default=100, help='Number of estimators for the random forest classifier')
    random_state = Parameter('random_state', default=0, help='Random state for the random forest classifier')
    
    @step
    def start(self):
        # Start the flow
        self.next(self.ingest_data)
        
    @step
    def ingest_data(self):
        from sklearn.datasets import load_iris
    
        # Load the iris dataset
        iris = load_iris()
        
        #pylint: disable=no-member
        self.X = iris.data
        self.y = iris.target
        #pylint: enable=no-member
        
        self.next(self.split_data)

    @step
    def split_data(self):
        #Split the data into train and test
        # TODO: WRITE YOUR CODE HERE
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.random_state)

        self.next(self.train)


    @step
    def train(self):
        # Train the model
        # TODO: WRITE YOUR CODE HERE
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            random_state=self.random_state
        )
        self.model.fit(self.X_train, self.y_train)
        self.next(self.show_metrics)

    @step
    def show_metrics(self):
        # Print some metrics
        # TODO: WRITE YOUR CODE HERE
        y_pred = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, y_pred)
        print(f'Accuracy: {self.accuracy:.4f}')
        self.next(self.register_model)
        
    @step
    def register_model(self):
        # Save the model in a pickle file in local storage
        # TODO: WRITE YOUR CODE HERE
        joblib.dump(self.model, 'iris_model.pkl')
        print("Model saved as 'iris_model.pkl'")
        self.next(self.end)
        
    @step
    def end(self):

        pass
    
if __name__ == '__main__':
    TrainingFlow()
