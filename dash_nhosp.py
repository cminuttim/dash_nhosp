#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Carlos Minutti Martinez <carlos.minutti@iimas.unam.mx>
@author: Miguel Félix Mata Rivera <mmatar@ipn.mx >


Resumen:
    
Los modelos presentados muestran la estimación del número de hospitalizaciones esperadas por localidad en la CDMX, dependiendo de diversos factores, como lo son la delegación, el mes, factores socio-económicos y de contaminación, etc.

Valores positivos representan variables / factores que aumentan el número de hospitalizaciones esperadas y su valor muestra la magnitud del efecto que tiene en el número de casos esperados. A su vez, valores negativos representan menor número de casos esperados debidos a la variable.

Únicamente se presentan en cada modelo las variables que muestran un efecto estadísticamente significativo, por lo que variables ausentes (con respecto a otros modelos), no influyen significativamente con respecto a la media.

La descripción de cada variable, la magnitud de su efecto y su p-value, se muestra al colocar el puntero del ratón sobre cada barra.

Es importante mencionar que el sistema no pretende ser utilizado para determinar el número de hospitalizaciones a esperar, sino que es un modelo estadístico para estudiar cómo interactúan los diferentes factores en cada enfermedad, para las hospitalizaciones ocurridas dentro de la Zona Valle de México.


El modelo final se genera mediante Regresión Binomial Negativa. El archivo PICKLE original de los modelos no se incluye por razones de privacidad de los datos, en su lugar se incluye un archivo PICKLE generado a partir de datos sintéticos.

Licencia:    
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS


