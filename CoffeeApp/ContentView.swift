//
//  ContentView.swift
//  CoffeeApp
//
//  Created by isabelmendes on 21/03/25.
//

import SwiftUI

struct ContentView: View {
    @State private var showMessage = false
    
    var body: some View {
        NavigationStack {
            VStack {
                Button(action: {
                    showMessage.toggle()
                }) {
                    Text("Coffee App")
                        .font(.title)
                        .padding()
                        .background(Color.brown)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
                
                if showMessage {
                    Text("Test your coffee! ☕")
                        .font(.headline)
                        .padding()
                        .transition(.opacity)
                }
                
                Spacer()
                
                // Navigation Button
                NavigationLink(destination: SecondView()) {
                    HStack {
                        Text("Next Page")
                            .font(.title2)
                            .foregroundColor(.white)
                        Image(systemName: "arrow.right")
                            .foregroundColor(.white)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color.brown)
                    .cornerRadius(10)
                    .padding(.bottom, 20)
                }
            }
            .padding()
        }
    }
}


