POST_METHOD_DOCS = {
  'summary': 'Inserts information in database through endpoint',
  'description': 'Allows to insert information especified in request body in database.',
    # 'request': {
    #     'type': 'object',
    #     'properties': {
    #         'name': {
    #             'type': 'string',
    #             'description': 'Nombre del objeto'
    #         },
    #         'age': {
    #             'type': 'integer',
    #             'description': 'Edad del objeto'
    #         }
    #     },
    #     'required': ['name']
    # },
  'responses': {
      '201': {
          'description': 'Objeto creado exitosamente',
          'content': {
              'application/json': {
                  'schema': {
                      'type': 'object',
                      'properties': {
                          'id': {
                              'type': 'integer',
                              'description': 'ID del objeto creado'
                          },
                          'name': {
                              'type': 'string',
                              'description': 'Nombre del objeto creado'
                          },
                          'age': {
                              'type': 'integer',
                              'description': 'Edad del objeto creado'
                          }
                      }
                  }
              }
          }
      },
      '400': {
          'description': 'Solicitud inválida'
      }
  }
}