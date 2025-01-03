package kafka_tutorial.exercise_05_confluent_cloud;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;

public class ProducerCloud {

    public static Properties loadConfig(final String configFile) throws IOException {
        if (!Files.exists(Paths.get(configFile))) {
            throw new IOException(configFile + " not found.");
        }
        final Properties cfg = new Properties();
        try (InputStream inputStream = new FileInputStream(configFile)) {
            cfg.load(inputStream);
        }
        return cfg;
    }

    public static void main(String[] args){
        try {
            final Properties props = loadConfig("client.properties");

            KafkaProducer<String, String> kafkaProducer = new KafkaProducer<>(props);
            try{
                for(int i = 0; i < 100; i++){
                    int value = i*4;
                    System.out.println(i);
                    kafkaProducer.send(new ProducerRecord<String, String>("topic_java", Integer.toString(i), "test message - " + value));
                }
            } catch (Exception e){
                e.printStackTrace();
            } finally {
                kafkaProducer.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.err.println("Failed to load configuration file.");
        }
    }
}