"""

import pickle
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask

import statsmodels.api as sm
import statsmodels.formula.api as smf



# Cargar modelo
with open('n_hosp.pickle', 'rb') as handle:
    models_dict = pickle.load(handle)
    

models = models_dict['models']
models_c = []

# Variables del modelo    
model_vars = models_dict['model_vars']

var_names = model_vars.index.values


var_effect_list = ['Ambos', 'Aumenta', 'Disminuye']

models_name = models_dict['models_name'] 
models_type = ['Todas', 'Crónicas']
models_select = models
model_vars_sel = ['Cualquiera'] + list(model_vars.index.values)


def get_cie_lst(vars_l, type_cie, effect):
    
    any_var = False
    if model_vars_sel[0] in vars_l:
        vars_l.remove(model_vars_sel[0])
        any_var = True
    
    vars_l = pd.Series(vars_l)
    
    cie_match = []
    for cie in models:
        cie_model = models_dict[cie+'_NB']
        pars = cie_model.params[1:]
        v = vars_l.isin(pars.index)
        
        if (not any_var) and (not all(v)):
            continue
            
        if type_cie!=models_type[0] and not (cie in models_c):
            continue
            
        if (not any_var):
            if effect=='Aumenta' and any(pars[vars_l[v]]<0):
                continue
    
            if effect=='Disminuye' and any(pars[vars_l[v]]>0):
                continue

        cie_match.append(cie)
        
    return cie_match
        
    

def min_max_scaler(X, xmin=None, xmax=None):
    
    if type(xmin)==type(None):
        xmin = X.min()
    if type(xmax)==type(None):
        xmax = X.max()
    
    X_tmp = X.copy()
        
    idx = xmin.index[xmin==xmax]
    idx = idx[idx.isin(X_tmp.columns)]
    if idx.shape[0]>0:
        X_tmp[idx] = 0
    
    idx = xmin.index[(xmin<xmax) * ((xmin!=0) + (xmax!=1))]
    idx = idx[idx.isin(X_tmp.columns)]
    
    X_tmp[idx] = (X_tmp[idx]-xmin[idx])/(xmax[idx]-xmin[idx])

    return (X_tmp, xmin, xmax)


def risk_bar_plot(cie):
    
    if len(cie)==0:
        return None
    cie_desc = models_name[cie]
    
    cie_model = models_dict[cie+'_NB']    
    
    pars = cie_model.params[1:].sort_values(ascending=False)
    p_val = cie_model.pvalues[pars.index]
    max_val = pars.abs().max()
                

    df = {'par': pars.index, 'val': pars, 'desc': model_vars[pars.index], 'pval':p_val}
    risk = pd.DataFrame.from_dict(df)
    risk.set_index(risk['par'])
    risk['val'] = np.round(risk['val'],3)
    risk['pval'] = np.round(risk['pval'],4)
    
    fig = px.bar(risk, x='par', y='val', title=f'Variables que influyen en {cie_desc} ({cie})', 
                 labels={'par':'Variable', 'val':'Efecto', 'desc':'Descripción', 'pval':'p-value'},
                 hover_data=['par', 'desc', 'val', 'pval'],
                 color='val', range_color=[-max_val,max_val], color_continuous_scale='bluered', template="plotly_white") #ylorrd, bluered, peach
    
    fig.update_layout(hovermode="x")    
    
    return fig


# app en /n_hosp (se requiere llamar a flask)
app_flask = flask.Flask(__name__)
app = dash.Dash(__name__, server=app_flask, url_base_pathname='/n_hosp/')

app_flask.route('/n_hosp/')
def render_dashboard():
	return flask.redirect('/n_hosp/')




edad_list = range(121)
sexo_list = ['M', 'F']
talla_list = range(20, 251)
peso_list = range(201)

app.layout = html.Div([
    html.H1("Modelos de predicción del número de hospitalizaciones evitables", style={'text-align': 'center', 'color': '#666666'}),
    
    html.Div([
        html.Span("Los modelos presentados muestran la estimación del número de hospitalizaciones esperadas por localidad en la CDMX, dependiendo de diversos factores, como lo son la delegación, el mes, factores socio-económicos y de contaminación, etc."),
        html.P(),
        html.Span("Valores positivos representan variables / factores que aumentan el número de hospitalizaciones esperadas y su valor muestra la magnitud del efecto que tiene en el número de casos esperados. A su vez, valores negativos representan menor número de casos esperados debidos a la variable."),
        html.P(),
        html.Span("Únicamente se presentan en cada modelo las variables que muestran un efecto estadísticamente significativo, por lo que variables ausentes (con respecto a otros modelos), no influyen significativamente con respecto a la media."),
        html.P(),
        html.Span("La descripción de cada variable, la magnitud de su efecto y su p-value, \
        se muestra al colocar el puntero del ratón sobre cada barra."),
        ], style={'color': '#666666', 'float':'right', 'padding':'8px', 'border':'1px solid #cecece',
        'margin':'5px 100px 20px 30px', 'width':'30%', 'min-height':'250px', 'font-size':'11pt'}),

    
    html.P(' ', style={'height':'10px'}),
    html.Div("Variables:", style={'color': '#333333', 'margin-left':'20px'}),

    dcc.Dropdown(
        id='vars-list',
        options=[{'label': (f"{i} - {model_vars[i]}" if (i!=model_vars_sel[0]) else i), 'value': i} for i in model_vars_sel],
        value=[model_vars_sel[0]],  # Valor por defecto
        multi=True,
        searchable=True,
        style={'width':'70%', 'margin-left':'10px'}
    ),


    html.P(' ', style={'height':'-10px'}),
    html.Div("Aumenta o dismunuye el numero de casos:", style={'color': '#333333', 'margin-left':'20px'}),

    dcc.Dropdown(id='effect-select', options=[{'label': i, 'value': i} for i in var_effect_list],
                 searchable=False,
                 value=var_effect_list[0], style={'width': '250px','float':'left', 'margin-left':'10px'}),


    html.P(' ', style={'height':'20px'}),
    html.Div("Tipo:", style={'color': '#333333', 'margin-left':'20px'}),

    dcc.Dropdown(
        id='type-select',
        options=[{'label': i, 'value': i} for i in models_type],
        value=models_type[0],  # Valor por defecto
        multi=False,
        searchable=False,
        style={'width':'250px', 'margin-left':'10px'}
    ),


    html.P(' ', style={'height':'-10px'}),
    html.Div("Modelos disponibles:", style={'color': '#333333', 'margin-left':'20px'}),
    
    dcc.Dropdown(
        id='models-select',
        options=[{'label': f"{i} - {models_name[i]}", 'value': i} for i in models_select],
        value=models_select[0],  # Valor por defecto
        multi=False,
        searchable=True,
        style={'width':'70%', 'margin-left':'10px'}
    ),

    html.P(' ', style={'height':'20px'}),
        
    dcc.Graph(id='risk-graph', figure={}, style={'width':'95%','float':'left'})
])


@app.callback(
    [Output('models-select', 'options'),Output('models-select', 'value')],
    [Input('vars-list', 'value'),
    Input('type-select', 'value'),
    Input('effect-select', 'value')]
)
def update_cie_lst(vars_l, type_cie, effect):

    
    cie_lst = models_select
    if(vars_l!=model_vars_sel[0] or type_cie!=models_type[0] or effect!=var_effect_list[0]):
        cie_lst = get_cie_lst(vars_l, type_cie, effect)
    
    return ([{'label': f"{i} - {models_name[i]}", 'value': i} for i in cie_lst], cie_lst[0])

@app.callback(
    Output('risk-graph', 'figure'),
    [Input('vars-list', 'value'),
    Input('type-select', 'value'),
    Input('effect-select', 'value'),
    Input('models-select', 'value')]
)
def update_graph_p(vars_l, type_cie, effect, mod):
    return risk_bar_plot(mod)



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server("0.0.0.0", 8443, debug=False)
