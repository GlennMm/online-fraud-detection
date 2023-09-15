export interface ModelResult {
    accuracy: number
    precision: number
    f1: number
}

export interface PredictionResult {
    classification: number
    probability: number
}

export interface ModelState {
    state: boolean
}