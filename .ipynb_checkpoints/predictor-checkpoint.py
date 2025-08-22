{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6da0403c-2df0-42d3-b1c6-4f30da9276e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "def predict_default(input_dict):\n",
    "    \"\"\"\n",
    "    Função simples para predição de default\n",
    "    \n",
    "    Exemplo de uso:\n",
    "    input_data = {\"ioi_3months\": 3, \"valor_vencido\":125000, \"valor_total_pedido\":35000}\n",
    "    resultado = predict_default(input_data)\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Carregar modelo e preprocessor\n",
    "        model = joblib.load('modelo_default.pkl')\n",
    "        preprocessor = joblib.load('preprocessor.pkl')\n",
    "        \n",
    "        # Converter para DataFrame\n",
    "        input_df = pd.DataFrame([input_dict])\n",
    "        \n",
    "        # Fazer predição\n",
    "        prediction = model.predict(input_df)[0]\n",
    "        \n",
    "        return {\"default\": str(prediction)}\n",
    "        \n",
    "    except Exception as e:\n",
    "        return {\"error\": str(e)}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
