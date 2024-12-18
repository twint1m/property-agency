import React, { useEffect, useState } from 'react';
import { FlatList, Text, View, StyleSheet, Alert, Platform, StatusBar } from 'react-native';

type Event = {
    datetime: string | null;
    duration: string | null;
    event_type: string | null;
    comment: string;
};

const RealtorEvents = () => {
    const [events, setEvents] = useState<Event[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/real_estate/events/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => setEvents(data))
            .catch(error => {
                console.error(error);
                setError(error.message);
            });
    }, []);

    useEffect(() => {
        if (error) {
            Alert.alert('Error', error);
        }
    }, [error]);

    const renderItem = ({ item }: { item: Event }) => (
        <View style={styles.item}>
            <Text style={styles.title}>{item.event_type}</Text>
            <Text>{item.datetime ? new Date(item.datetime).toLocaleString() : 'No date'}</Text>
            <Text>{item.comment}</Text>
        </View>
    );

    return (
        <View style={styles.container}>
            <FlatList
                data={events}
                renderItem={renderItem}
                keyExtractor={(item, index) => index.toString()}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 55, // Отступ сверху для iOS и Android
        backgroundColor: '#f0f0f0',
    },
    item: {
        padding: 20,
        marginVertical: 8,
        marginHorizontal: 16,
        backgroundColor: '#fff',
        borderRadius: 8,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 8,
        elevation: 2,
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
    },
});

export default RealtorEvents;