def eleccion_tipo_de_calculo():
    eleccion = int(input("""Elige tipo de calculo:
0. Corte-corte o Relleno-Relleno
1. Terraplen-excavación
2. Mixto-Mixto
3. Mixto-excavación o mixto-terraplen
Elección: """))
    if eleccion == 0:
        calculo_corte_corte()
    elif eleccion == 1:
        calculo_terraplen_excavacion()
    elif eleccion == 2:
        calculo_mixto_mixto()
    elif eleccion == 3:
        calculo_mixto_excavacion()
    else:
        print('Elige una opción válida :v')
        eleccion_tipo_de_calculo()


def calculo_corte_corte():
    print("NOTA: ambas áreas deben se de corte o ambas áreas deben ser de relleno")
    longitud_entre_areas=float(input('Longitud entre áreas L[m]='))
    area1=float(input('Area 1 de corte o de relleno A1[m2]='))
    area2=float(input('Area 2 de corte o de relleno A2[m2]='))
    volumen=(area1+area2)/2*longitud_entre_areas
    print(f'Volumen de area o de relleno = {volumen}')
    pregunta_hacer_mas_calculos()


def calculo_terraplen_excavacion():
    longitud_entre_areas=float(input('Longitud entre áreas L[m]='))
    area_corte=float(input('Área de corte Ac[m2]='))
    area_relleno=float(input('Área de relleno Ar[m2]='))
    longitud_de_corte=area_corte*longitud_entre_areas/(area_corte+area_relleno)
    longitud_de_relleno=area_relleno*longitud_entre_areas/(area_corte+area_relleno)
    volumen_de_corte=longitud_de_corte*area_corte/2
    volumen_de_relleno=longitud_de_relleno*area_relleno/2
    print(f'longitud de corte Lc[m]={longitud_de_corte}')
    print(f'longitud de relleno Lr[m]={longitud_de_relleno}')
    print(f'volumen de corte Vc [m]={volumen_de_corte}')
    print(f'volumen de relleno Vr[m]={volumen_de_relleno}')
    pregunta_hacer_mas_calculos()


def calculo_mixto_mixto():
    longitud_entre_areas=float(input('Longitud entre áreas L[m]='))
    area_corte1=float(input('Área de corte Ac1[m2]='))
    area_relleno1=float(input('Área de relleno Ar1[m2]='))
    area_corte2=float(input('Área de corte Ac2[m2]='))
    area_relleno2=float(input('Área de relleno Ar2[m2]='))
    volumen_de_corte=(area_corte1+area_corte2)*longitud_entre_areas/2
    volumen_de_relleno=(area_relleno1+area_relleno2)*longitud_entre_areas/2
    print(f'volumen de corte Vc [m]={volumen_de_corte}')
    print(f'volumen de relleno Vr[m]={volumen_de_relleno}')
    pregunta_hacer_mas_calculos()


def calculo_mixto_excavacion():
    longitud_entre_areas=float(input('Longitud entre áreas L[m]='))
    area_corte1=float(input('Área de corte Ac1[m2]='))
    area_relleno1=float(input('Área de relleno Ar1[m2]='))
    area2=float(input('Área de corte o de relleno A2[m2]='))
    eleccion = eleccion_corte_o_relleno()
    if eleccion == 0:
        volumen_de_corte = (area_corte1+area2)/2*longitud_entre_areas
        k=area2*area_relleno1/(area_corte1+area_relleno1)
        longitud_de_relleno = area_relleno1*longitud_entre_areas/(k+area_relleno1)
        longitud_de_corte = longitud_entre_areas-longitud_de_relleno
        volumen_de_relleno = area_relleno1*longitud_de_relleno/2
    elif eleccion == 1:
        volumen_de_relleno = (area_relleno1+area2)/2*longitud_entre_areas
        k=area2*area_corte1/(area_corte1+area_relleno1)
        longitud_de_corte=longitud_entre_areas*area_corte1/(area_corte1+k)
        longitud_de_relleno = longitud_entre_areas-longitud_de_corte
        volumen_de_corte = area2*longitud_de_corte/2
    print(f'Valor de K= {k}')
    print(f'longitud de corte Lc[m]={longitud_de_corte}')
    print(f'longitud de relleno Lr[m]={longitud_de_relleno}')
    print(f'volumen de corte Vc [m]={volumen_de_corte}')
    print(f'volumen de relleno Vr[m]={volumen_de_relleno}')
    pregunta_hacer_mas_calculos()


def eleccion_corte_o_relleno():
    eleccion=int(input("""¿A2 es area de conrte o de relleno?
0. Corte
1. Relleno
Elección: """))
    if eleccion == 0:
        return 0
    elif eleccion == 1:
        return 1
    else:
        print('Elge una opción válida')
        return eleccion_corte_o_relleno()


def pregunta_hacer_mas_calculos():
    eleccion=int(input("""¿Desea hacer mas calculos?
0. No
1. Si
Elección: """))
    if eleccion == 0:
        print('Gracias por usar mi programa. github.com/Jared-DL')
    elif eleccion == 1:
        eleccion_tipo_de_calculo()
    else:
        print('Elige una opción válida')
        pregunta_hacer_mas_calculos()


if __name__ == "__main__":
    print('---Calculo de volumenes para carreteras---')
    eleccion_tipo_de_calculo()