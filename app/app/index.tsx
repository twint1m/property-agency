import { StyleSheet } from 'react-native';
import { View } from 'react-native';
import RealtorEvents from '@/components/RealtorEvents';

export default function MainScreen() {
  return (
      <View style={styles.container}>
        <RealtorEvents />
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});