import React from 'react';
import { StyleSheet, View } from 'react-native';
import RealtorEvents from "@/components/RealtorEvents";

export default function App() {
  return (
      <View style={styles.container}>
        <RealtorEvents />
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});