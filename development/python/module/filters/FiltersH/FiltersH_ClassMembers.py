from ..projectHeader                    import *                                #project Header Script


AS_RollingBuffer_typ._fields_ = [('pData'                                 , P(D)                                       ),
                                 ('dimension'                             , LU                                         ),
                                 ('size'                                  , LU                                         ),
                                 ('index'                                 , LU                                         ),
                                 ('numValid'                              , LU                                         )]


AS_MovingAverageFilter_typ._fields_ = [('windowSize'                            , LU                                         ),
                                       ('pY'                                    , P(D)                                       ),
                                       ('pBuffer'                               , P(AS_RollingBuffer_typ)                    )]


AS_CMAFilter_typ._fields_ = [('numFilters'                            , LU                                         ),
                             ('pY'                                    , P(D)                                       ),
                             ('MAFilterArray'                         , P(AS_MovingAverageFilter_typ)              )]


AS_BiquadFilter_typ._fields_ = [('dim'                                   , LU                                         ),
                                ('pY'                                    , P(D)                                       ),
                                ('pS1'                                   , P(D)                                       ),
                                ('pS2'                                   , P(D)                                       ),
                                ('coef'                                  , D * 6                                      )]


AS_SOSFilter_typ._fields_ = [('pY'                                    , P(D)                                       ),
                             ('order'                                 , LU                                         ),
                             ('numFilters'                            , LU                                         ),
                             ('biquadFilterArray'                     , P(AS_BiquadFilter_typ)                     )]

