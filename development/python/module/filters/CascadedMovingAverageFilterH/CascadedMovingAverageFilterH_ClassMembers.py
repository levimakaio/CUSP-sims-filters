from ..projectHeader                    import *                                #project Header Script


cascadedMovingAverageFilter_typ._fields_ = [('numFilters'                            , I                                          ),
                                            ('pY'                                    , P(D)                                       ),
                                            ('filterArray'                           , P(movingAverageFilter_typ)                 )]

