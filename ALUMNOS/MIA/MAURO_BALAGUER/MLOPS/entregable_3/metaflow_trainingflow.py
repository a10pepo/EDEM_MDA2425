from metaflow import FlowSpec, Parameter, step
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

class TrainingFlow(FlowSpec):
    # Define the parameters for the flow
    max_depth = Parameter('max_depth', 
                         default=2, 
                         help='Max depth of the random forest classifier')
    n_estimators = Parameter('n_estimators', 
                            default=100, 
                            help='Number of estimators for the random forest classifier')
    random_state = Parameter('random_state', 
                           default=0, 
                           help='Random state for the random forest classifier')
    test_size = Parameter('test_size',
                         default=0.2,
                         help='Size of the test split')
    
    @step
    def start(self):
        # Start the flow
        print("Starting the training pipeline...")
        self.next(self.ingest_data)
        
    @step
    def ingest_data(self):
        from sklearn.datasets import load_iris
    
        # Load the iris dataset
        iris = load_iris()
        
        self.X = iris.data
        self.y = iris.target
        self.feature_names = iris.feature_names
        self.target_names = iris.target_names
        
        print("Data ingestion completed successfully.")
        self.next(self.split_data)

    @step
    def split_data(self):
        # Split the data into train and test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, 
            self.y, 
            test_size=self.test_size,
            random_state=self.random_state
        )
        
        print(f"Data split completed (test size: {self.test_size*100}%)")
        print(f"Train samples: {len(self.X_train)}")
        print(f"Test samples: {len(self.X_test)}")
        self.next(self.train)

    @step
    def train(self):
        # Train the model
        self.model = RandomForestClassifier(
            max_depth=self.max_depth,
            n_estimators=self.n_estimators,
            random_state=self.random_state
        )
        
        self.model.fit(self.X_train, self.y_train)
        
        print("Model training completed with parameters:")
        print(f"- max_depth: {self.max_depth}")
        print(f"- n_estimators: {self.n_estimators}")
        print(f"- random_state: {self.random_state}")
        self.next(self.show_metrics)

    @step
    def show_metrics(self):
        # Calculate and print metrics
        self.y_pred = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.report = classification_report(
            self.y_test, 
            self.y_pred, 
            target_names=self.target_names
        )
        
        print("\nModel Evaluation:")
        print(f"Accuracy: {self.accuracy:.2f}")
        print("\nClassification Report:")
        print(self.report)
        self.next(self.register_model)
        
    @step
    def register_model(self):
        # Save the model in a pickle file
        self.model_path = 'iris_model.pkl'
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)
        
        print(f"\nModel saved to {self.model_path}")
        self.next(self.end)
        
    @step
    def end(self):
        print("Training pipeline completed successfully!")
        
if __name__ == '__main__':
    TrainingFlow()
