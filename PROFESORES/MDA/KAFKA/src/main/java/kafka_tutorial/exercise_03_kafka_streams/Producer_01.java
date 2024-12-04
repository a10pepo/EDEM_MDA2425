package kafka_tutorial.exercise_03_kafka_streams;

import com.github.javafaker.Book;
import com.github.javafaker.Commerce;
import com.github.javafaker.Faker;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class Producer_01 {

    public static void main(String[] args){
        Faker faker = new Faker();
        for(int i = 0; i < 100000; i++){


            System.out.println(faker.artist().name());

            //System.out.println(quote);
            //kafkaProducer.send(new ProducerRecord<String, String>("quotes-input", quote ));
        }


        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> kafkaProducer = new KafkaProducer<String, String>(properties);

        try{
            for(int i = 0; i < 100000; i++){
                Thread.sleep(100);
                Book b = faker.book();
                System.out.println(b.author() + "   " + b.genre()  + "   " + b.publisher()  + "   "  + b.title() );
                String quote = faker.shakespeare().asYouLikeItQuote();
                //System.out.println(quote);
                //kafkaProducer.send(new ProducerRecord<String, String>("quotes-input", quote ));
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            kafkaProducer.close();
        }
    }
}