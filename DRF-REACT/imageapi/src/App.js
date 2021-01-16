import React, { useEffect, useState } from 'react';
import './App.css';
import Images from './components/images';
import ImageLoadingComponent from './components/ImageLoading';
import axiosInstance from './axios';

function App() {
	const ImageLoading = ImageLoadingComponent(Images);
	const [appState, setAppState] = useState({
		loading: true,
		images: null,
	});

	useEffect(() => {
		axiosInstance.get().then((res) => {
			const allImages = res.data;
			setAppState({ loading: false, images: allImages });
			console.log(res.data);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Image Repository</h1>
			<ImageLoading isLoading={appState.loading} images={appState.images} />
		</div>
	);
}
export default App;
