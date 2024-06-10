from ..projectHeader                    import *                                #project Header Script


SOSFilterTDF2_typ._fields_ = [('pY'                                    , P(D)                                       ),
                              ('order'                                 , I                                          ),
                              ('numFilters'                            , I                                          ),
                              ('biquadFilterArray'                     , P(biquadFilterTDF2_typ)                    )]

