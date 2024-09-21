package kafka_tutorial.exercise_05_confluent_cloud;

import org.apache.kafka.clients.consumer.*;
import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ConsumerCloud {

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

    public static void main(String[] args) {
        Properties props = null;  // Declare props here
        try {
            props = loadConfig("client.properties");
            props.put(ConsumerConfig.GROUP_ID_CONFIG, "kafka-java-getting-started");
            props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

            KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(props);
            kafkaConsumer.subscribe(Arrays.asList("topic_java"));

            while (true) {
                ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("key = %s, value = %s%n", record.key(), record.value());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.err.println("Failed to load configuration file.");
        } finally {
            if (props != null) {  // Check if props is not null before trying to create a KafkaConsumer
                try (KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(props)) {
                    kafkaConsumer.close();
                }
            }
        }
    }
}
