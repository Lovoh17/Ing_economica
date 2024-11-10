from django.shortcuts import render

def bienvenida(request):
    if request.method == 'POST':
        # Obtener los datos del formulario (ejemplo de cálculo de valor futuro)
        try:
            capital_inicial = float(request.POST['capital_inicial'])
            tasa_interes = float(request.POST['tasa_interes']) / 100
            tiempo = int(request.POST['tiempo'])

            # Cálculo de valor futuro (F = P(1 + i)^n)
            valor_futuro = capital_inicial * (1 + tasa_interes) ** tiempo
            resultado = round(valor_futuro, 2)

            return render(request, 'index.html', {'resultado': resultado, 'capital_inicial': capital_inicial, 'tasa_interes': tasa_interes, 'tiempo': tiempo})
        except ValueError:
            return render(request, 'index.html', {'error': 'Por favor ingrese valores válidos.'})
    return render(request, 'index.html')

def conversion_intereses(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            tasa_interes = float(request.POST["tasa_interes"])
            periodos = int(request.POST["periodos"])
            tipo_conversion = request.POST["tipo_conversion"]

            if tipo_conversion == "nominal_a_efectivo":
                # Convertir de nominal a efectivo
                tasa_interes_efectiva = (1 + (tasa_interes / 100) / periodos) ** periodos - 1
                resultado = round(tasa_interes_efectiva * 100, 4)
            elif tipo_conversion == "efectivo_a_nominal":
                # Convertir de efectivo a nominal
                tasa_interes_nominal = ((1 + tasa_interes / 100) ** (1 / periodos) - 1) * periodos
                resultado = round(tasa_interes_nominal, 4)

        except Exception as e:
            error = "Hubo un error en la conversión. Asegúrate de que los datos sean correctos."

    return render(request, 'calculadora.html', {'resultado': resultado, 'error': error})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def convertir_tasa(request):
    resultado_nominal_a_efectiva = None
    resultado_efectiva_a_nominal = None

    if request.method == 'POST':
        # Obtener los datos del formulario de Nominal a Efectiva
        if 'tasa_nominal' in request.POST:  # Formulario para convertir de Nominal a Efectiva
            tasa_nominal = float(request.POST.get('tasa_nominal'))
            frecuencia_interes = int(request.POST.get('frecuencia_interes'))
            frecuencia_capitalizacion = int(request.POST.get('frecuencia_capitalizacion'))

            # Número de periodos por año (frecuencia)
            n_interes = frecuencia_interes
            n_capitalizacion = frecuencia_capitalizacion

            # Convertir de tasa nominal a efectiva
            tasa_efectiva_resultado = (1 + tasa_nominal / 100 / n_capitalizacion) ** n_interes - 1
            resultado_nominal_a_efectiva = f"Tasa efectiva: {tasa_efectiva_resultado * 100:.4f}%"
        
        # Obtener los datos del formulario de Efectiva a Nominal
        elif 'tasa_efectiva' in request.POST:  # Formulario para convertir de Efectiva a Nominal
            tasa_efectiva = float(request.POST.get('tasa_efectiva'))
            frecuencia_interes_efectiva = int(request.POST.get('frecuencia_interes_efectiva'))
            frecuencia_capitalizacion_efectiva = int(request.POST.get('frecuencia_capitalizacion_efectiva'))

            # Número de periodos por año (frecuencia)
            n_interes = frecuencia_interes_efectiva
            n_capitalizacion = frecuencia_capitalizacion_efectiva

            # Convertir de tasa efectiva a nominal usando la fórmula correcta
            tasa_nominal_resultado = n_capitalizacion * ((1 + tasa_efectiva / 100) ** (1 / n_interes) - 1)
            resultado_efectiva_a_nominal = f"Tasa nominal: {tasa_nominal_resultado * 100:.4f}%"

    return render(request, 'conversion_tasas.html', {
        'resultado_nominal_a_efectiva': resultado_nominal_a_efectiva,
        'resultado_efectiva_a_nominal': resultado_efectiva_a_nominal
    })