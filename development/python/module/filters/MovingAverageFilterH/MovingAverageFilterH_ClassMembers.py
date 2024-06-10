from ..projectHeader                    import *                                #project Header Script


movingAverageFilter_typ._fields_ = [('windowSize'                            , LU                                         ),
                                    ('pY'                                    , P(D)                                       ),
                                    ('pBuffer'                               , P(rollingBuffer_typ)                       )]

