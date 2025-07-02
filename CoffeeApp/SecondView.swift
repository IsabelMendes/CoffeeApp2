//
//  SecondView.swift
//  CoffeeApp
//
//  Created by isabelmendes on 21/03/25.
//

import SwiftUI
import PhotosUI

struct SecondView: View {
    @State private var selectedImage: UIImage? // Store the captured image
    @State private var isShowingCamera = false // Control camera display

    var body: some View {
        VStack {
            // New welcome text at the top
            Text("Welcome to the Classification Coffee!")
                .font(.largeTitle)
                .fontWeight(.bold)
                .multilineTextAlignment(.center)
                .padding(.top, 20)

            Text("Take a picture of a coffee bean! 📸")
                .font(.title2)
                .multilineTextAlignment(.center)
                .padding()

            if let image = selectedImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 300)
                    .cornerRadius(10)
                    .padding()
            } else {
                Text("No image captured yet.")
                    .foregroundColor(.gray)
                    .padding()
            }

            Button(action: {
                isShowingCamera = true
            }) {
                HStack {
                    Image(systemName: "camera")
                    Text("Open Camera")
                }
                .font(.title2)
                .padding()
                .frame(maxWidth: .infinity)
                .background(Color.brown)
                .foregroundColor(.white)
                .cornerRadius(10)
                .padding(.top, 20)
            }
            .sheet(isPresented: $isShowingCamera) {
                CameraView(selectedImage: $selectedImage)
            }

            Spacer()
        }
        .navigationTitle("Capture Coffee Bean")
        .padding()
    }
}


